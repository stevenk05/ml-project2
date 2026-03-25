import random
import matplotlib.pyplot as plt


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
    maxSpecific = ['-', '-', '-', '-', '-', '-']
    for instance in trainingExamples:
        if(instance[6] == True):
            for i in range(6):
                if(maxSpecific[i] == '-' or (instance[i] != maxSpecific[i] and maxSpecific[i] != '?')):
                    if(maxSpecific[i] == '-'):
                        maxSpecific[i] = instance[i]
                    else:
                        maxSpecific[i] = '?'
    return maxSpecific

def main():
    """

    :return:
    """

    rand_target_concept = generate_rand_concept()
    #print(rand_target_concept)
    pass

if __name__ == "__main__":
    main()
