from inventory_report.inventory.product import Product


def test_cria_produto():
    mockProduct = Product(
       id=1,
       nome_do_produto="Vinho",
       nome_da_empresa="Wine",
       data_de_fabricacao="2023-01-31",
       data_de_validade="2023-03-31",
       numero_de_serie=1606,
       instrucoes_de_armazenamento="em ambiente arejado"
    )

    assert mockProduct.id == 1
    assert mockProduct.nome_do_produto == "Vinho"
    assert mockProduct.nome_da_empresa == "Wine"
    assert mockProduct.data_de_fabricacao == "2023-01-31"
    assert mockProduct.data_de_validade == "2023-03-31"
    assert mockProduct.numero_de_serie == 1606
    assert mockProduct.instrucoes_de_armazenamento == "em ambiente arejado"
