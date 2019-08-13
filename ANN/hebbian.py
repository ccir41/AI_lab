# Please give credit when used

import numpy as np
import pandas as pd


# import data set
dataset = pd.read_csv('hebb_and.csv')
X = dataset.iloc[:, [0,1,2]].values # input sequence
# print(X)

y = dataset.iloc[:, 3].values # target output
# print(y)


class HebbLearning():
	# initialize weight and bias to 0
	def __init__(self):
		self.w1 = 0
		self.w2 = 0
		self.b = 0

	def get_activation(self, net_input): # unit step activation
			if net_input < 0:
				return 0
			else:
				return 1

	def update_weight_bias(self, input_sequence, target):
		self.w1 += input_sequence[0]*target
		self.w2 += input_sequence[1]*target 
		self.b += target
		return self.w1, self.w2, self.b

	def net_input(self, input_sequence):
		return self.b + self.w1*input_sequence[0] + self.w2*input_sequence[1]


hl = HebbLearning()

# weight training
for x,y in zip(X,y):
	w1,w2,b = hl.update_weight_bias(x, y)
	print("Bias: {}\nWeight1: {}\nWeight2: {}\n".format(b,w1,w2))

# testing 
for x in X:
	net_input = hl.net_input(x)
	output = hl.get_activation(net_input)
	print(output)
