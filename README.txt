CSC426 - Machine Learning - Dr. Bloodgood 

Project 2: Find-S Algorithm and Random Training Example Experiment

Group members: Brian, Tyler, Steven, and A.J.

OBJECTIVE
Our objective is to implement the Find-S algorithm to find a maximally 
specific hypothesis consistent with a set of training examples, to verify
that it works correctly for the EnjoySport example from class, and to use it
to study the number of random training examples required to exactly learn 
the target concept.


All code is in the main.py file


FUNCTION DOCUMENTATION
generate_rand_training_example() - 
Generates a random instance and classifies it according to the target 
concept <Sunny, Warm, ?, ?, ?, ?>. Returns a list representing a single 
training example containing values for each of the 6 attributes (Sky, 
AirTemp, Humidity, Wind, Water, Forecast) and a boolean of whether or not 
the target concept is "Yes" or "No" (True for "Yes", False for "No").

findS(trainingExamples, trace_flag, curr_hypothesis = MAXSPECIFIC.copy()) -
Returns a maximally specific hypothesis consistent with the given training 
examples. The parameter "trainingExamples" represents the set of training 
examples to find the maximally specific hypothesis with. It receives a list 
of training examples, with each of these training examples being a list of length 7: 
6 items for the attribute values, and 1 item for the value of the target concept.
"trace_flag" receives a boolean: True if the program should output a trace of 
the intermediate hypotheses reached while finding a maximally specific one 
(desired for Task 2), and False otherwise. "curr_hypothesis" is the hypothesis 
that findS should start with. By default, this is set to the most specific 
hypothesis possible: <'-', '-', '-', '-', '-', '-'> (where '-' represents 
the null symbol [nothing is allowed]).

random_examples_experiment() -
Initiates the generation of random training examples and passes them into 
findS until the findS algorithm converges to the given target concept 
<Sunny, Warm, ?, ?, ?, ?>. Returns the number of training examples that it 
took for findS to converge to this target concept.

frequency_stats_histo(iteration_counts) -
Generates a frequency histogram from the list of the number of examples required for 
findS to converge to the given target concept in each experiment. Receives 
this list through the parameter "iteration_counts". Outputs the histogram as a pdf 
file with the name "iteration_histogram.pdf".

compute_stats(data) -
Computes the length (n), minimum, maximum, median, mean, standard deviation, 
and mode from a list of integers passed through the "data" parameter. Returns 
these values in a dictionary.

save_stats_table_pdf(stats) -
Generates a table of statistics (n, min, max, mode, median, mean, and 
standard deviation) given by the parameter "stats" and saves it as a pdf file 
with the name "stats_table.pdf". Receives the statistics as a dictionary through 
the parameter "stats".


HOW TO RUN ON THE TCNJ ELSA HPC
Upload the main.py file to the desired directory on your user of the TCNJ ELSA HPC
Open a terminal in this directory
Run "module add python/3.10.11" in the terminal to load the Python environment
Run "python main.py" to run the program
