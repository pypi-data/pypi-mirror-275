import numpy as np
from torchsummary import summary


class Cat:
    def __init__(self, model, loss_fn=None, optimizer=None):
        '''
        封装模型

        Parameters
        --------
        model: 模型
        loss_fn: 损失函数
        optimizer: 优化器
        '''
        # 训练日志、模型、损失函数、优化器、GPU 标志
        self.model = model
        self.loss_fn = loss_fn
        self.optimizer = optimizer
        self.GPU_FLAG = str(next(model.parameters()).device)
        self.log = {'train loss': [], 'train acc': [], 'valid loss': [], 'valid acc': []}

        if (loss_fn and optimizer) is None:
            print('未检测到损失函数或优化器，这将会影响到你的模型训练🙂')

    def train(self, train_set, epochs, valid_set=None):
        '''
        训练模型

        Parameters
        --------
        train_set: 训练集
        epochs: 训练轮数
        valid_set: 验证集

        Returns
        --------
        log: 训练日志
        '''
        self.model.train()
        for epoch in range(1, epochs+1):
            acc_temp = []       # 储存一个 epoch 的准确率、损失值
            loss_temp = []
            for x, y in train_set:
                if self.GPU_FLAG != 'cpu':
                    x, y = x.cuda(), y.cuda()
                self.optimizer.zero_grad()
                pred = self.model(x)
                loss = self.loss_fn(pred, y)
                loss_temp.append(loss.item())
                loss.backward()
                self.optimizer.step()

                acc_temp.append((pred.argmax(-1) == y).float().mean().item())

            train_acc, train_loss = np.mean(acc_temp), np.mean(loss_temp)
            # 记录、输出训练日志
            self.log['train acc'].append(train_acc)
            self.log['train loss'].append(train_loss)

            output = f'Epoch {epoch}/{epochs} Train-Loss: {train_loss:.6f} Train-Accuracy: {train_acc:.6f}'
            if valid_set is not None:
                valid_loss, valid_acc = self.valid(valid_set, show=False, train=True)
                self.log['valid acc'].append(valid_acc)
                self.log['valid loss'].append(valid_loss)
                output += f' Valid-Loss: {valid_loss:.6f} Valid-Accuracy: {valid_acc:.6f}'

            print(output)
        return self.log

    def valid(self, valid_set, show=True, train=False):
        '''
        验证模型

        Parameters
        --------
        valid_set : 验证集
        show : 是否输出损失值、准确率
        train : 最后是否切换为训练模式

        Returns
        --------
        loss, acc : 验证集上的的损失值、准确率
        '''
        self.model.eval()
        acc_temp = []       # 储存一个 epoch 的准确率、损失值
        loss_temp = []
        for x, y in valid_set:
            if self.GPU_FLAG != 'cpu':
                x, y = x.cuda(), y.cuda()
            pred = self.model(x)
            loss_temp.append(self.loss_fn(pred, y).item())  # 计算验证集 loss
            acc_temp.append((pred.argmax(-1) == y).float().mean().item())  # 计算验证集 accuracy
        if train:
            self.model.train()
        if show:
            print(f'Loss: {np.mean(loss_temp):.6f}')
            print(f'Accuracy: {np.mean(acc_temp):.6f}')
        return np.mean(loss_temp), np.mean(acc_temp)

    def summary(self, *input_size):
        '''
        查看架构

        Parameters
        --------
        input_size : 模型输入的形状
        '''
        # 判断GPU是否可用
        if self.GPU_FLAG != 'cpu':
            device = 'cuda'
        else:
            device = 'cpu'
        summary(self.model, input_size, device=device)

    def clear_log(self):
        '''清空训练日志'''
        self.log = {'train loss': [], 'train acc': [], 'valid loss': [], 'valid acc': []}

    @property
    def training(self):
        '''查看模型是否处于训练模式'''
        return self.model.training

    def to_train(self):
        '''切换到训练模式'''
        self.model.train()

    def to_eval(self):
        '''切换到推理模式'''
        self.model.eval()

    def to_cpu(self):
        '''切换到 CPU'''
        self.model.cpu()

    def to_cuda(self):
        '''切换到 GPU'''
        self.model.cuda()

    def __call__(self, x):
        '''模型推理'''
        return self.model(x)
