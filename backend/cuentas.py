from pandas.core.frame import DataFrame
from backend import Configs
from backend import Exceptions
from datetime import datetime
import pandas as pd

# TODO: Cada accion replicada a base de datos o guardar todo al finalizar
class Cuentas:
    COLUMNS_COMPRAS = ['material', 'kg', 'pagado']
    COLUMNAS_VENTAS = ['material', 'kg', 'recibido']

    def __init__(self, configs: Configs):
        self._configs = configs
        self._date = datetime
        self._df_compras = pd.DataFrame(columns=self.COLUMNS_COMPRAS)
        self._df_ventas = pd.DataFrame(columns=self.COLUMNAS_VENTAS)

    @property
    def compras(self) -> DataFrame:
        return self._df_compras
    
    @property
    def ventas(self) -> DataFrame:
        return self._df_ventas

    @property
    def compras_totales(self) -> DataFrame:
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
    def ventas_totales(self) -> DataFrame:
        # TODO: Crear tabla de totales ventas
        pass

    def add_compra(self, material, kg, pagado):
        '''No submateriales'''
        try:
            self._validate_values(material, kg, pagado)
        except:
            raise

        row = [material, kg, pagado]
        df_row = pd.DataFrame([row], columns=self.COLUMNS_COMPRAS)
        self._df_compras = self._df_compras.append(df_row, ignore_index=True)
        
    def update_compra(self):
        pass

    def delete_compra(self):
        pass

    def add_venta(self):
        pass

    def update_venta(self):
        pass

    def delete_venta(self):
        pass

    def _validate_values(self, material: str, kg: float, money: float):
        # Material exists
        if material not in self._configs.materiales['name'].to_list():
            raise Exceptions.MATERIAL_NO_EXISTS

        if kg < 0 or money < 0:
            raise Exceptions.VALUE_LESS_ZERO