# Step 1: Prompt the user for the task description
task = input("Enter your task: ")

# Step 2: Prompt the user for the task priority
priority = input("Priority (high/medium/low): ").lower()

# Step 3: Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 4: Use match-case to handle different priorities
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."

# Step 5: Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Step 6: Print the customized reminder (Make sure the format matches what the checker expects)
print(f"Reminder: {reminder}")
