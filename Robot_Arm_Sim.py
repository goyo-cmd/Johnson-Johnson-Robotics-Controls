# Import required libraries
import numpy as np  # For numerical calculations
import matplotlib.pyplot as plt  # For data visualization

# Function to simulate response time improvements
def simulate_response_time(base_time, efficiency_factor):
    """Calculate the new response time based on efficiency improvements."""
    return base_time * (1 - efficiency_factor)

# Function to simulate durability improvements
def simulate_durability(base_durability, reinforcement_factor):
    """Calculate the new durability score based on reinforcement."""
    return base_durability + (base_durability * reinforcement_factor)

# Example Base Metrics
base_response_time = 0.20  # in seconds
base_durability = 75       # durability score out of 100

# User Inputs with Validation
while True: ##This loop repeats for ever until something stops it
    try: #Try running this code
        #Convert and store the efficiency input to a number from string input
        efficiency_factor = float(input("Enter efficiency improvement factor (between 0 and 1, e.g., 0.15 for 15%): "))
        #Check valid range for the value given. Is it greater than or equal to 0 AND less than or equal to 1
        if 0 <= efficiency_factor <= 1:
            break   #if true it runs
        else:
            print("Please enter a value between 0 and 1.")
    #Catch the error and ask for numerical value if one is not given
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

while True:
    try:
        reinforcement_factor = float(input("Enter durability reinforcement factor (between 0 and 1, e.g., 0.10 for 10%): "))
        if 0 <= reinforcement_factor <= 1:
            break
        else:
            print("Please enter a value between 0 and 1.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Simulations
new_response_time = simulate_response_time(base_response_time, efficiency_factor)
new_durability = simulate_durability(base_durability, reinforcement_factor)

# Output Results
print("\nSimulation Results:")
print(f"Original Response Time: {base_response_time} seconds")
print(f"New Response Time: {round(new_response_time, 3)} seconds")
print(f"Original Durability Score: {base_durability}")
print(f"New Durability Score: {round(new_durability, 2)}")


# Visual Feedback
metrics = ["Response Time (seconds)", "Durability Score"]
original_values = [base_response_time, base_durability]
new_values = [new_response_time, new_durability]

plt.figure(figsize=(8, 5))
x = np.arange(len(metrics)) #Takes the length of metrics(2) and creates [0 1] these will be the 
                            #x-axis position bars. They are evenly spaced positions from arrange
width = 0.35    #define width for the bar in the graph/plot

#Remember x is [0 1] 0 for the response time bars position and 1 for the durability score position
#Shift the location of the bars slightly left by subtracting width/2
plt.bar(x - width/2, original_values, width, label='Original', color='blue')
# Shift the new pairs slightly right to have the bars side by side
plt.bar(x + width/2, new_values, width, label='New', color='green')

plt.xlabel("Metrics")
plt.ylabel("Values")
plt.title("Simulation Results: Original vs New")
plt.xticks(x, metrics)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
