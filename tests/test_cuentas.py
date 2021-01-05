from backend import Configs
import unittest
from backend import Cuentas

class TestCuentas(unittest.TestCase):
    def setUp(self) -> None:
        self.configs = Configs()
        self.configs.add_material('Chatarra', 6, 5)
        self.configs.add_material('Aluminio', 22, 19)
        self.configs.add_material('Delgado', 20, 18, 'Aluminio') #child
        self.configs.add_material('Grueso', 24, 22, 'Aluminio') #child

        self.cuentas = Cuentas(self.configs)
        self.cuentas.add_compra('Aluminio', 10, 200)
        self.cuentas.add_compra('Aluminio', 5, 100)
        self.cuentas.add_compra('Chatarra', 10, 45)

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_add_compra(self):
        # testing add_compra, compras, compras_totales
        self.assertEqual(len(self.cuentas.compras), 3)
        self.assertEqual(len(self.cuentas.compras_totales), 2)
