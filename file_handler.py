filename= input ("Enter the file name: ")
try:        
    with open(filename, 'r') as file:
        content = file.read()
        
        modified_content = content.upper()

        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"\nSuccess! Modified file saved as: {new_filename}")
        

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to read the file '{filename}'.")
except IOError as e:
    print(f"\nError: An I/O error occurred: {e}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")