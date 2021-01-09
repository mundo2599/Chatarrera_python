import unittest

from backend import Exceptions, Configs

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
        self.assertEqual(len(self.configs.materiales), 4)
        self.assertEqual(len(self.configs.materiales_no_children), 2)
        self.assertEqual(len(self.configs.material_children(name='Aluminio')), 2)

    def test_add_material_wrong_prices(self):
        with self.assertRaises(ValueError) as exception_context:
            self.configs.add_material('Cobre', -1, 5)
        self.assertEqual(str(exception_context.exception), str(Exceptions.VALUE_LESS_ZERO))
        self.assertEqual(len(self.configs.materiales), self.len)#Mismo tamano

        with self.assertRaises(ValueError) as exception_context:
            self.configs.add_material('Cobre', 1, -5)
        self.assertEqual(str(exception_context.exception), str(Exceptions.VALUE_LESS_ZERO))
        self.assertEqual(len(self.configs.materiales), self.len)#Mismo tamano

    def test_add_material_already_exists(self):
        with self.assertRaises(ValueError) as exception_context:
            self.configs.add_material('Chatarra', 6, 5)
        self.assertEqual(str(exception_context.exception), str(Exceptions.MATERIAL_EXISTS))
        self.assertEqual(len(self.configs.materiales), self.len)#Mismo tamano

    def test_add_material_no_parent(self):
        with self.assertRaises(ValueError) as exception_context:
            self.configs.add_material('Bote', parent='Amuminio')
        self.assertEqual(str(exception_context.exception), str(Exceptions.PARENT_NO_EXISTS))

    def test_save_and_load(self):
        self.configs.save('test.json')
        configs_loaded = Configs()
        configs_loaded.load('test.json')
        self.assertEqual(self.configs.last_save, configs_loaded.last_save)
        self.assertEqual(self.configs.materiales.values.tolist(), configs_loaded.materiales.values.tolist())
        self.assertEqual(self.configs.current_line, configs_loaded.current_line)

    def test_get_material(self):
        # Por nombre
        material = self.configs.material(name='Aluminio')
        self.assertEqual(material['name'], 'Aluminio')

        # Por index
        material = self.configs.material(index=1)
        self.assertEqual(material['name'], 'Aluminio')
        self.assertEqual(material['index'], 1)

        # no parametros
        with self.assertRaises(ValueError) as exception_context:
            self.configs.material()
        self.assertEqual(str(Exceptions.NO_PARAMETERS), str(exception_context.exception))

        # Nombre no existe
        with self.assertRaises(ValueError) as exception_context:
            self.configs.material(name='some_material')
        self.assertEqual(str(Exceptions.MATERIAL_NO_EXISTS), str(exception_context.exception))

        # Index no encontrado
        with self.assertRaises(ValueError) as exception_context:
            self.configs.material(index=-1)
        self.assertEqual(str(Exceptions.MATERIAL_NO_EXISTS), str(exception_context.exception))

    def test_get_material_children(self):
        # Por nombre
        material, children = self.configs.material_children(name='Aluminio')
        self.assertEqual(material['name'], 'Aluminio')
        self.assertEqual(len(children), 2)

        # Por index
        material, children = self.configs.material_children(index=0)
        self.assertEqual(material['index'], 0)
        self.assertEqual(material['name'], 'Chatarra')
        self.assertEqual(len(children), 0)

        # Nombre no existe
        with self.assertRaises(ValueError) as exception_context:
            self.configs.material(name='some_material')
        self.assertEqual(str(Exceptions.MATERIAL_NO_EXISTS), str(exception_context.exception))

        # Index no encontrado
        with self.assertRaises(ValueError) as exception_context:
            self.configs.material(index=-1)
        self.assertEqual(str(Exceptions.MATERIAL_NO_EXISTS), str(exception_context.exception))
