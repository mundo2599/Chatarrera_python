import pandas as pd
from datetime import datetime

from backend import Configs
from backend import Exceptions

# TODO: Cada accion replicada a base de datos o guardar todo al finalizar
class Cuentas:
    '''Clase para guardar compras y ventas hechas en un cierto periodo 
    de tiempo'''

    COLUMNS_COMPRAS = ['material', 'kg', 'pagado']
    COLUMNAS_VENTAS = ['material', 'kg', 'recibido']

    def __init__(self, configs: Configs):
        self._configs = configs
        self._date = datetime
        self._df_compras = pd.DataFrame(columns=self.COLUMNS_COMPRAS)
        self._df_ventas = pd.DataFrame(columns=self.COLUMNAS_VENTAS)

    @property
    def compras(self) -> pd.DataFrame:
        return self._df_compras
    
    @property
    def ventas(self) -> pd.DataFrame:
        return self._df_ventas

    @property
    def compras_totales(self) -> pd.DataFrame:
        compras_totales = pd.DataFrame(columns=self.COLUMNS_COMPRAS)
        # Por cada material parent
        for material in self._configs.materiales_no_children['name'].to_list():
            df_material = self._df_compras[self._df_compras['material'] == material]
            # Sumar de df_compras todos los kg y pagado de material
            kg = df_material['kg'].sum()
            pagado = df_material['pagado'].sum()
            row = [material, kg, pagado]
            df_row = pd.DataFrame([row], columns=self.COLUMNS_COMPRAS)
            # Agregar fila a nuevo df
            compras_totales = compras_totales.append(df_row, ignore_index=True)

        return compras_totales

    @property
    def ventas_totales(self) -> pd.DataFrame:
        '''Suma de ventas por material'''
        ventas_totales = pd.DataFrame(columns=self.COLUMNAS_VENTAS)
        # Por cada material parent
        for material in self._configs.materiales_no_children['name'].to_list():
            _, children = self._configs.material_children(name=material)
            # Agregar ventas que coincidan con el material o que sean submateriales
            df_material = self._df_ventas[
                (self._df_ventas['material'] == material) | 
                (self._df_ventas['material'].isin(children['name'].to_list()))
            ]

            # Sumar de df_compras todos los kg y recibido de material
            kg = df_material['kg'].sum()
            recibido = df_material['recibido'].sum()
            row = [material, kg, recibido]
            df_row = pd.DataFrame([row], columns=self.COLUMNAS_VENTAS)
            # Agregar fila a nuevo df
            ventas_totales = ventas_totales.append(df_row, ignore_index=True)
        
        return ventas_totales

    def add_compra(self, material, kg, pagado):
        '''No submateriales'''
        try:
            self._validate_values(material, kg, pagado, False)
        except:
            raise

        row = [material, kg, pagado]
        df_row = pd.DataFrame([row], columns=self.COLUMNS_COMPRAS)
        self._df_compras = self._df_compras.append(df_row, ignore_index=True)
        
    def update_compra(self):
        pass

    def delete_compra(self):
        pass

    def add_venta(self, material, kg, pagado):
        try:
            self._validate_values(material, kg, pagado)
        except:
            raise

        row = [material, kg, pagado]
        df_row = pd.DataFrame([row], columns=self.COLUMNAS_VENTAS)
        self._df_ventas = self._df_ventas.append(df_row, ignore_index=True)

    def update_venta(self):
        pass

    def delete_venta(self):
        pass

    def _validate_values(self, material: str, kg: float, money: float, include_subs=True) -> bool:
        # Material exists
        exists = False
        is_sub = False

        if material in self._configs.materiales['name'].to_list():
            # exists
            if material not in self._configs.materiales_no_children['name'].to_list():
                # is_sub
                if not include_subs:
                    raise Exceptions.CHILD_NO_VALID
        else:
            raise Exceptions.MATERIAL_NO_EXISTS
            

        if kg < 0 or money < 0:
            raise Exceptions.VALUE_LESS_ZERO

        return True