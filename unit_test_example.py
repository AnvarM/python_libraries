import calc
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10,5)
        self.assertEquals(result,15)
        
    def test_subt(self):
        result = calc.subt(10,5)
        self.assertEquals(result,5)

    def test_mult(self):
        result = calc.mult(10,5)
        self.assertEquals(result,50)
        
    def test_div(self):
        result = calc.div(10,5)
        self.assertEquals(result,2)

    def test_pow(self):
        result = calc.pow(10,5)
        self.assertEquals(result,100000)        
            

if __name__ == '__main__': 
    unittest.main() 