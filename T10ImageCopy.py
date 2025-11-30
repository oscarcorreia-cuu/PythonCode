def write_binary_file(input_filename, output_filename):
    try:
        # Step 1: Read the image file in binary mode
        with open(input_filename, 'rb') as input_file:
            binary_data = input_file.read()
        print(f"Successfully read from '{input_filename}'")

        # Step 2: Write the binary data to a new file
        with open(output_filename, 'wb') as output_file:
            output_file.write(binary_data)
        print(f"Successfully written to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"An error occurred while handling the file: {e}")

# Example usage
input_image = 'example_image.png'  # Ensure this image exists in your current directory
output_image = 'copied_image.png'
write_binary_file(input_image, output_image)
