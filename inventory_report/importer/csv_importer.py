import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path: str):
        with open(path, encoding="utf-8") as file:
            if "csv" not in path:
                raise ValueError("Arquivo inválido")
            else:
                result = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(result)
