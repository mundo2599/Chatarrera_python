import unittest

from backend import Exceptions, Configs, Cuentas, cuentas

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
        self.len_compras = len(self.cuentas.compras)

        self.cuentas.add_venta('Aluminio', 10, 30)
        self.cuentas.add_venta('Delgado', 10, 25)
        self.cuentas.add_venta('Chatarra', 10, 60)
        self.len_ventas = len(self.cuentas.ventas)

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_add_compra(self):
        # testing add_compra, compras, compras_totales
        self.assertEqual(len(self.cuentas.compras), 3)
        self.assertEqual(len(self.cuentas.compras_totales), 2)

        # material no existe, excepction y verificar que no se agrego
        with self.assertRaises(ValueError) as exception_context:
            self.cuentas.add_compra('Cobre', 10, 10)
        self.assertEqual(str(exception_context.exception), str(Exceptions.MATERIAL_NO_EXISTS))
        self.assertEqual(self.len_compras, len(self.cuentas.compras))
        
        print(self.cuentas.compras)
        print(self.cuentas.compras_totales)
        

    def test_add_venta(self):
        # testing add_venta, ventas, ventas_totales
        self.assertEqual(len(self.cuentas.ventas), 3)
        self.assertEqual(len(self.cuentas.ventas_totales), 2)

        # material no existe, excepction y verificar que no se agrego
        with self.assertRaises(ValueError) as exception_context:
            self.cuentas.add_venta('Cobre', 10, 10)
        self.assertEqual(str(exception_context.exception), str(Exceptions.MATERIAL_NO_EXISTS))
        self.assertEqual(self.len_ventas, len(self.cuentas.ventas))

        print(self.cuentas.ventas)
        print(self.cuentas.ventas_totales)

    def test_validate_values(self):
        # Material child correcto
        res = self.cuentas._validate_values('Delgado', 10, 10)
        self.assertEqual(res, True)

        # Material correcto
        res = self.cuentas._validate_values('Aluminio', 10, 10)
        self.assertEqual(res, True)

        # Material no existente
        with self.assertRaises(ValueError) as exception_context:
            self.cuentas._validate_values('Cobre', 10, 10)
        self.assertEqual(str(exception_context.exception), str(Exceptions.MATERIAL_NO_EXISTS))
        
        # material child como parametro pero no acepta child
        with self.assertRaises(ValueError) as exception_context:
            self.cuentas._validate_values('Delgado', 10, 10, include_subs=False)
        self.assertEqual(str(exception_context.exception), str(Exceptions.CHILD_NO_VALID))

        # kg negativo
        with self.assertRaises(ValueError) as exception_context:
            self.cuentas._validate_values('Aluminio', -1, 10)
        self.assertEqual(str(exception_context.exception), str(Exceptions.VALUE_LESS_ZERO))

