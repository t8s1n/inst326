class StudentProfile:
    def __init__(self):
        self.name = ""
        self.major = ""
        self.strengths = []
        self.weaknesses = []
        self.prospect_companies = []
        self.industry_preferences = []

    def create_profile(self):
        print("Creating Student Profile\n------------------------")
        self.name = input("Enter your name: ")
        self.major = input("Enter your major: ")
        self.strengths = input("Enter your strengths (WARNING: make sure it is comma-separated): ").split(',')
        self.weaknesses = input("Enter your weaknesses (WARNING: make sure it is comma-separated): ").split(',')
        self.prospect_companies = input(
            "Enter your prospect companies (WARNING: make sure it is comma-separated): ").split(',')
        self.industry_preferences = input(
            "Enter your industry preferences (WARNING: make sure it is comma-separated): ").split(',')

    def display_profile(self):
        print("\nStudent Profile\n---------------")
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")
        print(f"Strengths: {', '.join(self.strengths)}")
        print(f"Weaknesses: {', '.join(self.weaknesses)}")
        print(f"Prospect Companies: {', '.join(self.prospect_companies)}")
        print(f"Industry Preferences: {', '.join(self.industry_preferences)}")


if __name__ == "__main__":
    student = StudentProfile()
    student.create_profile()
    student.display_profile()

