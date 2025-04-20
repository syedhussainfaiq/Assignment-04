def mad_libs():
    # Prompt the user for words
    adjective = input("Please type an adjective and press enter: ").strip()
    noun = input("Please type a noun and press enter: ").strip()
    verb = input("Please type a verb and press enter: ").strip()

    # Construct and print the sentence
    sentence_start = "Code in Place is fun. I learned to program and used Python to make my"
    print(f"\n{sentence_start} {adjective} {noun} {verb}!")

# Run the program
mad_libs()
