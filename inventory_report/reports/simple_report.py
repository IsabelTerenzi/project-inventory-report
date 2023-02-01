from statistics import mode
# https://www.w3schools.com/python/ref_stat_mode.asp
from typing import Dict, List


class SimpleReport:
    @staticmethod
    def generate(lista: List[Dict]) -> str:
        fab_antiga = min([product["data_de_fabricacao"] for product in lista])

        val_proxima = min([product["data_de_validade"] for product in lista])

        mais_produtos = mode([product["nome_da_empresa"] for product in lista])

        return (
           f"Data de fabricação mais antiga: {fab_antiga}\n"
           f"Data de validade mais próxima: {val_proxima}\n"
           f"Empresa com mais produtos: {mais_produtos}\n"
        )
