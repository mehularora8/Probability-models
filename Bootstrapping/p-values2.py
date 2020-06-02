# Do NOT add any other import statements.
# Don't remove these import statements.
import numpy as np
import copy
import os

# Name:
# Stanford email:

########### CS109 Problem Set 5, Question 8 ##############
def get_filepath(filename):
    """
    filename is the name of a data file, e.g.,
    "learningOutcomes.csv". You can call this helper
    function in all parts of your code.
    Return a full path to the data file, located in the
    directory datasets, e.g., "datasets/learningOutcomes.csv"
    """
    return os.path.join("datasets", filename)

"""
Assembled by Lisa Yan and Past CS109 TA Anand Shankar
*************************IMPORTANT*************************
For part_a and part_b, do NOT modify the name of 
the functions. Do not add or remove parameters to them
either. Moreover, make sure your return value is exactly as
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""

def part_a(filename):
    """
    filename is the name of a data file, e.g. 
    "learningOutcomes.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.
    You can use the helper function defined above, get_filepath().
    Return the difference in sample means (float) as 
    described in the handout.
    """
    data = get_filepath(filename)

    learning_outcomes = np.genfromtxt(data, delimiter = ',', names = ['col1', 'col2', 'col3'], dtype = [('col1', np.int32), ('col2', np.dtype('U9')), ('col3', np.int32)])

    act1 = []
    act2 = []

    for i in range(len(learning_outcomes['col1'])):
        if learning_outcomes['col2'][i] == "activity1":
            act1.append(learning_outcomes['col3'][i])
        elif learning_outcomes['col2'][i] == "activity2":
            act2.append(learning_outcomes['col3'][i])

    return abs(np.mean(act1) - np.mean(act2))


def part_b(filename, seed=109):
    """
    filename is the name of a data file, e.g. 
    "learningOutcomes.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.
    You MUST use np.random.choice with replace=True
    to draw random samples. You may NOT use any other 
    function to draw random samples. See assignment 
    handout for details.
    Return the p-value (float) as described in the handout.
    """
    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE

    ### BEGIN YOUR CODE FOR PART (B) ###

    data = get_filepath(filename)

    learning_outcomes = np.genfromtxt(data, delimiter = ',', names = ['col1', 'col2', 'col3'], dtype = [('col1', np.int32), ('col2', np.dtype('U9')), ('col3', np.int32)])

    act1 = [] # Array to store learning outcomes where activity 1 was assigned
    act2 = [] # Array to store learning outcomes where activity 2 was assigned

    for i in range(len(learning_outcomes['col1'])):

        if learning_outcomes['col2'][i] == "activity1":
            act1.append(learning_outcomes['col3'][i])

        elif learning_outcomes['col2'][i] == "activity2":
            act2.append(learning_outcomes['col3'][i])

    # Both activity 1 and activity 2 outcomes combined
    combined_learning_outcomes = act1 + act2

    count = 0 # Count of p-error true values

    observed_diff = part_a(filename) #Observed difference in means

    for i in range(10000):

        # Draw respectively sized samples from combined distribution
        sample_for_activity1 = np.random.choice(combined_learning_outcomes, len(act1), replace = True)
        sample_for_activity2 = np.random.choice(combined_learning_outcomes, len(act2), replace = True)

        sample_mean_for_activity1 = np.mean(sample_for_activity1)
        sample_mean_for_activity2 = np.mean(sample_for_activity2)

        if abs(sample_mean_for_activity1 - sample_mean_for_activity2) >  observed_diff:
            count += 1

    return count / 10000

    ### END YOUR CODE FOR PART (B) ###


def optional_function():
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    backgrounds = get_filepath("background.csv")
    data = get_filepath("learningOutcomes.csv")

    learning_outcomes = np.genfromtxt(data, delimiter = ',', names = ['id', 'activity_number', 'outcome'], 
                        dtype = [('id', np.int32), ('activity_number', np.dtype('U9')), ('outcome', np.int32)])

    student_backgrounds = np.genfromtxt(backgrounds, delimiter = ',', names = ['id', 'bg'], dtype = [('id', np.int32), ('bg', np.dtype('U9'))])

    less_act1 = [] # Less background
    average_act1 = [] # Medium
    more_act1 = []
    less_act2 = [] # Less background
    average_act2 = [] # Medium
    more_act2 = []

    for i in range(len(learning_outcomes['id'])):

        if student_backgrounds['bg'][i] == "less":

            if learning_outcomes['activity_number'][i] == "activity1":
                less_act1.append(learning_outcomes['outcome'][i])
            else:
                less_act2.append(learning_outcomes['outcome'][i])

        elif student_backgrounds['bg'][i] == "average":

            if learning_outcomes['activity_number'][i] == "activity1":
                average_act1.append(learning_outcomes['outcome'][i])
            else:
                average_act2.append(learning_outcomes['outcome'][i])

        elif student_backgrounds['bg'][i] == "more":

            if learning_outcomes['activity_number'][i] == "activity1":
                more_act1.append(learning_outcomes['outcome'][i])
            else:
                more_act2.append(learning_outcomes['outcome'][i])

    observed_difference_for_less = abs(np.mean(less_act1) - np.mean(less_act2))
    observed_difference_for_average = abs(np.mean(average_act1) - np.mean(average_act2))
    observed_difference_for_more = abs(np.mean(more_act1) - np.mean(more_act2))

    combined_less = less_act1 + less_act2
    combined_average = average_act1 + average_act2
    combined_more = more_act2 + more_act1

    less_count = 0
    avg_count = 0
    more_count = 0

    for i in range(10000):

        # Draw respectively sized samples from combined distribution
        less_sample_for_activity1 = np.random.choice(combined_less, len(less_act1), replace = True)
        less_sample_for_activity2 = np.random.choice(combined_less, len(less_act2), replace = True)

        less_sample_mean_for_activity1 = np.mean(less_sample_for_activity1)
        less_sample_mean_for_activity2 = np.mean(less_sample_for_activity2)

        if abs(less_sample_mean_for_activity1 - less_sample_mean_for_activity2) >  observed_difference_for_less:
            less_count += 1

        average_sample_for_activity1 = np.random.choice(combined_average, len(average_act1), replace = True)
        average_sample_for_activity2 = np.random.choice(combined_average, len(average_act2), replace = True)

        average_sample_mean_for_activity1 = np.mean(average_sample_for_activity1)
        average_sample_mean_for_activity2 = np.mean(average_sample_for_activity2)

        if abs(average_sample_mean_for_activity1 - average_sample_mean_for_activity2) >  observed_difference_for_average:
            avg_count += 1

        more_sample_for_activity1 = np.random.choice(combined_more, len(more_act1), replace = True)
        more_sample_for_activity2 = np.random.choice(combined_more, len(more_act2), replace = True)

        more_sample_mean_for_activity1 = np.mean(more_sample_for_activity1)
        more_sample_mean_for_activity2 = np.mean(more_sample_for_activity2)

        if abs(more_sample_mean_for_activity1 - more_sample_mean_for_activity2) >  observed_difference_for_more:
            more_count += 1

    print("Observed diff for less: {}, p value:  {}".format(observed_difference_for_less, less_count/10000))
    print("Observed diff for avg: {}, p value:  {}".format(observed_difference_for_average, avg_count/10000))
    print("Observed diff for more: {}, p value:  {}".format(observed_difference_for_more, more_count/10000))

def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("****************************************************")
    print("Calling part_a with filename 'learningOutcomes.csv':")
    print("\tReturn value was:", part_a('learningOutcomes.csv'))
    print("****************************************************")

    print("****************************************************")
    print("Calling part_b with filename 'learningOutcomes.csv':")
    print("\tReturn value was:", part_b('learningOutcomes.csv'))
    print("****************************************************")

    print("****************************************************")
    print("Calling optional_function:")
    print("\tReturn value was:", optional_function())
    print("****************************************************")


    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()