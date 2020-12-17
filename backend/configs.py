from datetime import datetime
import pandas as pd
import json

from pandas.core.frame import DataFrame

class Configs:
    COLUMNS_MATERIALES = ['name', 'sale_price', 'buy_price', 'parent']

    def __init__(self):
        self._data = {}
        self._data['excel_path'] = ''
        self._data['last_save'] = None #datetime
        self._data['materiales'] = None #array, se usa al guardar y cargar

        # Last_date y current_line estan en la misma fila en excel
        self._data['last_date'] = None #datetime
        self._data['current_line'] = 1

        self._df_materiales = pd.DataFrame(columns=self.COLUMNS_MATERIALES)

    @property
    def materiales(self) -> DataFrame:
        return self._df_materiales

    @property
    def materiales_no_children(self) -> DataFrame:
        return self._df_materiales[self._df_materiales['parent'].isnull()]

    def material_children(self, name: str = None, id: str = None) -> DataFrame:
        """Use only one parameter"""
        if name:
            return self._df_materiales[self._df_materiales['parent'] == name]
        elif id:
            return self._df_materiales[self._df_materiales['parent'] == name]
        else:
            raise ValueError('No parameters provided')

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
            raise ValueError("Value can not be less than zero")

        # Verificar que no se repita el nombre
        if name in self._df_materiales['name'].values:
            raise ValueError("Material already exists")

        # validar que hay padre
        if parent != None and parent not in self._df_materiales['name'].values:
            raise ValueError("Parent doesn't exist")

        # Agregar material a df
        row = [name, sale_price, buy_price, parent]
        df_row = pd.DataFrame([row], columns=self.COLUMNS_MATERIALES)
        self._df_materiales = pd.concat([self._df_materiales, df_row], ignore_index=True)

        # Precio de compra menor que venta?? puede haber exccepciones

    # Archivo tipo json
    def save(self, path: str):
        self._data['last_save'] = datetime.now().isoformat()
        self._data['materiales'] = self._df_materiales.values.tolist()
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
            self._df_materiales = pd.DataFrame(self._data['materiales'], columns=self.COLUMNS_MATERIALES)
        except:
            raise