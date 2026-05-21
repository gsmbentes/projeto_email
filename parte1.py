class Email:
    def __init__(self,titular):
        self._titular = titular
        self.__senha = None
        self.__gmail = None
    def criar_email(self,email_novo,senha_nova):
        if self.__gmail and self.__senha is not None:
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
            raise ValueError(f"Site '{site}' inválido: deve começar com 'www.'")s
        if not site_formatado.endswith(".com.br"):
            raise ValueError(f"Site '{site}' inválido: deve terminar em '.com.br'")

        return True
    def entrar_site(self,gmail_tenta,senha_tenta,nome_site):
        self._autenticar_email(gmail_tenta,senha_tenta)
        self.validar_site(nome_site)
        print(f"entrando no site {nome_site}... ")
    def saindo_site(self,gmail_tenta,senha_tenta,nome_site):
        self._autenticar_email(gmail_tenta,senha_tenta)
        self.validar_site(nome_site)
        print(f"saindo do site {nome_site}")
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
        print("Senha redefinida com sucesso!")
    
