from typing import Literal
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter


class Inventory:
    @staticmethod
    def import_data(path: str, type: Literal["simples", "completo"]):
        if "csv" in path:
            result = CsvImporter.import_data(path)

        return (
            SimpleReport.generate(result)
            if type == "simples"
            else CompleteReport.generate(result)
        )
