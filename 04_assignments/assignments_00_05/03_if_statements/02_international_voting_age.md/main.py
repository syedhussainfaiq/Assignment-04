def check_voting_eligibility():
    """
    Prompts the user for their age and checks if they can vote in three fictional countries.
    """
    # Voting ages for the countries
    voting_age_peturksbouipo = 16
    voting_age_stanlau = 25
    voting_age_mayengua = 48

    # Prompt the user for their age
    age = int(input("How old are you? "))

    # Check eligibility for Peturksbouipo
    if age >= voting_age_peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is {voting_age_peturksbouipo}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {voting_age_peturksbouipo}.")

    # Check eligibility for Stanlau
    if age >= voting_age_stanlau:
        print(f"You can vote in Stanlau where the voting age is {voting_age_stanlau}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {voting_age_stanlau}.")

    # Check eligibility for Mayengua
    if age >= voting_age_mayengua:
        print(f"You can vote in Mayengua where the voting age is {voting_age_mayengua}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {voting_age_mayengua}.")

# Run the function
check_voting_eligibility()
