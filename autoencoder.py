# -*- coding: utf-8 -*-
"""Autoencoder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XJIKaMRUjl5clbGN0lMGqERt3PvZ5bkb
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

import torchvision
import torchvision.transforms as transforms 

import os
import sys

# Hyperparameters
batch_size = 128
num_epochs = 10

# Data prep
transform = transforms.Compose([transforms.ToTensor()])

train_set = torchvision.datasets.MNIST(root=os.getcwd(), train=True, transform=transform, download=True)
train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)

test_set = torchvision.datasets.MNIST(root=os.getcwd(), train=False, transform=transform, download=True)
test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=True)

# Model
class AutoEncoder(nn.Module):
  
  def __init__(self):
    super().__init__()
    self.encoder = nn.Sequential(nn.Linear(784, 128),
                                #  nn.L1Loss(),
                                 nn.ReLU(inplace=True),
                                 nn.Linear(128, 64),
                                 nn.ReLU(inplace=True),
                                 nn.Linear(64, 16))
                                #  nn.ReLU(inplace=True),
                                #  nn.Linear(16, 2))
    
    # self.hidden = nn.Sequential()

    self.decoder = nn.Sequential(nn.Linear(16, 64),
                                 nn.ReLU(inplace=True),
                                 nn.Linear(64, 128),
                                 nn.ReLU(inplace=True),
                                 nn.Linear(128, 784),
                                 nn.Sigmoid())

  def forward(self, x):
    x = self.encoder(x)
    x = self.decoder(x)
    return x

device =  'cuda' if torch.cuda.is_available() else 'cpu'
model = AutoEncoder().to(device)

optimizer = optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.MSELoss()

for epoch in range(num_epochs):

  running_loss = []
  running_acc = []
  n_samples = 0
  n_correct = 0

  for batch_idx, (data, _) in enumerate(train_loader):

    data = data.squeeze().reshape(-1, 784).to(device)

    # Forward
    outputs = model(data)
    loss = criterion(outputs, data)

    # BackWard
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    running_loss.append(loss.item())

    if batch_idx % batch_size == 0: 
      print(f"Epoch:{epoch+1}\t\tBatch Step:{batch_idx+1}/{len(train_loader)}\t\tLoss:{sum(running_loss)/len(running_loss):.4f}")

  print('================================================================')

# Visualization
from matplotlib import pyplot as plt
import numpy as np

def show(img):
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1,2,0)), interpolation='nearest')

sample_data, _ = next(iter(test_loader)) 

output = model((sample_data.squeeze().reshape(-1, 784)).to(device))
output = output.unsqueeze(1).reshape(-1, 1, 28, 28).detach().cpu()

fig = plt.figure(figsize=[20, 20])
plt.subplot(2,2,1)
show(torchvision.utils.make_grid(sample_data[:32]))
plt.subplot(2,2,2)
show(torchvision.utils.make_grid(output[:32]))
plt.show()