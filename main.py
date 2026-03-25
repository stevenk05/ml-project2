import matplatlib.pyplot as plt

trainingExamples = [["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", True],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", True],
    ["Rain", "Cold", "High", "Strong", "Warm", "Change", False],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", True]
]

# Find-S Algorithm Implementation
# '-' represents the empty set symbol (no value of that attribute is allowed)
maxSpecific = ['-', '-', '-', '-', '-', '-']
for instance in trainingExamples:
    if(instance[6] == True):
        for i in range(6):
            if(maxSpecific[i] == '-' or (instance[i] != maxSpecific[i] and maxSpecific[i] != '?')):
                if(maxSpecific[i] == '-'):
                    maxSpecific[i] = instance[i]
                else:
                    maxSpecific[i] = '?'
print(maxSpecific)



def main():
    pass

if __name__ == "__main__":
    main()