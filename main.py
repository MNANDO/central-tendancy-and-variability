from math import sqrt

def mean(values):
    sum = 0
    n = len(values)
    for v in values:
        sum += v
    return sum/n

def populationVariance(values, mean):
    num = 0
    denom = len(values)
    
    for v in values: 
        num += pow((v - mean), 2)
    return num/denom

def sampleVariance(values, mean):
    num = 0
    denom = len(values) - 1
    
    for v in values: 
        num += pow((v - mean), 2)
    return num/denom

def populationDeviation(values, mean):
    return sqrt(populationVariance(values, mean))

def sampleDeviation(values, mean):
    return sqrt(sampleVariance(values, mean))

def main():
    values = []
    
    while True:
        print("Enter value " + str(len(values)+1) + " (-1 if complete): ") 
        value = input()
        if (value == "-1"):
            break
        values.append(float(value))

    print("mean: " + str(mean(values)))
    print ("population variance: " + str(populationVariance(values, mean(values))))
    print ("sample variance: " + str(sampleVariance(values, mean(values))))
    print ("population deviation: " + str(populationDeviation(values, mean(values))))
    print ("sample deviation: " + str(sampleDeviation(values, mean(values))))

if __name__ == "__main__":
    main()
