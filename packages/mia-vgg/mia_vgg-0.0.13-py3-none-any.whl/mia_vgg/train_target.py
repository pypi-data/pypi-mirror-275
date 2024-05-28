"""In this module we use pytorch to train vgg16 on celebA."""

from torchvision import datasets, models
import matplotlib.pyplot as plt
from torch import nn
from torch.utils.data import random_split, DataLoader
import torch.optim as optim
from torchvision.transforms import PILToTensor, v2
import torch
import numpy as np
import os
from pathlib import Path
import pickle
from tqdm import tqdm


def trgtsf(t):
    """Transform a target.
    :param t: Target vector.
    :type t: Vector of size 40
    """
    return t[8]

def train():
    """Train VGG16. Evaluate on 20% unseen data. Create a mia dataset of loss with member and non-member labeled."""
    transform = v2.Compose([PILToTensor(),
                           v2.ToDtype(torch.float32, scale=True)])
    celeba = datasets.CelebA(root="data", download=True, target_transform=trgtsf, transform=transform)
    x = celeba[0][0]

    train, test = random_split(celeba, [0.8,0.2])
    trainloader = DataLoader(train, batch_size=100)
    testloader = DataLoader(test, batch_size=100)

    weights = models.VGG16_Weights
    model = models.vgg16(weights=weights)

    num_ftrs = model.classifier[len(model.classifier)-1].in_features

    model.classifier[len(model.classifier)-1] = nn.Linear(num_ftrs, 2)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    epochs = 1
    for epoch in range(epochs):
        running_loss = 0
        for i,data in enumerate(trainloader):
            optimizer.zero_grad()
            x,y = data
            x = x.to(device)
            y = y.to(device)
            soft = model(x)
            loss = criterion(soft, y)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i%1==0:
                print(f"epoch : {epoch}, batch : {i}/{len(trainloader)} - loss: {running_loss/100:.3f}")
                running_loss = 0

            if i>50:
                break

    #Save trained model

    mia_size = 1000
    mia = {"loss":np.zeros(mia_size).astype(float),
           "soft":np.zeros([mia_size,2]).astype(float),
           "y":np.zeros(mia_size),
           "member":np.zeros(mia_size),
           }
    half = int(mia_size/2)
    mia["member"][:half] = 1
    index = 0
    #Compute loss 
    criterion = nn.CrossEntropyLoss(reduction='none')
    with torch.no_grad():
        for i, data in enumerate(trainloader):
            x,y = data
            x = x.to(device)
            soft = model(x).cpu().detach().numpy()
            loss = criterion(soft, y)
            for j in range(len(loss)):
                if index > half-1:
                    break
                else:
                    mia["loss"][index] = loss[j]
                    mia["soft"][index] = soft[j]
                    mia["y"][index] = y[j]
                index += 1
                

    with torch.no_grad():
        values = {"y":np.empty(0), "yhat":np.empty(0)}
        for i, data in enumerate(testloader):
            x,y = data
            x = x.to(device)
            soft = model(x).cpu().detach().numpy()
            _, yhat = torch.max(soft, 1)
            loss = criterion(soft, y)
            values["y"] = np.append(values["y"], y)
            values["yhat"] = np.append(values["yhat"], yhat)

            for j in range(len(loss)):
                index += 1
                if index > mia_size-1:
                    break
                else:
                    mia["loss"][index] = loss[j]
                    mia["soft"][index] = soft[j]
                    mia["y"][index] = y[j]


        y = values["y"]
        yhat = values["yhat"]
    metric["accuracy"] = np.mean(y==yhat)
    metric["balanced_accuracy"] = np.mean([np.mean(yhat[y==yy]==yy) for yy in np.unique(y)])

    path = Path("result")
    os.makedirs(path, exist_ok=True)
    with open(Path(path, "metric.pickle"), 'wb') as f:
        pickle.dump(metric, f)
    with open(Path(path, "values.pickle"), 'wb') as f:
        pickle.dump(values, f)

        
if __name__=="__main__":
    train()
