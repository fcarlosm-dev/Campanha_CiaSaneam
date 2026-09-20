# Programa para classificação de perfil de consumo dos imóveis

#Definição dos blocos do código

#Agrupamento do código
def classificar_consumo():

    #Apresenta em tela menu de opções para o usuário informar qual o tipo de imóvel
    print("=== CLASSIFICAÇÃO DE CONSUMO DE ÁGUA ===")
    print("Tipo de imóvel:")
    print("1 - Comercial")
    print("2 - Casa")
    print("3 - Apartamento")

#Leitura e validação de entrada das informações
    try:
        opcao = int(input("Informe o tipo de imóvel (1, 2 ou 3): "))
        consumo = float(input("Informe o consumo mensal em m³: ").replace(",", "."))
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        return

#Valida se o valor informado é coerente, não podendo ser negativo. 
    if consumo < 0:
        print("O consumo não pode ser negativo.")
        return

#Conversão da opção numérica em texto utilizando as variáveis Se, Senão Se e Senão.
    if opcao == 1:
        tipo = "comercial"
    elif opcao == 2:
        tipo = "casa"
    elif opcao == 3:
        tipo = "apartamento"
    else:
        print("Opção de tipo de imóvel inválida.")
        return

#Regras de negócio/classificação
    if tipo == "comercial":
        mensagem = "Tarifa comercial aplicada – consulte o plano corporativo."

    elif tipo == "apartamento" and consumo < 10:
        mensagem = "Consumo econômico – excelente controle de água!"

    elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:
        mensagem = "Consumo moderado – dentro do padrão residencial."

    else:
        mensagem = "Consumo excessivo – adote medidas de economia e verifique vazamentos."

#Resultado
    print("\nClassificação:")
    print(mensagem)

#Verifica execução
if __name__ == "__main__":
    classificar_consumo()