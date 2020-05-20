# Name:
# Stanford email:

########### CS109 Problem Set 4, Question 10 ##############

# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np
from probabilities import *

"""
Starter Code for CS 109 Problem Set 4

*************************IMPORTANT*************************
The file probabilities contains helper functions 
probStress(), probExposure(), probCold(s, e), probFlu(s, e), 
and probSymptom(i, f, c). You should NOT re-implement these
functions; they are imported for you already.

We may additionally test your code with different values
from what is provided to you.

You can call the functions directly from this file:
  x = probFlu() + 5     # not a probability

*************************IMPORTANT*************************
"""


def inferProbFlu(ntrials = 1000000) -> float:
    """
    This is question 10 part (a).
    
    Computes P(Flu = 1 | Exposure = 1, X_2 = 1), the probability
    of flu conditioned on observing that the patient has had
    exposure to a sick friend and that they are experiencing
    Symptom 2 (runny nose). Uses rejection sampling.
    :param ntrials: the number of observations to sample.

    """

    numPositive = 0
    numSample = 0

    for i in range(ntrials):
    	array = [ 0,  0,  0, 0, 0, 0, 0, 0, 0]
    	#[Stress, Exposure, Cold, Flu, <X_1, X_2, X_3, X_4, X_5>]

    	if np.random.rand() <= 0.5:
    		array[0] = 1
    	else:
    		array[0] = 0

    	if np.random.rand() <= 0.1:
    		array[1] = 1
    	else: 
    		array[1] = 0

    	if np.random.rand() <= probCold(array[0], array[1]):
    		array[2] = 1 #Cold
    	else: 
    		array[2] = 0

    	if np.random.rand() <= probFlu(array[0], array[1]):
    		array[3] = 1 #Flu probability
    	else: 
    		array[3] = 0

    	for j in range(5):
    		if np.random.rand() <= probSymptom(j+1, array[3], array[2]):
    			array[4 + j] = 1
    		else:
    			array[4 + j] = 0

    	if array[3] == 1 and array[5] == 1 and array[1] == 1:
    		numPositive += 1

    	if array[1] == 1 and array[5] == 1:
    		numSample += 1

    return (numPositive/numSample)



def inferProbFluExact() -> float:
    """
    This is question 10 part (b). This is a REACH problem, meaning 
    that thinking about it will be useful, even if we don't expect
    you to be able to perfectly solve the problem. Show your work.
    If you get stuck (> 15 mins), explain what is hard and
    include your explanation in your writeup, not in your code.

    Computes P(Flu = 1 | Exposure = 1, X_2 = 1) exactly without
    using rejection sampling.
    """


    return -1 # TODO: delete this line and implement the function!


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("***********************************************************")
    print("(a) Calling inferProbFlu():")
    print("\tReturn value was:", inferProbFlu())
    print("***********************************************************\n")

    print("***********************************************************")
    print("(b) Calling inferProbFluExact():")
    print("\tReturn value was:", inferProbFluExact())
    print("***********************************************************\n")

    print("Done!")


########### CS109 Problem Set 4, Question 12 ##############
"""
*********** Article submission **********
If you choose to submit an article for extra credit, it
  should be in a function named article_ec:
  - this function should take 0 arguments
  - edit the string variable sunetid to be your SUNetID,
    e.g., "yanlisa"
  - edit the string variable title to be your article title,
    e.g., "10 Reasons Why Probability Is Great"
  - edit the string variable url to be a URL to your article,
    e.g., "http://cs109.stanford.edu/"
  - you should not modify the return value
"""
def article_ec():
    sunetid = "" # your sunet id here.
    title = "" # your article title here
    url = "" # a link to your article here
    return sunetid, title, url


############################################################
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
