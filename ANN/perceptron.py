
# Please give credit when used

import pandas as pd


class PerceptronLearning():
	# initialize weights, learning rate(alpha) and threshold(thita)
	def __init__(self):
		self.w1 = 0.3
		self.w2 = -0.1
		self.alpha = 0.1
		self.thita = 0.2

	def get_activation(self, net_input): # unit step activation
		if net_input < 0:
			return 0
		else:
			return 1

	def update_weight(self, input_sequence, target, error):
		self.w1 += self.alpha*input_sequence[0]*error
		self.w2 += self.alpha*input_sequence[1]*error

	def net_input(self, input_sequence):
		return self.w1*input_sequence[0] + self.w2*input_sequence[1] - self.thita

	def error(self, actual, target):
		return target - actual

	def read_dataset(self):
		dataset = pd.read_csv('perceptron_and.csv')
		X = dataset.iloc[:, [0,1]].values
		y = dataset.iloc[:, 2].values
		return X,y


pl = PerceptronLearning()
print("During Training Perceptron Neural Network")
while True:
	error_list = []
	X,y = pl.read_dataset()
	# weight training
	for x,y in zip(X,y):
		net_input = pl.net_input(x)
		output = pl.get_activation(net_input) # output is actual output
		error = pl.error(output, y) # y is target output
		pl.update_weight(x, y, error)
		error_list.append(error)
		print("input_sequence: {} => actual_output: {}; expected_output: {}".format(x, output, y))

	error_list = list(dict.fromkeys(error_list)) # first convert list into dictionary which removes duplicates beacause, dictionary have unique keys and then convert it back to list
	# print(error_list)
	if error_list == [0]: # break while loop when error is 0 for all input sequence
		break

# testing
print("\nAfter Training Perceptron Neural Network")
for x in X:
	net_input = pl.net_input(x)
	output = pl.get_activation(net_input)
	print("input_sequence: {} => output: {}".format(x, output))
