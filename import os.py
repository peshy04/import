import os

def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Check if the file exists
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")
        
        # Read the content of the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Ask the user for the output filename
        output_filename = input("Enter the name of the file to write the modified content: ")
        
        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print("You do not have permission to read or write to the specified file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    read_and_write_file()