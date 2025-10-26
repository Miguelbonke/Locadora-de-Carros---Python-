
# pip install customtkinter Pillow
# pip install Pillow

import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Adiciona a funcionalidade para imagens

ctk.set_appearance_mode("dark")

# Simulação de banco de dados de usuários
usuarios = {}

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("700x400")
        self.title("Sistema - Locadora de Veiculos DMF")
        self.iconbitmap("icone.ico")
        self.resizable(False, False)

        self.current_frame = None
        self.valor_total_aluguel = 0  # Variável para armazenar o valor total do aluguel
        self.show_login_frame()

    def switch_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

    def show_login_frame(self):
        login_frame = ctk.CTkFrame(self)

        # Carregar a imagem
        image = Image.open("logo_login.png")
        image = image.resize((100, 100))  # Redimensionar a imagem se necessário
        self.image_tk = ImageTk.PhotoImage(image)  # Manter uma referência para evitar garbage collection

        # Adicionar a imagem ao login_frame
        img_label = Label(login_frame, image=self.image_tk, bg="#2a2d2e")
        img_label.pack(pady=10)

        title = ctk.CTkLabel(login_frame, text="FAÇA O LOGIN", font=('Roboto', 28, 'bold'), text_color=('white'))
        title.pack(pady=10)

        self.username_entry = ctk.CTkEntry(login_frame, placeholder_text="Usuário", corner_radius=15, width=300)
        self.username_entry.pack(pady=(0, 10))

        self.password_entry = ctk.CTkEntry(login_frame, placeholder_text="Senha", show="*", corner_radius=15, width=300)
        self.password_entry.pack(pady=(0, 10))

        login_button = ctk.CTkButton(login_frame, fg_color="green", text="Login", corner_radius=15, hover_color="#145C34", command=self.login)
        login_button.pack(pady=10)

        register_button = ctk.CTkButton(login_frame, text="Registrar-se", corner_radius=15, fg_color="#2E86AB", hover_color="#1B4F72", command=self.show_register_frame)
        register_button.pack(pady=10)

        self.switch_frame(login_frame)

    def show_register_frame(self):
        register_frame = ctk.CTkFrame(self)

        # Carregar a imagem
        image = Image.open("logo_registro.png")
        image = image.resize((100, 100))  # Redimensionar a imagem se necessário
        self.image_tk = ImageTk.PhotoImage(image)  # Manter uma referência para evitar garbage collection

        # Adicionar a imagem ao register_frame
        img_label = Label(register_frame, image=self.image_tk, bg="#2a2d2e")
        img_label.pack(pady=10)

        title = ctk.CTkLabel(register_frame, text="CADASTRAR USUÁRIO", font=('Roboto', 28, 'bold'), text_color=('white'))
        title.pack(pady=10)

        self.reg_username_entry = ctk.CTkEntry(register_frame, placeholder_text="Usuário", corner_radius=15, width=300)
        self.reg_username_entry.pack(pady=(0, 10))

        self.reg_password_entry = ctk.CTkEntry(register_frame, placeholder_text="Senha", show="*", corner_radius=15, width=300)
        self.reg_password_entry.pack(pady=(0, 10))

        register_button = ctk.CTkButton(register_frame, fg_color="green", text="Cadastrar", corner_radius=15, hover_color="#145C34", command=self.register)
        register_button.pack(pady=10)

        back_button = ctk.CTkButton(register_frame, fg_color="red", text="Voltar ao Login", corner_radius=15, hover_color="#8A2C2C", command=self.show_login_frame)
        back_button.pack(pady=10)

        self.switch_frame(register_frame)

    def show_home_frame(self):
        home_frame = ctk.CTkFrame(self)

        # Configurar o layout das colunas para centralizar os widgets
        home_frame.grid_columnconfigure(0, weight=1)  # Configura a primeira coluna para expandir
        home_frame.grid_columnconfigure(1, weight=1)  # Configura a segunda coluna para expandir

        # Adicionar o texto "Seja bem-vindo à locadora de veículos DMF"
        welcome_label = ctk.CTkLabel(home_frame, text="Seja bem-vindo à locadora de veículos DMF", font=('Roboto', 28, 'bold'), text_color=('white'))
        welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="n")

        # Texto "Preencha os dados corretamente"
        label_home = ctk.CTkLabel(home_frame, text="Preencha os dados corretamente:", font=('Roboto', 20, 'bold'), text_color=('yellow'))
        label_home.grid(row=1, column=0, columnspan=2, padx=10, pady=(5, 5), sticky="n")

        # Nome
        nome_label = ctk.CTkLabel(home_frame, text="Digite o seu nome completo:", text_color="white", font=("Roboto", 14))
        nome_label.grid(row=2, column=0, padx=10, pady=(5, 5), sticky="e")

        self.nome_entry = ctk.CTkEntry(home_frame, placeholder_text="Nome", width=250, font=("Roboto", 14))
        self.nome_entry.grid(row=2, column=1, padx=10, pady=(5, 5), sticky="w")

        # Tipo de Carro
        tipo_carro_label = ctk.CTkLabel(home_frame, text="Selecione uma categoria de veículo:", text_color="white", font=("Roboto", 14))
        tipo_carro_label.grid(row=3, column=0, padx=10, pady=(5, 5), sticky="e")

        self.tipo_carro_combobox = ctk.CTkComboBox(home_frame, values=["Grupo A - [BASICO]", "Grupo B - [COMPACTOS]", "Grupo C - [PREMIUM]"], width=250, font=("Roboto", 14))
        self.tipo_carro_combobox.grid(row=3, column=1, padx=10, pady=(5, 5), sticky="w")

        # Quilometragem
        km_label = ctk.CTkLabel(home_frame, text="Quantos quilômetros pretende rodar?", text_color="white", font=("Roboto", 14))
        km_label.grid(row=4, column=0, padx=10, pady=(5, 5), sticky="e")

        self.km_entry = ctk.CTkEntry(home_frame, placeholder_text="KM", width=250, font=("Roboto", 14))
        self.km_entry.grid(row=4, column=1, padx=10, pady=(5, 5), sticky="w")

        # Dias de uso
        dias_label = ctk.CTkLabel(home_frame, text="Quantos dias irá utilizar o veículo?", text_color="white", font=("Roboto", 14))
        dias_label.grid(row=5, column=0, padx=10, pady=(5, 5), sticky="e")

        self.dias_entry = ctk.CTkEntry(home_frame, placeholder_text="Dias", width=250, font=("Roboto", 14))
        self.dias_entry.grid(row=5, column=1, padx=10, pady=(5, 5), sticky="w")

        # Botão de Calcular Simulação
        cal_button = ctk.CTkButton(home_frame, text="Calcular Simulação", fg_color="green", command=self.show_calculo_frame, width=250)
        cal_button.grid(row=6, column=0, columnspan=2, padx=10, pady=(15, 5))

        # Botão de Sair
        sair_button = ctk.CTkButton(home_frame, text="Sair", fg_color="red", command=self.show_login_frame, width=250)
        sair_button.grid(row=7, column=0, columnspan=2, padx=10, pady=(5, 10))

        self.switch_frame(home_frame)

    def show_calculo_frame(self):
        calculo_frame = ctk.CTkFrame(self)

        # Função para calcular quilometragem e valor do aluguel
        def calcular_simulacao(km, dias, tipo_carro):
            try:
                km = float(km)
                dias = int(dias)
                resultado_km = km * dias
                # Cálculo do valor do aluguel baseado no tipo de carro
                if "Grupo A" in tipo_carro:
                    valor_por_dia = 160
                elif "Grupo B" in tipo_carro:
                    valor_por_dia = 200
                elif "Grupo C" in tipo_carro:
                    valor_por_dia = 240
                else:
                    valor_por_dia = 0  # Caso nenhum grupo seja selecionado corretamente

                valor_aluguel = dias * valor_por_dia
                return resultado_km, valor_aluguel
            except ValueError:
                return None, None

        # Função para exibir resultado de quilometragem e aluguel
        def exibir_resultado(resultado_km, valor_aluguel):
            if resultado_km is None or valor_aluguel is None:
                resultado_texto = "Por favor, insira valores válidos para quilômetros e dias."
                valor_aluguel_texto = ""
            else:
                resultado_texto = f"Você rodará aproximadamente {resultado_km:.2f} km durante {dias} dias."
                valor_aluguel_texto = f"O valor final do aluguel será: R$ {valor_aluguel:.2f}."
                # Armazenando o valor total para uso posterior
                self.valor_total_aluguel = valor_aluguel

            resultado_label.configure(text=resultado_texto)
            valor_label.configure(text=valor_aluguel_texto)

        # Recupera dados do formulário
        nome_usuario = self.nome_entry.get()
        tipo_carro = self.tipo_carro_combobox.get()
        km = self.km_entry.get()
        dias = self.dias_entry.get()

        # Exibição das mensagens iniciais
        label_calculo = ctk.CTkLabel(calculo_frame, text=f"Olá, {nome_usuario}!", font=('Roboto', 28, 'bold'), text_color=('white'))
        label_carro = ctk.CTkLabel(calculo_frame, text=f"Você escolheu o {tipo_carro}. Abaixo está a sua simulação:", font=('Roboto', 18), text_color=('white'))

        # Configurando o layout do frame para expandir e centralizar
        calculo_frame.grid_columnconfigure(0, weight=1)
        calculo_frame.grid_columnconfigure(1, weight=1)

        # Centralizando os labels
        label_calculo.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        label_carro.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        # Cálculo dos resultados
        resultado_km, valor_aluguel = calcular_simulacao(km, dias, tipo_carro)

        # Exibição dos resultados
        resultado_label = ctk.CTkLabel(calculo_frame, font=('Roboto', 16), text_color=('yellow'))
        resultado_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        valor_label = ctk.CTkLabel(calculo_frame, font=('Roboto', 16), text_color=('orange'))
        valor_label.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        exibir_resultado(resultado_km, valor_aluguel)

        # Pergunta sobre prosseguir com a locação
        pergunta_label = ctk.CTkLabel(calculo_frame, text="Deseja prosseguir com a locação do veiculo?", font=('Roboto', 16), text_color=('white'))
        pergunta_label.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        # Botões de Sim e Não com layout centralizado
        sim_button = ctk.CTkButton(calculo_frame, text="Sim", fg_color="green", command=self.show_pagamento_frame)
        sim_button.grid(row=5, column=0, padx=20, pady=20, sticky="e")

        nao_button = ctk.CTkButton(calculo_frame, text="Não", fg_color="red", command=self.show_home_frame)
        nao_button.grid(row=5, column=1, padx=20, pady=20, sticky="w")

        self.switch_frame(calculo_frame)

    def show_pagamento_frame(self):
        pagamento_frame = ctk.CTkFrame(self)

        title = ctk.CTkLabel(pagamento_frame, text="Formas de Pagamento", font=('Roboto', 28, 'bold'), text_color=('white'))
        title.pack(pady=10)

        # Exibir as formas de pagamento
        pagamento_label = ctk.CTkLabel(pagamento_frame, text="Escolha uma das opções abaixo:", font=('Roboto', 18), text_color=('white'))
        pagamento_label.pack(pady=10)

        # Botões de pagamento (cartão de crédito, débito, etc.)
        opcao_cartao_credito = ctk.CTkButton(pagamento_frame, text="Cartão de Crédito", fg_color="#2E86AB", hover_color="#1B4F72", command=self.show_parcelamento_frame)
        opcao_cartao_credito.pack(pady=10)

        # Função para exibir a mensagem de pagamento aprovado no débito
        def confirmar_pagamento_debito():
            messagebox.showinfo(
                "Pagamento Aprovado",
                f"Pagamento aprovado!\nValor total da compra: R$ {self.valor_total_aluguel:.2f}."
            )
            self.show_home_frame()

        # Função para exibir a mensagem de boleto gerado
        def gerar_boleto():
            messagebox.showinfo(
                "Boleto Gerado",
                f"Boleto gerado com sucesso!\nValor total do boleto: R$ {self.valor_total_aluguel:.2f}."
            )
            self.show_home_frame()

        # Função para exibir a mensagem de PIX aprovado
        def confirmar_pagamento_pix():
            messagebox.showinfo(
                "PIX Aprovado",
                f"Pagamento via PIX aprovado!\nValor total da compra: R$ {self.valor_total_aluguel:.2f}."
            )
            self.show_home_frame()

        # Botão para pagamento com Cartão de Débito
        opcao_cartao_debito = ctk.CTkButton(pagamento_frame, text="Cartão de Débito", fg_color="#2E86AB", hover_color="#1B4F72", command=confirmar_pagamento_debito)
        opcao_cartao_debito.pack(pady=10)

        # Botão para pagamento com Boleto Bancário
        opcao_boleto = ctk.CTkButton(pagamento_frame, text="Boleto Bancário", fg_color="#2E86AB", hover_color="#1B4F72", command=gerar_boleto)
        opcao_boleto.pack(pady=10)

        # Botão para pagamento com PIX
        opcao_pix = ctk.CTkButton(pagamento_frame, text="PIX", fg_color="#2E86AB", hover_color="#1B4F72", command=confirmar_pagamento_pix)
        opcao_pix.pack(pady=10)

        # Botão de voltar
        voltar_button = ctk.CTkButton(pagamento_frame, text="Voltar", fg_color="red", command=self.show_calculo_frame)
        voltar_button.pack(pady=10)

        self.switch_frame(pagamento_frame)

    def show_parcelamento_frame(self):
        parcelamento_frame = ctk.CTkFrame(self)

        # Configurar layout do frame para centralizar os elementos
        parcelamento_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)  # Configura todas as 4 colunas com peso igual

        title = ctk.CTkLabel(parcelamento_frame, text="Opções de Parcelamento", font=('Roboto', 28, 'bold'), text_color=('white'))
        title.grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

        # Exibir as opções de parcelamento
        parcelamento_label = ctk.CTkLabel(parcelamento_frame, text="Escolha em quantas vezes deseja parcelar:", font=('Roboto', 18), text_color=('white'))
        parcelamento_label.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

        # Organizar os botões em uma grade com 4 colunas
        colunas = 4  # Definimos 4 colunas para que os botões fiquem dispostos horizontalmente
        for i in range(1, 13):
            opcao_parcelamento = ctk.CTkButton(parcelamento_frame, text=f"{i}x", fg_color="#2E86AB", hover_color="#1B4F72", command=lambda i=i: self.confirmar_pagamento(i))
            row = (i - 1) // colunas + 2  # Calcula a linha
            column = (i - 1) % colunas  # Calcula a coluna
            opcao_parcelamento.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        # Botão de voltar
        voltar_button = ctk.CTkButton(parcelamento_frame, text="Voltar", fg_color="red", command=self.show_pagamento_frame)
        voltar_button.grid(row=row + 1, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

        self.switch_frame(parcelamento_frame)

    def confirmar_pagamento(self, vezes):
        # Calcular o valor de cada parcela
        valor_parcela = self.valor_total_aluguel / vezes

        # Exibir a mensagem com o valor total da compra e o valor de cada parcela
        messagebox.showinfo(
            "Pagamento Confirmado",
            f"Você escolheu parcelar em {vezes}x.\n"
            f"Valor total da compra: R$ {self.valor_total_aluguel:.2f}.\n"
            f"Valor de cada parcela: R$ {valor_parcela:.2f}.\n"
            "Seu pagamento foi confirmado!"
        )
        self.show_home_frame()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in usuarios and usuarios[username] == password:
            messagebox.showinfo('Sucesso', 'Login Realizado!')
            self.show_home_frame()
        else:
            messagebox.showerror('Erro!', 'Usuário ou senha inválida!\n\nSe não está cadastrado no sistema, por favor clique em Registrar-se!')

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()

        if username in usuarios:
            messagebox.showerror('Atenção!', 'Usuário já existe!')
        else:
            usuarios[username] = password
            messagebox.showinfo('Sucesso', 'Cadastro realizado com sucesso!')
            self.show_login_frame()

if __name__ == "__main__":
    app = App()
    app.mainloop()
