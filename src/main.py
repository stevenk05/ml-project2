# Project 2: Find-S Algorithm and Random Training Example Experiment
# Course: CSC426-01 Machine Learning
# Members: Brian, Tyler, Steven, and A.J.
# Date: March 31, 2026
#
# Description:
# This project implements the Find-S algorithm to find the maximally
# specific hypothesis consistent with a set of training examples. This
# algorithm is tested with our EnjoySport training examples from class.
# It also conducts an experiment where random training examples 
# are generated until the Find-S algorithm converges to a specified 
# target concept. The number of iterations required for convergence 
# is recorded, and statistics about these iteration counts are computed and visualized.

import random
import sys
import matplotlib.pyplot as plt
import statistics

# EnjoySport training examples
trainingExamples = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", True],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", True],
    ["Rain", "Cold", "High", "Strong", "Warm", "Change", False],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", True]
]

MAXSPECIFIC = ['-', '-', '-', '-', '-', '-']

# the target concept that the random training examples are generated from
target_concept = ["Sunny", "Warm", '?', '?', '?', '?']

def generate_rand_training_example() -> list[str]:
    """
    The generate_rand_training_example() function generates a random training data from <Sunny, Warm, ?, ?, ?, ?> as the target
    concept.

    :return: A single training example with 6 attributes and a boolean value
            indicating whether the example is a positive or negative example of the target concept
    """

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
def findS(trainingExamples, trace_flag, curr_hypothesis = MAXSPECIFIC.copy()):
    """
    Core findS algorithm that produces a maximally specific hypothesis consistent with the given training examples.

    :param trainingExamples: A list of training examples.
    :param trace_flag: A flag to indicate a trace of the algorithm.
    :param curr_hypothesis: The current hypothesis being updated, initialized to the most specific
    :return: List of maximally specific attribute values that are consistent with the positive training examples.
    """

    # Output the starting hypothesis h_0 both to terminal and to an output file
    if (trace_flag == True):
        print(f"h_0: {curr_hypothesis}")
        o = sys.stdout
        with open('EnjoySport_trace.txt', 'w') as f:
            sys.stdout = f
            print(f"h_0: {curr_hypothesis}")
        sys.stdout = o

    for instance in trainingExamples:
        # positive training example
        if(instance[6] == True):
            for i in range(6):
                # If current attribute constrain is not satisfied by instance
                if(curr_hypothesis[i] == '-' or (instance[i] != curr_hypothesis[i] and curr_hypothesis[i] != '?')):
                    if(curr_hypothesis[i] == '-'):
                        curr_hypothesis[i] = instance[i]
                    else:
                        curr_hypothesis[i] = '?'

        # Output the current hypothesis both to terminal and to an output file
        if (trace_flag == True):
            print(f"h_{trainingExamples.index(instance) + 1}: {curr_hypothesis}")
            o = sys.stdout
            with open('EnjoySport_trace.txt', 'a') as f:
                sys.stdout = f
                print(f"h_{trainingExamples.index(instance) + 1}: {curr_hypothesis}")
            sys.stdout = o
    return curr_hypothesis

def random_examples_experiment():
    """
    Generates random training examples until the Find-S algorithm converges to the given 
    target concept <Sunny, Warm, ?, ?, ?, ?>.

    :return: The number of iterations (random training examples generated) required for 
            the Find-S algorithm to converge to the target concept.
    """

    curr_hypothesis = MAXSPECIFIC.copy()
    iterations = 0

    while curr_hypothesis != target_concept:
        training_example = []
        training_example.append(generate_rand_training_example())
        curr_hypothesis = findS(training_example, False, curr_hypothesis)
        iterations += 1

    return iterations

def frequency_stats_histo(iteration_counts):
    """
    Generates a histogram from the list of iteration counts.

    :param iteration_counts: A list of integers representing the number of iterations required for 
            the Find-S algorithm to converge to the target concept across multiple runs.
    """
    
    plt.hist(iteration_counts, bins= range(min(iteration_counts), max(iteration_counts) + 3), edgecolor='black')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Frequency')
    plt.title('Distribution of Iterations to Converge to Target Concept')
    plt.savefig(fname = "../docs/iteration_histogram.pdf", format='pdf')

def save_stats_table_pdf(stats):
    """
    Generates a table of statistics (n, min, max, mode, median, mean, std deviation) and saves it as pdf.

    :param stats: A dictionary containing the statistics
    """

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
    plt.savefig(fname = "../docs/stats_table.pdf", format='pdf')
    plt.close(fig)

def compute_stats(data):
    """
    Computes various statistics from a list of integers

    :param data: A list of integers.
    :return: A dictionary containing the computed statistics (n, min, max, mode, median, mean, std deviation).
    """

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

    experiment_iterations = 1000
    iteration_counts = []

    # findS using the given training examples from the EnjoySport example
    print("\nVerification of Correct Trace for EnjoySport Example (also saved as a .txt file):")
    hypothesis = findS(trainingExamples, True)
    # Output the maximally specific hypothesis both to terminal and to an output file
    print("The maximally specific hypothesis is: ", hypothesis)
    o = sys.stdout
    with open('EnjoySport_trace.txt', 'a') as f:
        sys.stdout = f
        print("The maximally specific hypothesis is: ", hypothesis)
    sys.stdout = o

    # run the experiment for a specified number of iterations and collect the iteration counts
    for _ in range(experiment_iterations):
        iteration_counts.append(random_examples_experiment())
    print(f"\nAll {experiment_iterations} experiments finished")

    # generate and save histogram and statistics table
    frequency_stats_histo(iteration_counts)
    frequency_stats = compute_stats(iteration_counts)
    save_stats_table_pdf(frequency_stats)
    print("Histogram and data table saved")


if __name__ == "__main__":
    main()
