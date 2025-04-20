


def main():
    adjective_1: str = input("Please type an adjective and press enter: ")
    noun_1: str = input("Please type a noun and press enter: ")
    verb_1: str = input("Please type a verb and press enter: ")
    noun_2: str = input("Please type a noun and press enter: ")
    adjective_2: str = input("Please type an adjective and press enter: ")
    noun_3: str = input("Please type a noun and press enter: ")
    noun_4: str = input("Please type a noun and press enter: ")
    verb_2: str = input("Please type a verb and press enter: ")
    noun_5: str = input("Please type a noun and press enter: ")
    adjective_3: str = input("Please type an adjective and press enter: ")
    noun_6: str = input("\Please type a noun and press enter: ")

    madlib: str = f"The other day, I saw a/an {noun_1} in the street. It was very {adjective_1} and it started to {verb_1}. I quickly grabbed my {noun_2} and ran away. It was a very {adjective_2} {noun_3}. When I got home, I told my {noun_4} what had {verb_2} and they gave me a {noun_5}. It was a very {adjective_3} {noun_6}."

    print(f"\n{madlib}\n")

if __name__ == '__main__':
    main()