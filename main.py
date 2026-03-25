import random
import matplotlib.pyplot as plt

trainingExamples = [["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", True],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", True],
    ["Rain", "Cold", "High", "Strong", "Warm", "Change", False],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", True]
]

maxSpecific = ['-', '-', '-', '-', '-', '-']

def generate_rand_concept() -> list[str]:
    """
    The generate_rand_concept() function generates a random target concept from <Sunny, Warm, ?, ?, ?, ?>.

    :return: List of random target concepts
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
    target_concept = []
    for x in attr_dic:
        target_concept.append(random.choice(attr_dic[x]))

    # if sunny and warm, it must be a true example
    if target_concept[0] == "Sunny" and target_concept[1] == "Warm":
        target_concept.append(True)
    else:
        target_concept.append(False)

    return target_concept

# Find-S Algorithm Implementation
# '-' represents the empty set symbol (no value of that attribute is allowed)
def findS(trainingExamples):
    temp_hypothesis = maxSpecific
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

    temp_hypothesis = maxSpecific
    iterations = 0
    random_data = generate_rand_concept()
    print(type(random_data))

    while '?' or '-' in temp_hypothesis:
        random_data = generate_rand_concept()
        print(random_data)
        temp_hypothesis = findS(random_data)
        iterations += 1

    return iterations


def main():
    """

    :return:
    """

    hypthesis = findS(trainingExamples)
    print("The maximally specific hypothesis is: ", hypthesis)

    print(count_iterations())

    # for i in range(100):
    #     rand_target_concept = generate_rand_concept()
    #     print(len(rand_target_concept))


if __name__ == "__main__":
    main()
