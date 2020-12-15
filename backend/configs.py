from datetime import date, datetime
import json

class Configs:
    def __init__(self):
        self._data = {}
        self._data['excel_path'] = ''
        self._data['last_save'] = None #datetime
        self._data['current_line'] = 1
        self._data['materiales'] = []
        self.saved = False

    @property
    def materiales(self) -> list:
        return self._data['materiales']

    @property
    def current_line(self) -> str:
        return self._data['current_line']

    @property
    def last_save(self) -> datetime:
        if self._data['last_save'] == None:
            return None
        else:
            return json.dumps(self._data['last_save'])

    def add_material(self, name: str, sale_price: float = 0, buy_price: float = 0, parent: str = None):
        # Precios no negativos
        if sale_price < 0 or buy_price < 0:
            raise ValueError("Prices can not be less than zero")

        # Verificar que no se repita el nombre y validar que hay padre
        parent_index = -1
        for i, material in enumerate(self._data['materiales']):
            if material['name'] == name:
                raise ValueError("Material already exists" )
            if parent != None and material['name'] == parent:
                parent_index = i

        material = {
            'name': name,
            'sale_price': sale_price,
            'buy_price': buy_price,
        }

        # Si father, agregarlo como sub material
        if parent != None:
            if parent_index == -1:
                raise ValueError("Parent doesn't exist")
            else:
                # Agregar material como hijo
                if 'children' not in self._data['materiales'][parent_index].keys():
                    self._data['materiales'][parent_index]['children'] = []
                self._data['materiales'][parent_index]['children'].append(material)
        else:
            # Agregar material
            self._data['materiales'].append(material)

        # Precio de compra menor que venta?? puede haber exccepciones

    # Archivo tipo json
    def save(self, path: str):
        self._data['last_save'] = datetime.now().isoformat()
        try:
            with open(path, 'w') as outfile:
                json.dump(self._data, outfile, indent=2)
        except:
            raise

    def load(self, path: str):
        # TODO: Validar variables y datos no corruptos y completos
        try:
            with open(path) as json_file:
                self._data = json.load(json_file)
        except:
            raise