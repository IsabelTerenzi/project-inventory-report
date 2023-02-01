from collections import Counter
# https://realpython.com/python-counter/
from typing import List, Dict
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    def generate(lista: List[Dict]) -> str:
        simple_report = SimpleReport.generate(lista)

        prod_estoque = Counter(product["nome_da_empresa"] for product in lista)
        stock = ""
        for empresa, quantidade in prod_estoque.items():
            stock += (f"- {empresa}: {quantidade}\n")

        return (
          f"{simple_report}\n"
          f"Produtos estocados por empresa:\n"
          f"{stock}"
        )
