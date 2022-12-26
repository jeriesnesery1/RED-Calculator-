import random

def calculate_red(avg_length, min_threshold, max_threshold, max_p,count):
    temp_p = max_p * (avg_length - min_threshold) / (max_threshold - min_threshold)
    p=temp_p/(1-(count*temp_p))
    return p

# Example usage
avg_length = 35
min_threshold = 20
max_threshold = 40
max_p = 0.04
count=0
# Generate a table of probabilities
print("Packet\tProbability")
while(True):
    probability=calculate_red(avg_length, min_threshold, max_threshold, max_p,count)
    
    
    print(f"{count}\t{probability}")
    count=count+1
    if(probability>=1):
        break;
