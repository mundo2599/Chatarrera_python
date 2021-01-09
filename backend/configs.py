from backend import Exceptions

from typing import Dict, Tuple
from datetime import datetime
import pandas as pd
import json

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

    # PROPERTIES
    @property
    def materiales(self) -> pd.DataFrame:
        return self._df_materiales

    @property
    def materiales_no_children(self) -> pd.DataFrame:
        return self._df_materiales[self._df_materiales['parent'].isnull()]

    def material(self, name: str = None, index: str = None) -> Dict:
        """Use only one parameter"""
        material = pd.DataFrame()
        if name != None:
            material = self._df_materiales[self._df_materiales['name'] == name]
        elif index != None:
            try:
                material = self._df_materiales.loc[[index]] # Doble corchete para que regrese un df
            except:
                pass
        else:
            raise Exceptions.NO_PARAMETERS

        if len(material) == 0:
            raise Exceptions.MATERIAL_NO_EXISTS
        else:
            map_material = material.to_dict('records')[0]
            map_material['index'] = material.index
            return map_material

    def material_children(self, name: str = None, index: str = None) -> Tuple[Dict, pd.DataFrame]:
        """
        Use only one parameter.
        Returns Tuple with parent as Map and children as DataFrame
        """
        try:
            material = self.material(name=name, index=index)
        except:
            raise
        
        children = self.materiales[self._df_materiales['parent'] == material['name']]
        return material, children

    @property
    def current_line(self) -> str:
        return self._data['current_line']

    @property
    def last_save(self) -> datetime:
        if self._data['last_save'] == None:
            return None
        else:
            return json.dumps(self._data['last_save'])

    # FUNCTIONS
    def add_material(self, name: str, sale_price: float = 0, buy_price: float = 0, parent: str = None):
        # Precios no negativos
        if sale_price < 0 or buy_price < 0:
            raise Exceptions.VALUE_LESS_ZERO

        # Verificar que no se repita el nombre
        if name in self._df_materiales['name'].values:
            raise Exceptions.MATERIAL_EXISTS

        # validar que hay padre
        if parent != None and parent not in self._df_materiales['name'].values:
            raise Exceptions.PARENT_NO_EXISTS

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