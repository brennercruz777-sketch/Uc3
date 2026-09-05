valor_total = 10.0
saldo_usuario = 9.0
pergunta=input("Você tem cupom? s/n\n")
if pergunta == "s":
    cupom_valido = True
else:
    cupom_valido = False

if cupom_valido:
    #valor_total = valor_total * 0.9
    valor_total *= 0.9

if saldo_usuario>=valor_total:
    print("201 Created - Pedido realizado com sucesso")
else:
    print("402 Payment Required - Saldo insuficiente")