# Python Pong

This is an implementation of a machine learning algorithm applied to the game of pong. As this was a learning project for me, I did not write the pong game myself, but have used the source from the tutorial that I was following, as my main aims were to implement the machine learning program. 

## About NEAT-python

The NEAT machine learning package for python is one of the most interesting machine learning ideas that I have come across, and it has been very enjoyable to learn more about it, and I encourage anyone to have a look at their [website ](https://neat-python.readthedocs.io/en/latest/neat_overview.html). 

The main feature of the program that I found most interesting was the usage of genome theory from biology, and selective breading. The program uses selective breading to select the best genes (in this case the best pong players) and bread them with each other in the next generation of pong players. 

I have kept the defaults of the tutorial that I was following, apart from adding in an extra input to the neural network. The inputs that I have used to train the AI are: y position of the AI paddle, distance to the ball, ball speed, and the ball y position. This then returns that output of whether the AI should move the paddle up, down, or not move it. 

## How to run 

The progam should be able to run on any machine after installing the required packages found in requirements.txt. There are comments in the code, but the main parts that can be changed are the last 2 function calls. The first is commented out, and this runs the learning stage of the program, and the last line is the line that enables the user to play against the best pong player in the set. 

I have tried to add to the comments 