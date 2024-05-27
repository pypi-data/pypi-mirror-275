import torch
from torchvision import datasets


class Dataset(torch.utils.data.Dataset):
    def __init__(self, path, one_hot=False, transform=None):
        self.data_set = datasets.ImageFolder(path, transform=transform)
        self.x, self.y = zip(*self.data_set)
        if one_hot:
            self.y = torch.nn.functional.one_hot(torch.tensor(self.y)).float()

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return len(self.x)

    @property
    def classes(self):
        return self.data_set.classes

    @property
    def class_to_idx(self):
        return self.data_set.class_to_idx
