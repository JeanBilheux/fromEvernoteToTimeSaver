import unittest
from runMe import ProduceWorkingHours

class testProduceWorkingHours(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_empty_input_string(self):
        obj = ProduceWorkingHours("")
        self.assertEqual(obj.nbrDaysWorked(), -1)
        
    def test_wrong_none_empty_string_format(self):
        obj = ProduceWorkingHours("any thing here")
        self.assertEqual(obj.nbrDaysWorked(), 0)

    def test_nbr_days_worked_for_simple_1_day_worked(self):
        obj = ProduceWorkingHours("11: 8h")
        self.assertEqual(obj.nbrDaysWorked(), 1)
        
    def test_nbr_hours_worked_for_simple_1_day_worked(self):
        obj = ProduceWorkingHours("11: 8h")
        self.assertListEqual(obj.listHoursWorked(), ['8'])
        
    def test_nbr_days_worked_for_simple_2_days_worked(self):
        input_string = "20: 8h\n19: 8h"
        obj = ProduceWorkingHours(input_string)
        self.assertEqual(obj.nbrDaysWorked(), 2)
        
    def test_nbr_days_worked_for_simple_2_days_worked_plus_empty_line(self):
        input_string = "20: 8h\n19: 8h\n"
        obj = ProduceWorkingHours(input_string)
        self.assertEqual(obj.nbrDaysWorked(), 2)

    def test_nbr_hours_worked_for_simple_2_days_worked(self):
        input_string = "20: 8h\n19: 9h"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['8','9'])
    
    def test_nbr_hours_worked_for_simple_2_days_worked_plus_empty_line(self):
        input_string = "20: 8h\n19: 9h\n"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['8','9'])
        
    def test_nbr_hours_worked_for_complex_1_day_worked(self):
        input_string = "5: 8:30->4:30"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['8.0'])
    
    def test_nbr_hours_worked_for_complex_1_day_worked_with_plus_half_h(self):
        input_string = "5: 8:30->4:30 + .5h"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['8.5'])
    
    def test_nbr_hours_worked_for_complex_1_day_worked_with_plus_one_and_halfh(self):
        input_string = "5: 8:30->4:30 + 1.5h"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['9.5'])

    def test_nbr_hours_worked_for_complex_1_day_worked_with_minus_half_h(self):
        input_string = "5: 8:30->4:30 - .5h"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['7.5'])
    
    def test_nbr_hours_worked_for_complex_1_day_worked_with_minus_one_and_halfh(self):
        input_string = "5: 8:30->4:30 - 1.5h"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['6.5'])

    def test_nbr_hours_worked_for_complex_1_day_worked_with_plus_and_minus_h(self):
        input_string = "5: 8:30->4:30 - .5h + 1h"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['8.5'])

    def test_nbr_hours_worked_for_complex_2_days_worked_with_plus_and_minus_h(self):
        input_string = "5: 8:30->4:30 - .5h + 1h\n 4: 8:30->5:30 - .5h + .5h"
        obj = ProduceWorkingHours(input_string)
        self.assertListEqual(obj.listHoursWorked(), ['8.5','9.0'])

if __name__ == "__main__":
    unittest.main()
    
# to run test
# >> python produce_working_hours_test.py -v