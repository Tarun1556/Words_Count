def count_words(user_input):
    """
    Function to count the number of words in the given input.
    :param user_input: string input from the user
    :return: integer count of words
    """
    if not user_input.strip():
        # Handle the case where input is empty or whitespace
        print("Error: No input provided. Please enter a valid sentence or paragraph.")
        return None
    # Split the input by spaces and count the words
    return len(user_input.split())

def main():
    """
    Main function to prompt user input, count words, and display the result.
    """
    print("Welcome to the Word Counter!")
    print("Please enter a sentence or paragraph below:")
    
    try:
        # Prompt the user for input
        user_input = input("> ")
        
        # Count the words in the input
        word_count = count_words(user_input)
        
        # Display the word count if input is valid
        if word_count is not None:
            print(f"The number of words in your input is: {word_count}")
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    main()
