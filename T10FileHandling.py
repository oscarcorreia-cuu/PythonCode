import os

# Function to write data to a new file
def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write('This is an example of file manipulation in Python.\n')
        file.write('We are demonstrating various file operations.\n')
    print(f"Data written to {filename}.")

# Function to read data from a file
def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(f"Content of {filename}:")
    print(content)

# Function to append data to a file
def append_to_file(filename):
    with open(filename, 'a') as file:
        file.write('Appending a new line to the file.\n')
    print(f"Data appended to {filename}.")

# Function to rename a file
def rename_file(old_filename, new_filename):
    if os.path.exists(new_filename):
        os.remove(new_filename)  # Delete the file
        print(f"{new_filename} has been deleted.")
    else:
        print(f"{new_filename} does not exist.")
    os.rename(old_filename, new_filename)
    print(f"File renamed from {old_filename} to {new_filename}.")

# Function to delete a file
def delete_file(filename):
    os.remove(filename)
    print(f"File '{filename}' has been deleted.")

# Main demonstration function
def file_operations_demo():
    # Step 1: Write to file
    filename = 'example.txt'
    write_to_file(filename)

    # Step 2: Read from the file
    read_from_file(filename)

    # Step 3: Append data to the file
    append_to_file(filename)

    # Step 4: Read updated content
    read_from_file(filename)

    # Step 5: Rename the file
    new_filename = 'example_renamed.txt'
    rename_file(filename, new_filename)

    # Step 6: Read from the renamed file
    read_from_file(new_filename)

    # Step 7: Delete the file
    # delete_file(new_filename)

# Execute the file operations demo
try:
    file_operations_demo()
except FileExistsError:
    print("You are trying to rename your file to an exiting file.")
