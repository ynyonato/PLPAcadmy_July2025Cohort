def file_manipulation(input_filename, output_filename):
    with open(input_filename, 'r' ) as f:
        # read the content of the file in a stram
        contents = f.read()
    
    # count the number of words
    word_count = len(contents.split())
    
    # convert words to uppercase
    contents_upper = contents.upper()
    
    # Write to an output file
    with open(output_filename, 'w') as f:
        f.write(contents_upper)
        f.write(f"\n\nWord count : {word_count}\n")

    # Print sucess message
    print(f"Output message has been sent to : {output_filename} and contains {word_count} words")

# Calling the function 
file_manipulation("input.txt", "output.txt")