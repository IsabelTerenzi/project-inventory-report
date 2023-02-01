from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mockProduct = Product(
        id=1,
        nome_do_produto="Vinho",
        nome_da_empresa="Wine",
        data_de_fabricacao="2023-01-31",
        data_de_validade="2023-03-31",
        numero_de_serie=1606,
        instrucoes_de_armazenamento="em ambiente arejado",
    )

    assert str(mockProduct.__repr__()) == f"O produto {mockProduct.nome_do_produto}\
 fabricado em {mockProduct.data_de_fabricacao} por\
 {mockProduct.nome_da_empresa} com validade até\
 {mockProduct.data_de_validade} precisa ser armazenado\
 {mockProduct.instrucoes_de_armazenamento}."
