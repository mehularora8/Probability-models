'''
Logistic Regression Classifier
'''
import math
import numpy as np

"""
Starter Code for CS 109 Problem Set 6
Written by Tim Gianitsos
Comments by Alex Tsun and Anand Shankar

*************************IMPORTANT*************************
Do NOT modify the name of any functions. Do not add or remove
parameters to them either. Moreover, make sure your return
value is exactly as described in the PDF handout and in the
provided function comments. Remember that your code is being
autograded. You are free to write helper functions if you so
desire but they are not necessary. Do NOT rename this file.
Do NOT modify any code outside the begin and end code markers.
*************************IMPORTANT*************************
"""

def sigmoid(vec):
    '''
    Parameters:

    `vec`: a numpy array or scalar
    ================================
    Returns the sigmoid function applied to each element of `vec`.
    '''
    return 1 / (1 + np.exp(-vec))

class LogisticRegression:
    '''
    Logistic Regression Classifier

    For a datapoint, the Logistic Regression classifier computes the probability of each label,
    and then it predicts the label with the highest probability. During training, it learns
    weights for each feature using gradient ascent. During prediction, it uses the test data
    to apply a linear transformation to the weights.
    '''

    def __init__(self, learning_rate, max_steps):
        '''DO NOT RENAME INSTANCE VARIABLES'''
        self.learning_rate = learning_rate
        self.max_steps = max_steps
        self.weights = None

    def fit(self, train_features, train_labels):
        # This line inserts a column of ones before the first column of train_features,
        # resulting in the an `n x (d + 1)` size matrix, This is so we
        # don't need to have a special case for the bias weight.
        train_features = np.insert(train_features, 0, 1, axis=1)

        # This makes the matrix immutable
        train_features.setflags(write=False)

        # This is the theta you will be performing gradient ascent on. It has
        # shape (d + 1).
        theta = np.zeros(train_features.shape[1])

        num_features = train_features.shape[1]

        # Loop over max steps for gradient ascent
        for i in range(self.max_steps):
            # Initialize gradient at each step to 0s
            gradient = np.zeros(num_features)

            # For each training sample
            for j in range(train_features.shape[0]):
                pred = train_labels[j] - sigmoid(np.dot(theta, train_features[j]))
                for k in range(num_features):
                    gradient[k] +=  pred * train_features[j][k]


            # Update weights
            for k in range(num_features):
                theta[k] += self.learning_rate * gradient[k]

            if i % 100 == 0:
                print("Iteration {} complete".format(i))


        self.weights = theta

    def predict(self, test_features):
        test_features = np.insert(test_features, 0, 1, axis=1) # add bias term
        test_features.setflags(write=False) # make immutable
        preds = np.zeros(test_features.shape[0])

        for i in range(test_features.shape[0]):
            if sigmoid(np.matmul(self.weights, test_features[i])) >= 0.5: preds[i] = 1
            else: preds[i] = 0

        return preds
