import unittest
from student_matching_process import matched_company_profile


class test_matching_company_profile(unittest.TestCase):

    def setUp(self):
        self.profile = matched_company_profile()

    def test_matching_companies(self):
        self.profile.student_name = "John"
        self.profile.company_name = "Dell"
        self.profile.industry = "Technology"
        self.profile.location = "Cupertino, California, USA"
        self.profile.ceo = "Tim Cook"
        self.profile.headquarters = "Cupertino, California, USA"
        self.profile.specialty = "Consumer electronics, software"

        matches = self.profile.find_matching_companies()
        self.assertIn("Apple Inc.", [match["Name"] for match in matches])

    def test_no_matching_companies(self):
        self.profile.student_name = "John"
        self.profile.company_name = "Unknown"
        self.profile.industry = "Unknown Industry"
        self.profile.location = "Unknown Location"
        self.profile.ceo = "Unknown CEO"
        self.profile.headquarters = "Unknown Headquarters"
        self.profile.specialty = "Unknown Specialty"

        matches = self.profile.find_matching_companies()
        self.assertEqual(len(matches), 0)


if __name__ == '__main__':
    unittest.main()
