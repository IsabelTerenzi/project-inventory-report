from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path: str):
        with open(path, encoding="utf-8") as file:
            if "json" not in path:
                raise ValueError("Arquivo inválido")
            else:
                result = json.loads(file)
            return list(result)
