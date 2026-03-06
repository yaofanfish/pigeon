#!/usr/bin/env python3

print("\033[36mloading modules")
import sys, os

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

import numpy as np
from PIL import Image

import code
print("finished loading modules\033[0m")

# thanks torch website
device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu" # GPU
print(f"Using {device} device")

class PigeonRecogniser(nn.Module):
	def __init__(self):
		super().__init__()
		# self.flatten = nn.Flatten(start_dim=1, end_dim=-1) # flattener # dont need, I'll do it myself
		self.layers = nn.Sequential( # takes a bunch of args, each being a callable that is called in order f1(f2(f3(input))) # docs calls it self.linear_relu_stack
			nn.Linear(in_features=144*256, out_features=4096, bias=True), # takes 144*256 out 1024 **DOES BACKPROP ITSELF, DON'T NEED TO DIY**
			nn.ReLU(), # simple relu
			nn.Linear(in_features=4096, out_features=4096),
			nn.ReLU(),
			nn.Linear(in_features=4096, out_features=1024),
			nn.ReLU(),
			nn.Linear(in_features=1024, out_features=2) # pigeon / pidgeon
		)
		self.loss_fn = nn.MSELoss()
		self.train = torch.optim.SGD(self.parameters(), lr=1e-3) # "optimizer" # backprop, where simple, new value = old value - (first partial deriv * lr)
	def forward(self, img):
		img = loadimg(img)
		logits = self.layers(img)
		return logits # just means the output neurons
	def choochootrain(self):
		model.train() # this is a SWITCH
	def loadimg(self=None, img=None, path=None):
		if not img:
			img = Image.open(path)
		if type(img) != torch.tensor:
			if type(img) == np.ndarray:
				img = torch.tensor(img)
			else:
				img = self.convimg(img)
		return img
	def convimg(self=None, img=None):
		if not img:
			raise Exception("where is my img")
		img = img.resize((144, 256))
		img = img.convert("L")
		img = np.array(img, dtype=np.float64) # doesn't work with torch for some reason
		img /= 255
		img = torch.tensor(img)
		return img

model = PigeonRecogniser().to(device)
print(model)

code.interact(local=dict(globals(), **locals()))

