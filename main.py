from parte1 import Email 

nome = input("Digite seu nome: ")
Cr = Email(nome)

while True:
    print(f"\n--- Olá {nome}, Bem-vindo ao painel ---")
    print("1 - Criar E-mail / Cadastrar")
    print("2 - Entrar em um Site")
    print("3 - Redefinir Senha")
    print("4 - Sair do Programa")
    
    opcao = input("Escolha uma opção: ")

    try:
        if opcao == "1":
            email = input("Digite o novo Gmail (@gmail.com): ")
            senha = input("Digite a nova senha: ")
            Cr.criar_email(email, senha)

        elif opcao == "2":
            site = input("Nome do site: ")
            em = input("E-mail: ")
            se = input("Senha: ")
            Cr.entrar_site(em, se, site)

        elif opcao == "3":
            antiga = input("Senha atual: ")
            nova = input("Nova senha: ")
            Cr.redefinir_senha(antiga, nova)

        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

    except (ValueError, PermissionError) as e:
        print(f"\nALERTA: {e}")