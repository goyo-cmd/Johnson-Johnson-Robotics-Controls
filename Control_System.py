# Import required libraries
import time  # For measuring response times
import numpy as np  # For numerical calculations



# List of commands to test
commands = ["move_arm", "rotate_joint", "adjust_grip"]

# Define a function to measure the response time of commands
def check_response_time(command):
    """Simulates command execution and measures response time."""
    start_time = time.time()
    if command == "rotate_joint":
        time.sleep(0.14)  # Simulate delay for rotate_joint
    elif command == "move_arm":
        time.sleep(0.08)  # Simulate moderate response time
    elif command == "adjust_grip":
        time.sleep(0.06)  # Simulate delayed response
    response_time = time.time() - start_time
    return response_time

# Measure and print response times for each command
print("\nTesting initial command response times:")
for cmd in commands:
    response_time = check_response_time(cmd)
    print(f"{cmd} response time: {round(response_time, 3)} seconds")

# Define the Expected Response Time for each command
expected_response_times = [0.10, 0.15, 0.05]  # Expected response times for move_arm, rotate_joint, adjust_grip respectively

#Compare the response times to the expected times to Analyze performance
print("\nCommand Overview:")
results = []

for cmd in commands:
    response_time = check_response_time(cmd)
    expected = expected_response_times[commands.index(cmd)]
    performance_status = "OK - Command running as expected" if response_time <= expected else "SLOW - Command slower than expected"
    
    results.append([cmd, round(response_time, 3), expected, performance_status])
    
# Print table with formatted columns
print("\n" + "-"*120)
print(f"{'Command':<15} {'Observed Response Time':<30} {'Expected Response Time':<30} {'Notes on Performance':<30}")
print("-"*120)
for row in results:
    print(f"{row[0]:<15} {row[1]:<30} {row[2]:<30} {row[3]:<30}")
print("-"*120)

#print(results)

# Check statuses of the commands and display slow commands only. Suggest possible causes of delays
"""Varialbe to store those commands that appear as slow in the results list row 4 (Index 3)"""
slow_commands = [row[0] for row in results if row[3] == "SLOW - Command slower than expected"]
    
if slow_commands: 
    print("\n Please address the following:")
    matched_command = slow_commands
    for matched_command in slow_commands:

    
        if matched_command == "move_arm":
            print(f"\n⚠️  Slow move_arm command: Check arm Calibration, Check power to motor, check command calculations for issues")
    
        elif matched_command == "rotate_joint":
            print(f"\n⚠️  Slow rotate_joint command: Check joint Calibration or check for obstruction, Check power to motor, check command calculations for issues")
    
        elif matched_command == "adjust_grip":
            print(f"\n⚠️  Slow adjust_grip command: Check grip for wear, Check power to motor, check command calculations for issues")

else:
    print("\n✓ All commands within expected limits!")


#Define optimization function
def optimized_command(command, improvement_factor=0.2):
    """Simulates optimized command execution."""
    print(f"\n Optimizing command: {command}")  # Placeholder action
    optimized_response_time = check_response_time(command) * (1 - improvement_factor)
    return optimized_response_time

#Apply optimization to slow commands only
for row in results:
    if row[3] == "SLOW - Command slower than expected":
        command = row[0]
        observed_response_time = row[1]
        
        new_response_time = optimized_command(command)
        
        row[1] = round(new_response_time, 3)   # Replace observed response time
        row[3] = "OPTIMIZED"                   # Optional: update the status
        
        
        print(f"\n Optimized Response time for {command} is {round(new_response_time, 3)} seconds")


print("\nUpdated Command Overview:")
print("-"*120)
print(f"{'Command':<15} {'Observed Response Time':<30} {'Expected Response Time':<30} {'Notes on Performance':<30}")
print("-"*120)

for row in results:
    print(f"{row[0]:<15} {row[1]:<30} {row[2]:<30} {row[3]:<30}")

print("-"*120)


# Diagnostic findings: Detail the issues identified in the code and their relation to response delays.
# Solution and Validation: Explain the code fix implemented and the validation steps taken to confirm the solution.
"""The code did not optimize the response time once a low response time was observed. Optimixation was since added to
improve the response time of the robot arm part with delays.Suggestion for checking physical and software issues
that may be the cause of the delay are clearly printed now so that on can take immediate action toawrds a solution.
"""
# Solution and Validation: Explain the code fix implemented and the validation steps taken to confirm the solution.
"""Now if there is any slow response time detected, the note on the slow performance will be displayed in a table.
A warning will let the user know that the command is slow and then try optimizing the response time through software.
The response time is then measure again one last time to verify that the new time for the command has improved and is displayed
on a table once again."""
