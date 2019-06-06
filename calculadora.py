import unittest
from calculadora import Calculadora

class testCalculadora(unittest.testCal):

	def test_de_una_calculadora_inicia_en_cero(self):
		clac = Calculadora()
		self.assertEquial(0,calc.valor)
