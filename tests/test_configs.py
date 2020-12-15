import unittest
from backend import Configs, configs

class TestConfigs(unittest.TestCase):
    def setUp(self) -> None:
        self.configs = Configs()
        self.configs.add_material('Chatarra', 6, 5)
        self.configs.add_material('Aluminio', 22, 19)
        self.configs.add_material('Delgado', 20, 18, 'Aluminio') #child
        self.configs.add_material('Grueso', 24, 22, 'Aluminio') #child
        self.len = len(self.configs.materiales)
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_add_material(self):
        self.assertEqual(len(self.configs.materiales), 2)
        self.assertEqual(len(self.configs.materiales[1]['children']), 2)
        pass

    def test_add_material_wrong_prices(self):
        exception_expected = "Prices can not be less than zero"

        with self.assertRaises(ValueError) as exception_context:
            self.configs.add_material('Cobre', -1, 5)
        self.assertEqual(str(exception_context.exception), exception_expected)
        self.assertEqual(len(self.configs.materiales), self.len)#Mismo tamano

        with self.assertRaises(ValueError) as exception_context:
            self.configs.add_material('Cobre', 1, -5)
        self.assertEqual(str(exception_context.exception), exception_expected)
        self.assertEqual(len(self.configs.materiales), self.len)#Mismo tamano

    def test_add_material_already_exists(self):
        exception_expected = "Material already exists"
        with self.assertRaises(ValueError) as exception_context:
            self.configs.add_material('Chatarra', 6, 5)
        self.assertEqual(str(exception_context.exception), exception_expected)
        self.assertEqual(len(self.configs.materiales), self.len)#Mismo tamano

    def test_add_material_no_parent(self):
        exception_expected = "Parent doesn't exist"
        with self.assertRaises(ValueError) as exception_context:
            self.configs.add_material('Bote', parent='Amuminio')
        self.assertEqual(str(exception_context.exception), exception_expected)

    def test_save_and_load(self):
        self.configs.save('test.json')
        configs_loaded = Configs()
        configs_loaded.load('test.json')
        self.assertEqual(self.configs.last_save, configs_loaded.last_save)
        self.assertEqual(self.configs.materiales, configs_loaded.materiales)
        self.assertEqual(self.configs.current_line, configs_loaded.current_line)