# Embedded company data
company_data = [
    {"Name": "Apple Inc.", "CEO": "Tim Cook", "Industry": "Technology",
     "Headquarters Location": "Cupertino, California, USA", "Specialty": "Consumer electronics, software"},
    {"Name": "Microsoft Corporation", "CEO": "Satya Nadella", "Industry": "Technology",
     "Headquarters Location": "Redmond, Washington, USA", "Specialty": "Software, hardware, cloud computing"},
    {"Name": "Amazon.com, Inc.", "CEO": "Andy Jassy", "Industry": "E-commerce, Technology",
     "Headquarters Location": "Seattle, Washington, USA",
     "Specialty": "E-commerce, cloud computing, digital streaming"},
    {"Name": "Google (Alphabet Inc.)", "CEO": "Sundar Pichai", "Industry": "Technology",
     "Headquarters Location": "Mountain View, California, USA",
     "Specialty": "Search engine, cloud computing, software"},
    {"Name": "Facebook, Inc. (Meta Platforms, Inc.)", "CEO": "Mark Zuckerberg", "Industry": "Social Media, Technology",
     "Headquarters Location": "Menlo Park, California, USA", "Specialty": "Social networking"},
    {"Name": "Tesla, Inc.", "CEO": "Elon Musk", "Industry": "Automotive, Energy",
     "Headquarters Location": "Palo Alto, California, USA", "Specialty": "Electric vehicles, energy storage"},
    {"Name": "NVIDIA Corporation", "CEO": "Jensen Huang", "Industry": "Technology",
     "Headquarters Location": "Santa Clara, California, USA", "Specialty": "Graphics processing units (GPUs)"},
    {"Name": "Netflix, Inc.", "CEO": "Reed Hastings", "Industry": "Entertainment, Technology",
     "Headquarters Location": "Los Gatos, California, USA", "Specialty": "Streaming media"},
    {"Name": "Adobe Inc.", "CEO": "Shantanu Narayen", "Industry": "Software",
     "Headquarters Location": "San Jose, California, USA", "Specialty": "Multimedia and creativity software"},
    {"Name": "Intel Corporation", "CEO": "Pat Gelsinger", "Industry": "Technology",
     "Headquarters Location": "Santa Clara, California, USA", "Specialty": "Semiconductors"}
]


class preffered_company_matches:
    def __init__(self):
        self.student_name = ""
        self.company_name = ""
        self.industry = ""
        self.location = ""
        self.ceo = ""
        self.headquarters = ""
        self.specialty = ""

    def capture_profile(self):
        print("Enter Student's Preferred Company Profile\n----------------------------------------")
        self.student_name = input("Enter student's name: ")
        self.company_name = input("Enter preferred company name: ")
        self.industry = input("Enter company industry: ")
        self.location = input("Enter company location: ")
        self.ceo = input("Enter company CEO: ")
        self.headquarters = input("Enter company headquarters location: ")
        self.specialty = input("Enter company specialty: ")

    def display_profile(self):
        print("\nPreferred Company Profile\n-------------------------")
        print(f"Student Name: {self.student_name}")
        print(f"Company Name: {self.company_name}")
        print(f"Industry: {self.industry}")
        print(f"Location: {self.location}")
        print(f"CEO: {self.ceo}")
        print(f"Headquarters: {self.headquarters}")
        print(f"Specialty: {self.specialty}")


class matched_company_profile(preffered_company_matches):

    def find_matching_companies(self):
        matching_companies = []

        for company in company_data:
            if (self.industry.lower() in company["Industry"].lower() and
                    self.location.lower() in company["Location"].lower()):
                matching_companies.append(company)

        return matching_companies

    def display_matches(self, matches):
        if matches:
            print("\nMatching Companies\n------------------")
            for match in matches:
                print(match["Name"])
        else:
            print("\nSorry, there are no matches for your preferences. :(")


class matched_company_profile_class(matched_company_profile):

    def find_matching_companies(self):
        matching_companies = []

        for company in company_data:
            if (self.industry.lower() in company["Industry"].lower() and
                    self.location.lower() in company["Headquarters Location"].lower()):
                matching_companies.append(company)

        return matching_companies


def matching_company_process():
    profile = matched_company_profile_class()
    profile.capture_profile()
    matches = profile.find_matching_companies()
    profile.display_matches(matches)


if __name__ == "__main__":
    matching_company_process()
