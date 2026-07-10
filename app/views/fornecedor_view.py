from colorama import init, Fore, Style

init(autoreset=True)

class Fornecedor_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "===CRUD DE FORNECEDORES (MVC)==="

    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar fornecedor")
        print(f"2 - Listar fornecedores")
        print(f"3 - Atualizar fornecedor")
        print(f"4 - Excluir fornecedor")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def ler_dados_fornecedor(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE FORNECEDOR ===")
        razao = input("Digite a razão social do fornecedor: ")
        nome = input("Digite o nome fantasia do fonecedor: ")
        cnpj = input("Digite o CNPJ do fornecedor: ")
        sla = int(input("Digite o SLA de atendimento do fornecedor: "))
        return razao, nome, cnpj, sla

    def ler_id(self):
        return input("Digite o ID do fornecedor: ")
    
    def exibir_fornecedores(self, fornecedores):
        print(Fore.YELLOW + "\n--- TABELA DE FORNECEDORES ---")
        if not fornecedores:
            print("Nenhum fornecedor cadastrado")
            return
        print(f"{'ID':<4} | {'RAZÃO SOCIAL':<29} | {'NOME FANTASIA':<20} | {'CNPJ':<18} | {'SLA ATENDIMENTO':<17}")
        print("-"*100)
        for f in fornecedores:
            print(f"{f.id:<4} | {f.razao_social:<29} | {f.nome_fantasia:<20} | {f.cnpj:<18} | {f.sla_atendimento:<17}")
        print("-"*100)

    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")