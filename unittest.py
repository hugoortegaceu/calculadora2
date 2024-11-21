import unittest
 
class TestCalculadora(unittest.TestCase):
  def setUp(self):
    self.calculadora = Calculadora()
 
  def test_sumar(self):
    self.assertEqual(self.calculadora.sumar(2, 3), 5)
 
  def test_restar(self):
    self.assertEqual(self.calculadora.restar(5, 3), 2)
 
  def test_multiplicar(self):
    self.assertEqual(self.calculadora.multiplicar(4, 2), 8)
 
  def test_dividir(self):
    self.assertEqual(self.calculadora.dividir(10, 2), 5)
    with self.assertRaises(ValueError):
      self.calculadora.dividir(5, 0)