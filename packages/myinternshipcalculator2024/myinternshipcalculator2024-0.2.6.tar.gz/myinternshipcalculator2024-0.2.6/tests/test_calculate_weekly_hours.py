import unittest
from myinternshipcalculator2024.calculator import calculate_weekly_hours

class TestCalculateWeeklyHours(unittest.TestCase):
    def test_calculate_weekly_hours(self):
        result = calculate_weekly_hours(7)
        self.assertEqual(result, 7*5)

    def test_calculate_weekly_hours_zero(self):
        result = calculate_weekly_hours(0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()