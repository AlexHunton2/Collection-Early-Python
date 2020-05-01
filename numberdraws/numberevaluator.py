import torch, torchvision, os, cv2
import numpy as np 
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim


#defining datasets
train = datasets.MNIST("", train=True, download=True, transform = transforms.Compose([transforms.ToTensor()]))

test = datasets.MNIST("", train=False, download=True, transform = transforms.Compose([transforms.ToTensor()]))

trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=True)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        #sets up layers
        self.fc1 = nn.Linear(784, 64) # inputs to hidden
        self.fc2 = nn.Linear(64, 64) #hidden to hidden
        self.fc3 = nn.Linear(64, 64) #hidden to hidden
        self.fc4 = nn.Linear(64, 10) #hidden to output
    def forward(self, x):
        #F.relu = activation function
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        #dont need retuifiy linear on output layer
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)

net = Net()

trained = True

if not trained:
  #training time.
  optimizer = optim.Adam(net.parameters(), lr=0.001) # declares optimizer, uses the "Adam" optimizer cause its typical
  #EPOCHS amount of times the training passes through entire data. IE Epoch = 1, goes through data a singular time. Epoch = 3, goes through data 3 times.
  EPOCHS = 1500
  for epoch in range(EPOCHS):
      for data in trainset:
          #data is a batch of featuresets and labels
          X, y = data # X is the batch of features, y is the batch of targets
          net.zero_grad() # sets graidents to 0 before loss calc. You will do this likely ever step
          output = net(X.view(-1, 28*28)) #pass in the reshaped batch
          loss = F.nll_loss(output, y) #calc and grab the loss value
          loss.backward() #apply this loss backwards thru the network's parameters
          optimizer.step() # attempt to optimize weight to account for loss/gradients
      print(loss)
  torch.save(net.state_dict(), "misc/misc")

class numbertonumbers():
    IMG_SIZE = 28
    IMGS = "numberdraws\imgs"
    data = []
    
    def convertData(self):
        self.data = []
        for i in os.listdir(self.IMGS):
            try:
                path = os.path.join(self.IMGS, i) #path = the path of a specfic image
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) #greyscales image so less complicated
                img = cv2.resize(img, (self.IMG_SIZE, self.IMG_SIZE)) #resizes the image
                img = cv2.bitwise_not(img)
                self.data.append([np.array(img)])
            except Exception as e:
                pass
    def getData(self):
      return self.data

#load training data
def loaddata():
    neural = Net()
    neural.load_state_dict(torch.load("numberdraws\E-150"))

    number = numbertonumbers()
    number.convertData()
    data = number.getData()

    tensorData = torch.Tensor([i[0] for i in data]).view(-1, 28, 28)
    tensorData = tensorData/225
    #print(torch.argmax(neural(tensorData[9].view(-1,784))[0]))
    #plt.imshow(tensorData[0].view(28, 28))
    #plt.show()
    
    return torch.argmax(neural(tensorData[0].view(-1,784))[0])