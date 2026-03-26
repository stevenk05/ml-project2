import random
import matplotlib.pyplot as plt
from time import sleep

trainingExamples = [["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", True],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", True],
    ["Rain", "Cold", "High", "Strong", "Warm", "Change", False],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", True]
]

MAXSPECIFIC = ['-', '-', '-', '-', '-', '-']

target_concept = ["Sunny", "Warm", '?', '?', '?', '?']

def generate_rand_training_example() -> list[str]:
    """
    The generate_rand_training_example() function generates a random training data from <Sunny, Warm, ?, ?, ?, ?>. as the target
    concept.

    :return: A single traning example with 6 attributes and a boolean value 
            indicating whether the example is a positive or negative example of the target concept
    """

    # :::NOTE:::
    # if we don't need any neg example since find s ignores them, just remove 'sky' and 'AirTemp' form the dic
    attr_dic = {
        "Sky" : ["Sunny", "Cloudy", "Rain"],
        "AirTemp" : ["Warm", "Cold"],
        "Humidity" : ["Normal", "High"],
        "Wind" : ["Strong", "Weak"],
        "Water" : ["Warm", "Cool"],
        "Forcast" : ["Same", "Change"]
    }

    # pick a rand attr-val from the dic
    training_example = []
    for x in attr_dic:
        training_example.append(random.choice(attr_dic[x]))

    # if sunny and warm, it must be a true example
    if training_example[0] == "Sunny" and training_example[1] == "Warm":
        training_example.append(True)
    else:
        training_example.append(False)

    return training_example

# Find-S Algorithm Implementation
# '-' represents the empty set symbol (no value of that attribute is allowed)
def findS(trainingExamples, temp_hypothesis = MAXSPECIFIC):
    for instance in trainingExamples:
        if(instance[6] == True):
            for i in range(6):
                if(temp_hypothesis[i] == '-' or (instance[i] != temp_hypothesis[i] and temp_hypothesis[i] != '?')):
                    if(temp_hypothesis[i] == '-'):
                        temp_hypothesis[i] = instance[i]
                    else:
                        temp_hypothesis[i] = '?'
    return temp_hypothesis

def count_iterations():

    temp_hypothesis = MAXSPECIFIC.copy()
    iterations = 0
    random_data = []
    random_data.append(generate_rand_training_example())

    while temp_hypothesis != target_concept:
        training_example = []
        training_example.append(generate_rand_training_example())
        temp_hypothesis = findS(training_example, temp_hypothesis)
        iterations += 1

    return iterations


def main():
    """

    :return:
    """

    experiment_iterations = 100
    iteration_counts = []

    #hypthesis = findS(trainingExamples)
    #print("The maximally specific hypothesis is: ", hypthesis)

    for _ in range(experiment_iterations):
        iteration_counts.append(count_iterations())

    print(iteration_counts)

if __name__ == "__main__":
    main()
