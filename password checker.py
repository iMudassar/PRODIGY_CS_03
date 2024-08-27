import re

def assess_password_strength(password):
    # Initialize variables for password strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password)
    lowercase_criteria = re.search(r"[a-z]", password)
    number_criteria = re.search(r"[0-9]", password)
    special_char_criteria = re.search(r"[\W_]", password)
    
    # Count the number of criteria met
    criteria_met = sum([length_criteria, bool(uppercase_criteria), bool(lowercase_criteria), bool(number_criteria), bool(special_char_criteria)])
    
    # Determine password strength based on the criteria met
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Provide feedback to the user
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")
    
    # Print the strength and feedback
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")

def main():
    while True:
        password = input("Enter a password to assess its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Exiting the program.")
            break
        assess_password_strength(password)
        print()  # Add a newline for better readability between checks

# Start the program
if __name__ == "__main__":
    main()
