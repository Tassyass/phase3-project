# test_blood_donation_system.py
import unittest
from blood_donation_system import BloodDonationSystem

class TestBloodDonationSystem(unittest.TestCase):
    def setUp(self):
        self.blood_donation_system = BloodDonationSystem()

    def test_add_donor(self):
        self.blood_donation_system.session.query(self.blood_donation_system.Donor).delete()
        self.blood_donation_system.session.query(self.blood_donation_system.BloodType).delete()
        self.blood_donation_system.session.commit()

        self.blood_donation_system.run('1\nJohn\nA\n2\n')
        donor = self.blood_donation_system.session.query(self.blood_donation_system.Donor).first()
        self.assertEqual(donor.name, 'John')
        self.assertEqual(donor.blood_type.blood_type, 'A')

    def tearDown(self):
        self.blood_donation_system.session.query(self.blood_donation_system.Donor).delete()
        self.blood_donation_system.session.query(self.blood_donation_system.BloodType).delete()
        self.blood_donation_system.session.commit()

if __name__ == '__main__':
    unittest.main()
