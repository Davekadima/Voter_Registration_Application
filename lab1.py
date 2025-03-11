"""
Voter Registration Application
This program asks for user information and checks if they can register to vote.
"""

def is_valid_state(state):
    """ Checks if the state abbreviation is correct."""
    # A list of all the correct 2-letter abbreviations for U.S. states.
    valid_states = {
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
        "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
        "VA", "WA", "WV", "WI", "WY",
    }
    # Check if the input state is in the set of valid states.
    return state in valid_states

# Print a welcome message to the user.
print("Welcome to the Voter Registration Application!")

def get_user_input(prompt):
    """ Asks the user for their input and removes extra spaces."""
    # Get user input using the provided prompt.
    user_input = input(prompt)
    # Remove any leading or trailing spaces from the input and convert to lowercase.
    return user_input.strip().lower()

# Ask the user if they want to continue with the registration process.
if get_user_input("Do you want to continue with Voter Registration? (yes/no): ") == "yes":
    # If the user wants to continue, proceed with the registration.
    # Ask for the user's first name.
    first_name = input("Enter your first name: ")
    # Ask for the user's last name.
    last_name = input("Enter your last name: ")
    # Ask for the user's age.
    age = input("Enter your age: ")
    # Validate the user's age.
    while not age.isdigit() or not 18 <= int(age) <= 120:
        # If the age is invalid, print an error message and ask for the age again.
        print("Invalid age. You must be between 18 and 120 years old.")
        age = input("Enter your age: ")
    # Ask if the user is a U.S. citizen.
    citizenship = get_user_input("Are you a U.S. citizen? (yes/no): ")
    # Check if the user is a U.S. citizen.
    if citizenship != "yes":
        # If the user is not a U.S. citizen, print an error message.
        print("Sorry, only U.S. citizens can register to vote.")
    else:
        # Ask for the user's state.
        user_state = input("Enter your state (2-letter code): ").strip().upper()
        # Validate the user's state.
        while not is_valid_state(user_state):
            # If the state is invalid, print an error message and ask for the state again.
            print("Invalid state code. Please enter a valid 2-letter state abbreviation.")
            user_state = input("Enter your state (2 letters code): ").strip().upper()
        # Ask for the user's zipcode.
        zipcode = input("Enter your 5-digit zipcode: ")
        # Validate the user's zipcode.
        while not zipcode.isdigit() or len(zipcode) != 5:
            # If the zipcode is invalid, print an error message and ask for the zipcode again.
            print("Invalid zipcode. Please enter a 5-digit number.")
            zipcode = input("Enter your 5-digit zipcode: ")
        # Print a confirmation message with the user's information.
        print("\n" + "-" * 40)
        print("         VOTER REGISTRATION SUMMARY         ")
        print("-" * 40)
        print(f"Name:       {first_name} {last_name}")
        print(f"Age:        {age}")
        print("U.S. Citizen: Yes")
        print(f"State:      {user_state.upper()}")
        print(f"Zipcode:    {zipcode}")
        print("-" * 57)
        print("Your voter registration card will arrive in a few weeks!")
        print("-" * 57)

else:
    # If the user does not want to continue, print a cancellation message.
    print("Registration cancelled.")
