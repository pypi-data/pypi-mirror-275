import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
import utils


class ProGBN(nn.Module):
    """
        Bayesian Progressive Deep Topic Model with Knowledge Informed Textual Data Coarsening Process. ICML 2023.

        Zhibin Duan, Xinyang Liu, Yudi Su, Yishi Xu, Bo Chen, Mingyuan Zhou.

        https://github.com/xinyangATK/ProGBN
    """
    def __init__(self, vocab_size, num_topics_list, MBratio=100, hidden_size=512, embed_size=100, dropout=0.5, pc=True, device='cpu'):
        super(ProGBN, self).__init__()

        self.real_min = torch.tensor(1e-30)
        self.wei_shape_max = torch.tensor(1.0).float()
        self.wei_shape = torch.tensor(1e-1).float()

        self.vocab_size = vocab_size
        self.hidden_size = hidden_size
        self.embed_size = embed_size

        self.num_topic_list = num_topics_list[::-1]
        self.topic_size = [self.vocab_size] + self.num_topic_list
        self.num_layers = len(num_topics_list)

        self.adj = []
        for layer in range(self.num_layers - 1):
            self.adj.append(args.adj[layer])

        self.pos_weight = []
        self.edge_index = []
        for layer in range(self.num_layers - 1):
            pos_weight = (self.adj[layer].shape[0] ** 2 - self.adj[layer].sum()) / self.adj[layer].sum()
            weight_mask = self.adj[layer].view(-1) == 1
            weight_tensor = torch.ones(weight_mask.size(0)).cuda()
            weight_tensor[weight_mask] = pos_weight
            self.pos_weight.append(weight_tensor)
            self.edge_index.append(self.adj[layer].nonzero().t())

        self.bn_layer = nn.ModuleList([nn.BatchNorm1d(self.hidden_size) for i in range(self.num_layers)])

        h_encoder = [utils.DeepConv1D(self.hidden_size, 1, self.vocab_size)]
        for i in range(self.num_layers - 1):
            h_encoder.append(utils.ResConv1D(self.hidden_size, 1, self.hidden_size))

        self.h_encoder = nn.ModuleList(h_encoder)

        shape_encoder = [utils.Conv1D(self.topic_size[i + 1], 1, self.topic_size[i + 1] + self.hidden_size) for i in range(self.num_layers - 1)]
        shape_encoder.append(utils.Conv1D(self.topic_size[self.num_layers], 1, self.hidden_size))
        self.shape_encoder = nn.ModuleList(shape_encoder)

        # gam_shape_encoder = [utils.Conv1D(self.topic_size[i + 1], 1, self.topic_size[i + 1] + self.hidden_size) for i in range(self.num_layers - 1)]
        # gam_shape_encoder.append(utils.Conv1D(self.topic_size[self.num_layers], 1, self.hidden_size))
        # self.gam_shape_encoder = nn.ModuleList(gam_shape_encoder)

        scale_encoder = [utils.Conv1D(self.topic_size[i + 1], 1, self.topic_size[i + 1] + self.hidden_size) for i in range(self.num_layers - 1)]
        scale_encoder.append(utils.Conv1D(self.topic_size[self.num_layers], 1, self.hidden_size))
        self.scale_encoder = nn.ModuleList(scale_encoder)

        topic_embedding = [utils.Get_topic_embedding(self.topic_size[i], self.embed_size) for i in range(self.num_layers + 1)]
        self.topic_embedding = nn.ModuleList(topic_embedding)

        decoder = [utils.Conv1DSoftmaxEtm(self.topic_size[i], self.topic_size[i + 1], self.embed_size) for i in
                   range(self.num_layers)]
        self.decoder = nn.ModuleList(decoder)

        for t in range(self.num_layers - 1, -1, 1):
            self.decoder[t - 1].alphas = self.decoder[t].rho

        self.rho = [0] * self.num_layers
        self.rho_graph_encoder = nn.ModuleList()
        for layer in range(self.num_layers - 1):
            self.rho_graph_encoder.append(GCNConv(in_channels=self.embed_size, out_channels=self.embed_size).cuda())

    def reparameterize(self, Wei_shape_res, Wei_scale, Sample_num=1):
        # sample one
        eps = torch.cuda.FloatTensor(Sample_num, Wei_shape_res.shape[0], Wei_shape_res.shape[1]).uniform_(0, 1)
        theta = torch.unsqueeze(Wei_scale, axis=0).repeat(Sample_num, 1, 1) * torch.pow(-utils.log_max(1 - eps), torch.unsqueeze(Wei_shape_res, axis=0).repeat(Sample_num, 1, 1))  #
        theta = torch.max(theta, self.real_min.cuda())
        return torch.mean(theta, dim=0, keepdim=False)

    def inner_product(self, x, dropout=0.):
        # default dropout = 0
        # x = F.dropout(x, dropout, training=self.training)
        x_t = x.permute(1, 0)
        x = x @ x_t
        return x

    def rho_decoder(self, x):
        re_adj = self.inner_product(x)
        re_adj = torch.sigmoid(re_adj)
        return re_adj

    def compute_loss(self, x, re_x):
        likelihood = torch.sum(x * utils.log_max(re_x) - re_x - torch.lgamma(x + 1.))
        return - likelihood / x.shape[1]

    def KL_GamWei(self, Gam_shape, Gam_scale, Wei_shape_res, Wei_scale):
        eulergamma = torch.tensor(0.5772, dtype=torch.float32)
        part1 = Gam_shape * utils.log_max(Wei_scale) - eulergamma.cuda() * Gam_shape * Wei_shape_res + utils.log_max(Wei_shape_res)
        part2 = - Gam_scale * Wei_scale * torch.exp(torch.lgamma(1 + Wei_shape_res))
        part3 = eulergamma.cuda() + 1 + Gam_shape * utils.log_max(Gam_scale) - torch.lgamma(Gam_shape)
        KL = part1 + part2 + part3
        return - torch.sum(KL) / Wei_scale.shape[1]

    @property
    def bottom_word_embeddings(self):
        return self.rho[0]

    @property
    def topic_embeddings_list(self):
        return [item.rho for item in self.topic_embedding][1:][::-1]

    def get_phis(self):
        phis = [0] * self.num_layers
        for t in range(self.num_layers - 1, -1, -1):
            if t == 0:
                phi = torch.mm(self.topic_embedding[t](), torch.transpose(self.topic_embedding[t + 1](), 0, 1))
            else:
                phi = torch.mm(self.topic_embedding[t]().detach(), torch.transpose(self.topic_embedding[t + 1](), 0, 1))

            phis[t] = torch.softmax(phi, dim=0)

        return phis

    def get_phi_list(self):
        phis = self.get_phis()
        return [item.T for item in phis[1:][::-1]]

    def get_theta(self, x):
        hidden_list = [0] * self.num_layers
        theta = [0] * self.num_layers
        k_rec = [0] * self.num_layers
        l = [0] * self.num_layers
        l_tmp = [0] * self.num_layers
        phi_theta = [0] * self.num_layers

        for t in range(self.num_layers):
            if t == 0:
                hidden = F.relu(self.bn_layer[t](self.h_encoder[t](x)))
            else:
                hidden = F.relu(self.bn_layer[t](self.h_encoder[t](hidden_list[t - 1])))

            hidden_list[t] = hidden

        phis = self.get_phis()
        for t in range(self.num_layers - 1, -1, -1):
            if t == self.num_layers - 1:
                hidden_phitheta = hidden_list[t]
            else:
                hidden_phitheta = torch.cat((hidden_list[t], phi_theta[t + 1].permute(1, 0)), 1)
            k_rec_temp = torch.max(torch.nn.functional.softplus(self.shape_encoder[t](hidden_phitheta)), self.real_min.cuda())  # k_rec = 1/k
            k_rec[t] = torch.min(k_rec_temp, self.wei_shape_max.cuda())
            l_tmp[t] = torch.max(torch.nn.functional.softplus(self.scale_encoder[t](hidden_phitheta)), self.real_min.cuda())
            l[t] = l_tmp[t] / torch.exp(torch.lgamma(1 + k_rec[t]))
            theta[t] = self.reparameterize(k_rec[t].permute(1, 0), l[t].permute(1, 0))

            # if t == 0:
            #     phi = torch.mm(self.topic_embedding[t](), torch.transpose(self.topic_embedding[t + 1](), 0, 1))
            # else:
            #     phi = torch.mm(self.topic_embedding[t]().detach(), torch.transpose(self.topic_embedding[t + 1](), 0, 1))

            # phi = torch.softmax(phi, dim=0)

            phi_theta[t] = torch.mm(phis[t], theta[t].view(-1, theta[t].size(-1)))

        if self.training:
            return phi_theta, theta, k_rec, l
        else:
            return [item.T for item in theta[::-1]]

    def get_beta(self):
        beta_list = [0] * self.num_layers

        for t in range(self.num_layers):
            if t == 0:
                self.rho[t] = self.topic_embedding[t]()
            else:
                self.rho[t] = self.rho_graph_encoder[t - 1](self.rho[t - 1].detach(), self.edge_index[t - 1])

            beta_list[t] = torch.softmax(torch.mm(self.rho[t],  torch.transpose(self.topic_embedding[t + 1](), 0, 1)), dim=0)

        return [item.T for item in beta_list[::-1]]

    def forward(self, x):
        phi_theta, theta, k_rec, l = self.get_theta(x[0])
        coef = 10

        rec_x = [0] * self.num_layers
        loss = [0] * self.num_layers
        likelihood = [0] * self.num_layers
        KL = [0] * self.num_layers
        graph_lh = [0] * self.num_layers
        ones_tensor = torch.tensor(1.0, dtype=torch.float32).cuda()

        phi_alpha = [0] * self.num_layers

        for t in range(self.num_layers):
            if t == 0:
                self.rho[t] = self.topic_embedding[t]()
            else:
                self.rho[t] = self.rho_graph_encoder[t - 1](self.rho[t - 1].detach(), self.edge_index[t - 1])

            phi_alpha[t] = torch.softmax(torch.mm(self.rho[t],  torch.transpose(self.topic_embedding[t + 1](), 0, 1)), dim=0)
            rec_x[t] = torch.mm(phi_alpha[t], theta[t].view(-1, theta[t].size(-1)))

        for t in range(self.num_layers):
            if t == self.num_layers - 1:
                KL[t] = self.KL_GamWei(ones_tensor, ones_tensor, k_rec[t].permute(1, 0), l[t].permute(1, 0))
            else:
                KL[t] = self.KL_GamWei(phi_theta[t + 1], ones_tensor, k_rec[t].permute(1, 0), l[t].permute(1, 0))

            likelihood[t] = self.compute_loss(x[t].permute(1, 0), rec_x[t])
            re_adj = self.rho_decoder(self.rho[t])

            if t == 0:
                graph_lh[0] = torch.tensor(0.).cuda()
            else:
                graph_lh[t] = F.binary_cross_entropy(re_adj.view(-1), self.adj[t - 1].view(-1), weight=self.pos_weight[t - 1])

            if self.args.model.pc:
                loss[t] = coef * (1 - 0.2 * t) * likelihood[t] + KL[t] + 0.005 * graph_lh[t] # 1000 * torch.relu(likelihood[0] - 200)  + KL[0]

        loss = sum(loss)
        # return loss, likelihood, KL, graph_lh
        return {'loss': loss}
