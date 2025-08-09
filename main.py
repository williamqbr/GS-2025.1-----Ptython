
import time

usuarios = []
alertas = []
historico_enchentes = {
    "01001-000": ["2022-01-12", "2023-02-05"],
    "01310-000": ["2024-03-20"]
}
doacoes = []

def cadastrar_usuario():
    print("\n== Cadastro de Usuário ==")
    nome = input("Nome completo: ")
    email = input("E-mail: ")
    localizacao = input("CEP (somente números): ")
    risco = input("Perfil de risco (idoso, mobilidade reduzida, nenhum): ").lower()

    if not nome or not email or not localizacao:
        print("Dados incompletos! Cadastro cancelado.\n")
        return

    usuario = {
        "nome": nome,
        "email": email,
        "cep": localizacao,
        "risco": risco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!\n")

def criar_alerta():
    print("\n== Criar Alerta Climático ==")
    cep = input("CEP da ocorrência: ")
    descricao = input("Descrição do alerta: ")

    if not cep or not descricao:
        print("Dados inválidos.\n")
        return

    alerta = {
        "cep": cep,
        "descricao": descricao,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    alertas.append(alerta)
    print("Alerta registrado!\n")

def visualizar_alertas():
    print("\n== Alertas Atuais ==")
    for alerta in alertas:
        print(f"{alerta['timestamp']} - CEP: {alerta['cep']} - {alerta['descricao']}")
    print()

def consultar_historico():
    print("\n== Histórico de Enchentes por CEP ==")
    cep = input("Digite o CEP: ")
    if cep in historico_enchentes:
        print(f"Ocorrências registradas para o CEP {cep}: {', '.join(historico_enchentes[cep])}")
    else:
        print("Nenhum registro encontrado.")
    print()

def doar():
    print("\n== Doações ==")
    nome = input("Nome do doador: ")
    valor = input("Valor da doação (R$): ")

    try:
        valor = float(valor)
        if valor <= 0:
            raise ValueError
    except ValueError:
        print("Valor inválido.")
        return

    doacoes.append({"nome": nome, "valor": valor})
    print("Doação registrada! Obrigado pelo apoio.\n")

def menu():
    while True:
        print("=== Sistema de Monitoramento de Enchentes ===")
        print("1. Cadastrar usuário")
        print("2. Criar alerta climático")
        print("3. Ver alertas em tempo real")
        print("4. Consultar histórico por CEP")
        print("5. Realizar doação")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if not usuarios and escolha not in ["1", "6"]:
            print("\n Nenhum usuário cadastrado. Por favor, cadastre um usuário antes de continuar.\n")
            continue

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            criar_alerta()
        elif escolha == "3":
            visualizar_alertas()
        elif escolha == "4":
            consultar_historico()
        elif escolha == "5":
            doar()
        elif escolha == "6":
            print("Sistema encerrado. Obrigado por contribuir!")
            break
        else:
            print("Opção inválida.\n")

# Início do sistema
if __name__ == "__main__":
    menu()