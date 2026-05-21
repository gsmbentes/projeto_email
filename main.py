from parte1 import Email 

nome = input("Digite seu nome: ")
Cr = Email(nome)

while True:
    print(f"\n--- Olá {nome.upper()}, Bem-vindo ao painel ---")
    print("1 - Criar E-mail / Cadastrar")
    print("2 - Entrar em um Site")
    print("3 - Sair de um Site")
    print("4 - Redefinir Senha")
    print("5 - Verificar o Historico")
    print("6 - Sair do Programa")
    
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
            site = input("Nome do site: ")
            em = input("E-mail: ")
            se = input("Senha: ")
            Cr.saindo_site(em, se, site)
        elif opcao == "4":
            antiga = input("Senha atual: ")
            nova = input("Nova senha: ")
            Cr.redefinir_senha(antiga, nova)
        elif opcao == "5":
            se = input("Senha para a visualização do histórico : ")
            Cr.exibir_historico(se)
        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

    except (ValueError, PermissionError) as e:
        print(f"\nALERTA: {e}")