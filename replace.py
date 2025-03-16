import os

# Define the root directory (current directory)
root_dir = '.'

# Define the words to replace and their replacements
replacements = {
    "vidhi-jaju": "udyThe",
    "vidhi": "uday",
    "jaju": "surothiya",
    "Jaju": "Surothiya",
    "Vidhi": "Uday",
    "DockSpace": "containerexp"
}

# Function to check if a file is binary
def is_binary(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the first 1024 bytes to check for binary content
            chunk = file.read(1024)
            # Check for null bytes or non-UTF-8 characters
            if b'\x00' in chunk:
                return True
            try:
                chunk.decode('utf-8')
            except UnicodeDecodeError:
                return True
        return False
    except Exception:
        return True

# Function to replace words in a file's content
def replace_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()

        # Perform replacements in the file content
        for old_word, new_word in replacements.items():
            file_contents = file_contents.replace(old_word, new_word)

        # Write the updated contents back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_contents)
        print(f"Processed content in: {file_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

# Recursively scan through all files in the directory
for subdir, _, files in os.walk(root_dir):
    for file in files:
        file_path = os.path.join(subdir, file)

        # Skip Git-related files and directories
        if '.git' in file_path.split(os.sep):
            print(f"Skipping Git file: {file_path}")
            continue

        # Skip binary files
        if is_binary(file_path):
            print(f"Skipping binary file: {file_path}")
            continue

        # Process the file
        replace_in_file(file_path)

print("Replacement complete!")