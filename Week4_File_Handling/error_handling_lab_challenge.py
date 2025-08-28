def file_manipulation(input_filename, output_filename):
    try :
        with open(input_filename, 'r' ) as f:
            # read the content of the file in a stream
            contents = f.read()
            # count the number of words
            word_count = len(contents.split())
            # convert words to uppercase
            contents_upper = contents.upper()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied to read the file {input_filename}")
        return
    except Exception as e:
        print(f"An unexpected error occured {e}")
        return

    # Write to an output file
    with open(output_filename, 'w') as f:
        f.write(contents_upper)
        f.write(f"\n\nWord count : {word_count}\n")
        # Print success message
        print(f"Output message has been sent to : {output_filename} and contains {word_count} words")

# Asking user to enter the input filename
print(" Enter input file name : ")
input_filename = input("")
output_filename = "output.txt"
# Calling the function 
file_manipulation(input_filename, output_filename)