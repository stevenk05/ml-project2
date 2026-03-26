import random
import matplotlib.pyplot as plt
import math
import statistics
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
def findS(trainingExamples, temp_hypothesis = MAXSPECIFIC.copy()):
    for instance in trainingExamples:
        if(instance[6] == True):
            for i in range(6):
                if(temp_hypothesis[i] == '-' or (instance[i] != temp_hypothesis[i] and temp_hypothesis[i] != '?')):
                    if(temp_hypothesis[i] == '-'):
                        temp_hypothesis[i] = instance[i]
                    else:
                        temp_hypothesis[i] = '?'

            #if (trace_flag == True):
            #print(temp_hypothesis)
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
        print(temp_hypothesis)
        #sleep(0.5)

    return iterations

def frequency_statistics(iteration_counts):
    
    plt.hist(iteration_counts, bins= range(min(iteration_counts), max(iteration_counts) + 3), edgecolor='black')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Frequency')
    plt.title('Distribution of Iterations to Converge to Target Concept')
    plt.savefig(fname = "iteration_histogram.pdf", format='pdf')

def save_stats_table_pdf(stats):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.axis('off')
    table_data = [
        ["n",              str(stats["n"])],
        ["Min",            str(stats["min"])],
        ["Max",            str(stats["max"])],
        ["Mode",           str(stats["mode"])],
        ["Median",         str(stats["median"])],
        ["Mean",           f"{stats['mean']:.4f}"],
        ["Std Deviation",  f"{stats['std_dev']:.4f}"],
    ]
    table = ax.table(cellText=table_data, colLabels=["Statistic", "Value"],
                        loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.4, 1.8)
    ax.set_title("Statistics: Examples Required to Learn Target Concept", pad=20)
    plt.tight_layout()
    plt.savefig(fname = "stats_table.pdf", format='pdf')
    plt.close(fig)

def compute_stats(data):
    n = len(data)
    minimum = min(data)
    maximum = max(data)
    median = statistics.median(data)
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    mode = statistics.mode(data)

    return {"n": n, "min": minimum, "max": maximum, "mode": mode,
            "median": median, "std_dev": std_dev, "mean": mean}


def main():
    """

    :return:
    """

    experiment_iterations = 100000
    iteration_counts = []

    hypothesis = findS(trainingExamples)
    print("The maximally specific hypothesis is: ", hypothesis)


    for _ in range(experiment_iterations):
        iteration_counts.append(count_iterations())

    print(min(iteration_counts))
    frequency_statistics(iteration_counts)
    frequency_stats = compute_stats(iteration_counts)
    save_stats_table_pdf(frequency_stats)


if __name__ == "__main__":
    main()
