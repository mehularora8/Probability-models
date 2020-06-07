'''
Naive Bayes Classifier
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

class NaiveBayes:
    '''
    Naive Bayes Classifier

    For a datapoint, the Naive Bayes classifier computes the probability of each label,
    and then it predicts the label with the highest probability. During training,
    it learns probabilities by counting the occurences of feature/label combinations
    that it finds in the training data. During prediction, it uses these counts to
    compute probabilities.
    '''

    def __init__(self, use_mle):
        '''DO NOT RENAME INSTANCE VARIABLES'''
        self.label_counts = {}
        self.feature_counts = {}
        self.use_mle = use_mle # True for MLE, False for MAP with Laplace add-one smoothing

    def fit(self, train_features, train_labels):
        self.label_counts[0] = 0
        self.label_counts[1] = 0

        # Set label counts
        self.label_counts[0] = np.count_nonzero(train_labels == 0)
        self.label_counts[1] = np.count_nonzero(train_labels == 1)

        for i in range(train_features.shape[1]): #d columns
            data = train_features[:, [i]]

            ft = 0 #ft = false-true, instances where the data label is a 1 and feature is a 0
            tf = 0 #ft = true-false, instances where the data label is a 0 and feature is a 1
            tt = 0 #ft = true-true, instances where the data label is a 1 and feature is a 1
            ff = 0 #ff = false-false, instances where the data label is a 0 and feature is a 0

            for j in range(train_features.shape[0]): #n rows
                if data[j] == 0 and train_labels[j] == 1:
                    ft += 1
                elif data[j] == 1 and train_labels[j] == 0:
                    tf += 1
                elif data[j] == 1 and train_labels[j] == 1:
                    tt += 1
                elif data[j] == 0 and train_labels[j] == 0:
                    ff += 1

            if ft != 0 : self.feature_counts[(i, 0, 1)] = ft
            if tf != 0 : self.feature_counts[(i, 1, 0)] = tf
            if tt != 0 : self.feature_counts[(i, 1, 1)] = tt
            if ff != 0 : self.feature_counts[(i, 0, 0)] = ff

    def predict(self, test_features):
        preds = np.zeros(test_features.shape[0], dtype=np.uint8)

        total_labels = self.label_counts[0] + self.label_counts[1]

        for i in range(test_features.shape[0]): #n rows

            p0 = self.label_counts[0] / total_labels #Start with probability of (Y = 0)
            p1 = self.label_counts[1] / total_labels #Start with probability of (Y = 1)

            if self.use_mle:

                for j in range(test_features.shape[1]):
                    
                    p0 *= self.feature_counts.get((j, test_features[i][j], 0) , 0) / self.label_counts[0]
                    p1 *= (self.feature_counts.get((j, test_features[i][j], 1), 0)) / self.label_counts[1]
            else:

                for j in range(test_features.shape[1]):
                    
                    p0 *= (self.feature_counts.get((j, test_features[i][j], 0), 0) + 1) / (self.label_counts[0] + 2)
                    p1 *= (self.feature_counts.get((j, test_features[i][j], 1), 0) + 1) / (self.label_counts[1] + 2)


            if p0 > p1 : preds[i] = 0
            else : preds[i] = 1

        return preds
