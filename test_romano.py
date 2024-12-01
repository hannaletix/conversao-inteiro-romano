import unittest
from romano import inteiro_para_romano

class TestConversaoInteiroParaRomano(unittest.TestCase):
    def test_1_para_I(self):
        self.assertEqual(inteiro_para_romano(1), "I")
    
    def test_4_para_IV(self):
        self.assertEqual(inteiro_para_romano(4), "IV")
    
    def test_9_para_IX(self):
        self.assertEqual(inteiro_para_romano(9), "IX")
    
    def test_10_para_X(self):
        self.assertEqual(inteiro_para_romano(10), "X")
    
    def test_40_para_XL(self):
        self.assertEqual(inteiro_para_romano(40), "XL")
    
    def test_90_para_XC(self):
        self.assertEqual(inteiro_para_romano(90), "XC")
    
    def test_400_para_CD(self):
        self.assertEqual(inteiro_para_romano(400), "CD")
    
    def test_900_para_CM(self):
        self.assertEqual(inteiro_para_romano(900), "CM")
    
    def test_3999_para_MMMCMXCIX(self):
        self.assertEqual(inteiro_para_romano(3999), "MMMCMXCIX")

# Testes de uso direto fora do escopo de unittest
if __name__ == "__main__":
    print(inteiro_para_romano(1))    # Saída: "I"
    print(inteiro_para_romano(4))    # Saída: "IV"
    print(inteiro_para_romano(58))   # Saída: "LVIII"
    print(inteiro_para_romano(3999)) # Saída: "MMMCMXCIX"
