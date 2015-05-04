import unittest
from runMe import ProduceWorkingHours

class testProduceWorkingHours(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_empty_input_string(self):
        obj = ProduceWorkingHours("")
        self.assertEqual(obj.nbrDaysWorked(), -1)
    
    def test_only_1_day_worked_from_any_string(self):
        obj = ProduceWorkingHours("any thing here")
        self.assertEqual(obj.nbrDaysWorked(), 1)
    
    def test_only_1_day_worked_form_simple_8hours_day_string_correctly_formated(self):
        obj = ProduceWorkingHours("11: 8h")
        self.assertEqual(obj.nbrDaysWorked(), 1)
        
    def test_simle_2_days_worked_with_simple_8hours_day_string_correctly_formated(self):
        input_string = "20: 8h\n19: 8h"
        obj = ProduceWorkingHours(input_string)
        self.assertEqual(obj.nbrDaysWorked(), 2)
        
    def test_simle_2_days_worked_plus_empty_string_with_simple_8hours_day_string_correctly_formated(self):
        input_string = "20: 8h\n19: 8h\n"
        obj = ProduceWorkingHours(input_string)
        self.assertEqual(obj.nbrDaysWorked(), 2)

    

if __name__ == "__main__":
    unittest.main()
    
    
    
# to run test
# >> python produce_working_hours_test.py -v