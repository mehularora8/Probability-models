'''
Additional classifier questions
'''
import math
import numpy as np

"""
Starter Code for CS 109 Problem Set 6
Written by Tim Gianitsos
Spec by Lisa Yan

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

#############################################
########### Naive Bayes Questions ###########
#############################################

def question_nb_a(clf, train_features, train_labels):
    # This fits the model to the training data. Ensure your implementation for 
    # `NaiveBayes.fit()` is correct!
    clf.fit(train_features, train_labels)

    epsilon = 1e-8 # prevents division by zero in case fit() is not implemented
    res = clf.label_counts[1] / ((clf.label_counts[0] + clf.label_counts[1]) or epsilon)
    return res

def question_nb_b(clf, train_features, train_labels):
    clf.fit(train_features, train_labels)
    res = np.zeros(train_features.shape[1])

    zero_count = clf.label_counts[0]

    for i in range(train_features.shape[1]):
        res[i] = (clf.feature_counts.get((i, 1, 0), 0) / zero_count)

    return res

def question_nb_c(clf, train_features, train_labels):
    clf.fit(train_features, train_labels)
    res = np.zeros(train_features.shape[1])

    one_count = clf.label_counts[1]

    for i in range(train_features.shape[1]):
        res[i] = (clf.feature_counts.get((i, 1, 1), 0)/ one_count)

    return res

def question_nb_d(clf, train_features, train_labels):
    clf.fit(train_features, train_labels)
    res = np.zeros(5)

    l = [] # List of tuples, (index, ratio)

    for i in range(train_features.shape[1]):
        prob_x_is_zero = (clf.feature_counts.get((i, 0, 1), 0) + clf.feature_counts.get((i, 0, 0), 0)) / train_features.shape[1]
        prob_x_is_one = 1 - prob_x_is_zero

        zero_count = clf.label_counts[0]
        one_count = clf.label_counts[1]

        prob_x_one_y_one = clf.feature_counts.get((i, 1, 1), 0)/ one_count
        prob_x_zero_y_one = clf.feature_counts.get((i, 1, 0), 0) / zero_count

        ratio = (prob_x_one_y_one * prob_x_is_zero) / (prob_x_zero_y_one * prob_x_is_one)

        l.append((i, ratio))

    l.sort(key = lambda x: x[1])

    for j in range(5):
        res[j] = l[j][0]

    res.sort()
    print(res)
    return res

#############################################
####### Logistic Regression Questions #######
#############################################

def question_lr_a(clf, train_features, train_labels):
    clf.fit(train_features, train_labels)
    res = np.zeros(5)

    ### YOUR CODE HERE

    ### END YOUR CODE

    return res

def question_lr_b(clf, train_features, train_labels, test_features, test_labels):
    clf.fit(train_features, train_labels)
    res = 0.0

    # Method to calculate precision

    preds = clf.predict(test_features)
    true = 0
    total = 0
    for i in range(len(test_labels)):
        if test_labels[i] == 1 and preds[i] == 1:
            true += 1
            
        if preds[i] == 1:
            total += 1

    res = true / total
    return res

def question_lr_c(clf, train_features, train_labels, test_features, test_labels):
    clf.fit(train_features, train_labels)
    res = 0.0

    preds = clf.predict(test_features)
    true = 0
    total = 0
    for i in range(len(test_labels)):
        if test_labels[i] == 1 and preds[i] == 1:
            true += 1
        elif test_labels[i] == 1 and preds[i] == 0:
            total += 1

    res = true / (true + total)
    print(res)
    return res
