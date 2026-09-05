estoque = [
    {"id": 1, "nome": "Senhor dos Anéis", "quantidade": 10, "preco": 150.00},
    {"id": 2, "nome": "Arquitetura de Software", "quantidade": 15, "preco": 300.00},
    {"id": 3, "nome": "Pequeno Príncipe", "quantidade": 2, "preco": 80.00}
]

estoque.append({"id": len(estoque)+1, "nome": "1984", "quantidade": 5, "preco": 100.00})

print(estoque[1]["nome"])