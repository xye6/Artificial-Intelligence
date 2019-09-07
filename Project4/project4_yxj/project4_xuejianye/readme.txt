Readme

Individual work

dt.py and nn.py is done with python3.

for those python files:

1) Run them in terminal

2) Type parameters by using command line to train the model. There are several major parameters you can use to train the model:

For dt.py:
   ‘-d’: type the file path of the dataset which you want to use to train the model(please use my data files, which including header)

For nn.py python:
   ‘-a’: type a number to indicate your expected learning rate;
   ‘-d’: type the file path of the dataset which you want to use to train the model;
   ‘-e’: type a number to indicate your expected epoch number;
   ‘-c’: type a number to indicate your expected number k for cross validation
   ‘-hl’: type numbers connected by ‘-‘ to indicate your expected hidden layer structure. 
          for example, type ‘7’ means you only want to have one hidden layer with 7 nodes;
	type ‘8-6’ means you want to have two hidden layers with 8 and 6 nodes respectively;
	type ‘0’ means you don’t want to have hidden layers

   ‘-w’: if you want to use pre-trained model, type the path of the file containing pre-trained model’s weights (if you want to use pre-trained model, remember to change the structure of hidden layers, the weights file’s name will tell you the structure of hidden layers)


example for command line: 

python3 nn.py -d iris.discrete.txt -w iris_weights_7.txt

Python3 nn.py -d car_evaluation.txt -w car_weights_8-6.txt -hl 8-6

python3 nn.py -d car_evaluation.txt -c 3 -hl 8-6 (it will spend long time on running)

python3 dt.py -d restaurant.txt

python3 dt.py -d iris.txt

you can learn more by using ‘—help’ command after the .py file (also to see the default)

3) Now you have gotten trained model, follow the instruction to predict! Type test data with comma or blank as separator. For example, type ’S,ML,S,S’ as the test data to model which has been trained on Iris data.


