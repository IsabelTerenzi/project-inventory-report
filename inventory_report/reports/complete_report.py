from collections import Counter
from typing import List, Dict
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    def generate(lista: List[Dict]) -> str:
        simple_report = SimpleReport.generate(lista)

        # https://realpython.com/python-counter/
        prod_estoque = Counter(product["nome_da_empresa"] for product in lista)
        estoque = ""
        for empresa, quantidade in prod_estoque.items():
            estoque += (f"- {empresa}: {quantidade}\n")

        return (
          f"{simple_report}\n"
          f"Produtos estocados por empresa:\n"
          f"{estoque}"
        )
