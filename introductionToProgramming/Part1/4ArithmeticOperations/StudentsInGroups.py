# Get the number of students on the course
num_students = int(input("How many students on the course? "))

# Get the desired group size
group_size = int(input("Desired group size? "))

# Calculate the number of groups formed
num_groups = (num_students + group_size - 1) // group_size

# Print the result
print("Number of groups formed:", num_groups)
