import unittest
from restaraunts import solution

class RestarauntsTest(unittest.TestCase):

    def test_first(self):

        input = [
                ["Shogun", "Tapioca Express", "Burger King", "KFC"], 
                ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
                ]
        output = ["Shogun"]
        result = solution(*input)
        self.assertEqual(result,output)
    
    def test_second(self):
        input = [
                ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                ["KFC", "Shogun", "Burger King"]
                ]
        output = ['Shogun']
        result = solution(*input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
        
