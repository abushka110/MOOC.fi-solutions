import os

# Function to format the directory or file name
def format_name(name):
    name = name.replace(':', '').replace('.', '')
    return '-'.join(word.capitalize() for word in name.split())

# Open the file
with open('filesFolders.txt', 'r') as f:
    lines = f.readlines()

# Initialize the current directory to the root directory
current_dir = 'test'

# Iterate over each line in the file
for line in lines:
    line = line.strip()  # Remove leading/trailing whitespace

    # If the line starts with 'folder', it's a directory
    if line.lower().startswith('folder'):
        # Remove 'folder' from the directory name
        line = line.replace('folder ', '')
        
        # Create the directory under the root directory
        current_dir = os.path.join('test', format_name(line))
        os.makedirs(current_dir, exist_ok=True)
    else:
        # Skip files that contain 'Quiz'
        if 'Quiz' in line:
            continue

        # Remove 'Programming exercise: ' from the file name
        line = line.replace('Programming exercise: ', '')
        
        # Create a Python file in the current directory
        file_path = os.path.join(current_dir, f"{format_name(line)}.java")
        with open(file_path, 'w') as f:
            # Add lines to each created Python file
            f.write("# solution\n\n")
            f.write("# test\n")
            f.write("if __name__ == \"__main__\":\n")
            f.write("    pass  # Add your test code here\n")
