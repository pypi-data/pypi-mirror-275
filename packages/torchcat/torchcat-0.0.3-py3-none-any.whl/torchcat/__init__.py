import numpy as np
from torchsummary import summary


class Cat:
    def __init__(self, model, loss_fn=None, optimizer=None):
        # 训练日志、模型、损失函数、优化器、GPU 标志
        self.model = model
        self.loss_fn = loss_fn
        self.optimizer = optimizer
        self.GPU_FLAG = str(next(model[0].parameters()).device)
        self.log = {'train loss': [], 'train acc': [], 'valid loss': [], 'valid acc': []}

        if (loss_fn and optimizer) is None:
            print('未检测到损失函数或优化器，这将会影响到你的模型训练🙂')

    # 训练
    def train(self, train_set, epochs):
        self.model.train()
        for epoch in range(1, epochs+1):
            loss_temp = []  # 储存一个批次内的损失值
            for x, y in train_set:
                self.optimizer.zero_grad()
                pred = self.model(x)
                loss = self.loss_fn(pred, y)
                loss_temp.append(loss.item())
                loss.backward()
                self.optimizer.step()
            loss_mean = np.mean(loss_temp)
            # 记录、输出训练日志
            self.log['train loss'].append(loss_mean)
            print(f'Epoch {epoch}/{epochs} Loss: {loss_mean:.6f}')

    # 验证
    def valid(self, valid_set):
        self.model.eval()
        acc_temp = []       # 储存一个批次内的准确率、损失值
        loss_temp = []
        for x, y in valid_set:
            pred = self.model(x)
            loss_temp.append(self.loss_fn(pred, y).item())  # 计算验证集 loss
            acc_temp.append(np.mean(pred.detach().numpy().argmax(-1) == y))  # 计算验证集 accuracy
        print(f'Loss: {np.mean(loss_temp):.6f}')
        print(f'Accuracy: {np.mean(acc_temp):.6f}')

    # 查看架构
    def summary(self, input_size):
        # 判断GPU是否可用
        if self.GPU_FLAG == 'cpu':
            device = 'cpu'
        else:
            device = 'cuda'
        summary(self.model, input_size, device=device)

    def train(self):
        self.model.train()

    def eval(self):
        self.model.eval()

    def __call__(self, x):
        return self.model(x)
