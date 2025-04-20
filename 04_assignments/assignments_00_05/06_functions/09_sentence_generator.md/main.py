def make_sentence(word, part_of_speech):
    """
    Generate a sentence using the given word based on its part of speech.
    
    Args:
        word (str): The word to be inserted into the sentence
        part_of_speech (int): 0 for noun, 1 for verb, 2 for adjective
    """
    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech!")

def main():
    # Get input from user
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Generate and print the sentence
    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main() 