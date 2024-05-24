# TorchCat

# 简介

TorchCat 能够用于简化你的模型训练

# 用法

导入库

```python
from torch import Cat
```

封装你的模型

```python
# 你的模型
net = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28*28, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
)

net = Cat(model=net,
          loss_fn=nn.CrossEntropyLoss(),
          optimizer=torch.optim.Adam(net.parameters(), lr=0.0001))
```

| 参数      | 说明         |
| --------- | ------------ |
| model     | 你的模型     |
| loss_fn   | 选择损失函数 |
| optimizer | 选择优化器   |

## Cat.summary()

在封装模型后，使用 `net.summary()`，可以查看模型的架构。`input_size` 参数需填写模型的输入形状，如 `net.summary(1, 28, 28)`

## Cat.train()

使用 `net.train()`，可以开始模型的训练

 `log`，可以记录训练时的训练日志，包括

- 训练集损失（`log['train loss']`）
- 训练集准确率（`log['train acc']`）
- 验证集损失（`log['valid loss']`）
- 验证集准确率（`log['validacc']`）

```python
log = net.train(train_set=train_set, epochs=5, valid_set=test_set)
```

| 参数      | 说明     |
| --------- | -------- |
| train_set | 训练集   |
| epochs    | 训练轮次 |
| valid_set | 验证集   |
