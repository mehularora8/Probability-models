# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np
import os

# Name:
# Stanford email:

########### CS109 Problem Set 5, Question 6 ##############
def get_filepath(filename):
    """
    filename is the name of a data file, e.g.,
    "personKeyTimingA.txt". You can call this helper
    function in all parts of your code.

    Return a full path to the data file, located in the
    directory datasets, e.g., "datasets/personKeyTimingA.txt"
    """
    return os.path.join("datasets", filename)

"""
Assembled by Lisa Yan and Past CS109 TA Anand Shankar
*************************IMPORTANT*************************
For part_a and part_b, do NOT modify the name of the 
functions. Do not add or remove parameters to them either.
Moreover, make sure your return value is exactly as 
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""


def part_a(filename):
    """
    filename is the name of a data file, e.g. 
    "personKeyTimingA.txt". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.
    You can use the helper function defined above, get_filepath().

    Let X be a random variable as defined in the 
    assignment handout. You should compute and
    return E[X] (which is of type float).
    """
    data = get_filepath(filename)

    timings = np.genfromtxt(data, delimiter = ',', names = ['col1', 'col2'], dtype = [('col1', np.int32), ('col2', np.dtype('U7'))])

    keystroke_times = []

    numStrokes = len(timings['col1'])

    keystroke_times.append(timings['col1'][0])

    for i in range(1, numStrokes):
        keystroke_times.append(timings['col1'][i] - timings['col1'][i-1])

    return np.mean(keystroke_times)

def part_b(filename):
    """
    filename is the name of a data file, e.g. 
    "personKeyTimingA.txt". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    Let X be a random variable as defined in the 
    assignment handout. You should compute and
    return E[X^2] (which is of type float).
    """
    data = get_filepath(filename)

    timings = np.genfromtxt(data, delimiter = ',', names = ['col1', 'col2'], dtype = [('col1', np.float32), ('col2', np.dtype('U7'))])

    keystroke_times = []

    numStrokes = len(timings['col1'])

    keystroke_times.append(timings['col1'][0] ** 2)

    for i in range(1, numStrokes):
        keystroke_times.append((timings['col1'][i] - timings['col1'][i-1]) ** 2)

    return np.mean(keystroke_times)


def optional_function():
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    pass  # TODO: delete this line and optionally implement the function!


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("***********************************************************")
    print("    Calling part_a with filename 'personKeyTimingA.txt'    ")
    print("\tReturn value was:", part_a('personKeyTimingA.txt'))
    print("***********************************************************\n")

    print("***********************************************************")
    print("    Calling part_a with filename 'personKeyTimingB.txt'    ")
    print("\tReturn value was:", part_a('personKeyTimingB.txt'))
    print("***********************************************************\n")

    print("***********************************************************")
    print("    Calling part_b with filename 'personKeyTimingA.txt'    ")
    print("\tReturn value was:", part_b('personKeyTimingA.txt'))
    print("***********************************************************\n")

    print("***********************************************************")
    print("    Calling part_b with filename 'personKeyTimingB.txt'    ")
    print("\tReturn value was:", part_b('personKeyTimingB.txt'))
    print("***********************************************************\n")

    print("***********************************************************")
    print("                 Calling optional_function                 ")
    print("\tReturn value was:", optional_function())
    print("***********************************************************\n")

    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
