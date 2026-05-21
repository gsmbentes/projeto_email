class Email:
    def __init__(self,titular):
        self._titular = titular
        self.__senha = None
        self.__gmail = None
        self.nome_site = None
        self.__historico = []
    def criar_email(self,email_novo,senha_nova):
        if self.__gmail is not None and self.__senha is not None:
            raise ValueError("Dados ja presentes, ERRO!")
        if len(email_novo) < 6 or len(senha_nova) < 6:
            raise ValueError("minimo de 6 caracteres")
        sinais = "!@#?"
        if not any(caractere in sinais for caractere in senha_nova):
            raise ValueError("no minimo um sinal especial")
        tem_letra = any(c.isalpha() for c in senha_nova)
        tem_numero = any(c.isdigit() for c in senha_nova)
        if not (tem_letra and tem_numero):
            raise ValueError("A senha deve conter letras e números")
        email_novo = email_novo.lower()
        sufixo = "@gmail.com"        
        if not email_novo.endswith(sufixo) or email_novo.find(sufixo) <= 0:
            raise ValueError("O e-mail deve ser um endereço @gmail.com válido")
        self.__gmail = email_novo
        self.__senha = senha_nova
        self.__historico.append("Criação de conta e e-mail")
        print(f"Conta para {self._titular} criada com sucesso!")
    def _autenticar_email(self,email_tenta,senha_tenta):
        if email_tenta != self.__gmail :
            raise PermissionError("Erro, email inválido!")
        if senha_tenta != self.__senha:
            raise PermissionError("Erro, senha incorreta!!")
        else:
            return True
    def validar_site(self, site):
        site_formatado = site.strip().lower()
        if not site_formatado.startswith("www."):
            raise ValueError(f"Site '{site}' inválido: deve começar com 'www.'")
        if not site_formatado.endswith(".com.br"):
            raise ValueError(f"Site '{site}' inválido: deve terminar em '.com.br'")

        return True
    def entrar_site(self,gmail_tenta,senha_tenta,nome_site):
        self._autenticar_email(gmail_tenta,senha_tenta)
        self.validar_site(nome_site)
        self.nome_site = nome_site
        self.__historico.append(f"acesso ao Site : {nome_site}")
        print(f"entrando no site {nome_site}... ")
    def nome_site_validar(self,nome_site):
        if self.nome_site is None :
            raise PermissionError("erro site sem nome")
        if nome_site != self.nome_site: 
            raise ValueError(f"site não identificado , usuário está presente neste site {self.nome_site}")
        else:
            self.nome_site = nome_site
    def saindo_site(self,gmail_tenta,senha_tenta,nome_site):
        self._autenticar_email(gmail_tenta,senha_tenta)
        self.validar_site(nome_site)
        self.nome_site_validar(nome_site)
        self.__historico.append(f"saída do Site : {nome_site}")
        print(f"saindo do site {nome_site}")
        self.nome_site = None
    def redefinir_senha(self, senha_antiga, senha_nova):
        if self.__senha != senha_antiga:
            raise ValueError("A senha atual está incorreta. Não é possível redefinir.")

        if senha_antiga == senha_nova:
            raise ValueError("A nova senha não pode ser igual à senha atual.")

        if len(senha_nova) < 6:
            raise ValueError("A nova senha deve ter no mínimo 6 caracteres.")

        sinais = "!@#?"
        tem_letra = any(c.isalpha() for c in senha_nova)
        tem_numero = any(c.isdigit() for c in senha_nova)
        tem_sinal = any(c in sinais for c in senha_nova)

        if not (tem_letra and (tem_numero or tem_sinal)):
            raise ValueError("A nova senha deve conter letras e (números ou sinais !@#?).")

        self.__senha = senha_nova
        self.__historico.append("Redefinição de senha")
        print("Senha redefinida com sucesso!")
    def _validar_senha(self,senha_tenta):
        if senha_tenta != self.__senha:
            raise PermissionError("erro senha esta errada, acesso negado")
        else:
            return True
    def exibir_historico(self,senha_tenta):
        self._validar_senha(senha_tenta)
        print(f"Histórico de navegação de {self._titular}")
        if not  self.__historico :
            print("Zero atividades")
            return
        for i, atividade in enumerate(self.__historico, 1):
            print(f"{i}. {atividade}")

        print(f"\nTotal de atividades realizadas: {len(self.__historico)}")
        print("-"*45)