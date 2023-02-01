import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path: str):
        with open(path, encoding="utf-8") as file:
            if "xml" not in path:
                raise ValueError("Arquivo inválido")
            else:
                result = xmltodict.parse(file.read())['dataset']['record']
            return result
