# 🛡️ Sistema de Autenticação e Navegação Simulada

Este projeto foi desenvolvido por **Gustavo** como parte de estudos avançados em **Programação Orientada a Objetos (POO)** com Python. O sistema simula o gerenciamento de uma conta de e-mail e o controle de sessões de navegação em sites.

## 🚀 Funcionalidades Principais

O sistema é dividido em módulos que garantem a segurança e a integridade dos dados:

* **Criação de Conta:** Validação rigorosa de e-mail (sufixo `@gmail.com`) e requisitos de senha forte (mínimo de 6 caracteres, letras, números e caracteres especiais).
* **Autenticação de Acesso:** Métodos privados que validam as credenciais antes de permitir qualquer ação sensível.
* **Gerenciamento de Sessão Ativa:** O sistema monitora em qual site o utilizador está "logado". Não é possível sair de um site sem ter entrado nele previamente ou tentar sair de um site estando noutro.
* **Histórico de Atividades:** Registo automático de todas as ações realizadas (criações, trocas de senha, entradas e saídas de sites), protegido por senha para visualização.

## 🛠️ Tecnologias e Conceitos Aplicados

Este projeto demonstra o domínio técnico em:

* **Encapsulamento:** Uso de atributos privados (`__senha`, `__gmail`, `__historico`) para proteção de dados sensíveis.
* **Tratamento de Exceções:** Implementação de `raise ValueError` e `raise PermissionError` para lidar com entradas inválidas ou tentativas de acesso negado.
* **Lógica de Estados:** Controlo da variável de sessão `nome_site` para garantir um fluxo lógico de navegação.
* **Arquitetura Limpa:** Separação total entre a lógica de negócio (`Email`) e a interface de utilizador (CLI).

## 📂 Estrutura do Projeto

* **`parte1.py`**: Contém a classe `Email` com toda a lógica, validações e armazenamento de dados.
* **`main.py`**: Interface de linha de comando que gere o loop de interação com o utilizador e o tratamento de erros em tempo de execução.

---

### Exemplo de Uso do Histórico:
O histórico utiliza a função `enumerate` para exibir as atividades de forma organizada e numerada:
1. Criação de conta e e-mail
2. Acesso ao Site: www.google.com.br
3. Saída do Site: www.google.com.br
4. Redefinição de senha
