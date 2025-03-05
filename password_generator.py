


import random
import string

class PasswordGenerator:
    def __init__(self):
        self.complexity_levels = {
            "1": {"lowercase": string.ascii_lowercase},
            "2": {"lowercase": string.ascii_lowercase, "uppercase": string.ascii_uppercase},
            "3": {"lowercase": string.ascii_lowercase, "uppercase": string.ascii_uppercase, "digits": string.digits},
            "4": {"lowercase": string.ascii_lowercase, "uppercase": string.ascii_uppercase, "digits": string.digits, "punctuation": string.punctuation}
        }

    def generate_password(self, length, complexity):
        char_pool = "".join(complexity.values())
        return "".join(random.choice(char_pool) for _ in range(length))

    def get_complexity(self):
        while True:
            print("\nChoose the complexity of the password:")
            print("1. Lowercase only")
            print("2. Lowercase + Uppercase")
            print("3. Lowercase + Uppercase + Digits")
            print("4. Lowercase + Uppercase + Digits + Special Characters")
            choice = input("Enter your choice (1/2/3/4): ")
            if choice in self.complexity_levels:
                return self.complexity_levels[choice]
            else:
                print("Invalid choice, please select 1, 2, 3, or 4.")

    def get_length(self):
        while True:
            try:
                length = int(input("Enter the desired password length: "))
                if length < 6:
                    print("Password length should be at least 6 characters for better security.")
                else:
                    return length
            except ValueError:
                print("Please enter a valid integer for the password length.")

    def run(self):
        print("Password Generator")
        length = self.get_length()
        complexity = self.get_complexity()
        password = self.generate_password(length, complexity)
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()


