# -*- coding: utf-8 -*-
"""Sparse Autoencoder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iR759cVgGJA6Bg85AGBwFyNVHUOeRzq5
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader

import torchvision
import torchvision.transforms as transforms 

import seaborn as sns
import numpy as np

import os, sys

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
                                #  nn.ReLU(),
                                 nn.Linear(128, 64),
                                #  nn.ReLU(),
                                 nn.Linear(64, 16)
                                 )
    
    self.decoder = nn.Sequential(nn.Linear(16, 64),
                                #  nn.ReLU(),
                                 nn.Linear(64, 128),
                                #  nn.ReLU(),
                                 nn.Linear(128, 784),
                                #  nn.Sigmoid()
                                 )

  def forward(self, x):
    x = self.encoder(x)
    x = self.decoder(x)
    return x

device =  'cuda' if torch.cuda.is_available() else 'cpu'
model = AutoEncoder().to(device)

def sparse_loss(model, data):
  loss = 0
  values = data
  for i in model.children():
    for j in i: 
      values = F.relu(j(values))
      loss += torch.mean(torch.abs(values))
  return loss

reg_param = 0.001 # tuning parameter for l1 regularization
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
    mse_loss = criterion(outputs, data)
    l1_loss = sparse_loss(model, data)
    loss = mse_loss + l1_loss * reg_param

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
sample_data = sample_data + torch.empty(128, 1, 28, 28).normal_(0.1307, 0.3081)
output = model((sample_data.squeeze().reshape(-1, 784)).to(device))
output = output.unsqueeze(1).reshape(-1, 1, 28, 28).detach().cpu()

fig = plt.figure(figsize=[20, 20])
plt.subplot(2,2,1)
show(torchvision.utils.make_grid(sample_data[:32]))
plt.subplot(2,2,2)

show(torchvision.utils.make_grid(output[:32]))
plt.show()