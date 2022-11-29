from tkinter import *
from tkinter import ttk

from funcionalidades import Funcs
from relatorio import Relatorios
from validadores import Validadores

janela = Tk()


class MeuApp(Funcs, Relatorios, Validadores):
    # Construtor
    def __init__(self):
        self.janela = janela
        self.valida_entrada()
        self.tela()
        self.frames_da_tela()
        self.botoes_frame1()
        self.lista_frame2()
        self.limpar_clientes()
        self.criar_tabela_clientes()
        self.select_lista()
        self.menu()
        janela.mainloop()

    # Definição da tela
    def tela(self):
        self.janela.title("Cadastro de clientes")
        self.janela.iconbitmap("imagem/grafico.ico")
        self.janela.configure(background="#4F4F4F")
        self.janela.geometry("700x500")
        # Responsividade da tela
        self.janela.resizable(True, True)

    def frames_da_tela(self):
        self.frame_1 = Frame(
            self.janela, bd=4, bg="#A9A9A9",
            highlightbackground="#363636", highlightthickness=1.4
            )
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(
            self.janela, bd=4, bg="#A9A9A9",
            highlightbackground="#363636", highlightthickness=1.4
            )
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def botoes_frame1(self):
    # Labels e entradas
        self.lb_nome = Label(self.frame_1, text="Nome", bg="#A9A9A9")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.46, relwidth=0.47, relheight=0.13)

        self.lb_cpf = Label(self.frame_1, text="CPF", bg="#A9A9A9")
        self.lb_cpf.place(relx=0.05, rely=0.65)

        self.cpf_entry = Entry(self.frame_1, validate="key", validatecommand=self.vcpf)
        self.cpf_entry.place(relx=0.05, rely=0.76, relwidth=0.47, relheight=0.13)

        self.lb_telefone = Label(self.frame_1, text="Telefone", bg="#A9A9A9")
        self.lb_telefone.place(relx=0.55, rely=0.35)

        self.telefone_entry = Entry(self.frame_1, validate="key", validatecommand=self.vtelefone)
        self.telefone_entry.place(relx=0.55, rely=0.46, relwidth=0.25, relheight=0.13)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.1, relwidth=0.07, relheight=0.13)

        self.lb_valor = Label(self.frame_1, text="Valor", bg="#A9A9A9")
        self.lb_valor.place(relx=0.55, rely=0.65)
        
        self.valor_entry = Entry(self.frame_1)
        self.valor_entry.place(relx=0.55, rely=0.76, relwidth=0.07, relheight=0.13)

    # Botão de Buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", command=self.buscar_cliente)
        self.bt_buscar.place(relx=0.14, rely=0.1, relwidth=0.1, relheight=0.13)
    # Botão de Adicionar
        self.bt_adicionar = Button(self.frame_1, text="Novo", command=self.add_cliente)
        self.bt_adicionar.place(relx=0.64, rely=0.1, relwidth=0.1, relheight=0.13)
    # Botão de Atualizar
        self.bt_atualizar = Button(self.frame_1, text="Alterar", command=self.alterar_cliente)
        self.bt_atualizar.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.13)
    # Botão de Apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.86, rely=0.1, relwidth=0.1, relheight=0.13)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="CPF")
        self.listaCli.heading("#5", text="Valor")

        self.listaCli.column("#0", width=0)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=250)
        self.listaCli.column("#3", width=100)
        self.listaCli.column("#4", width=100)
        self.listaCli.column("#5", width=100)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        self.listaCli.bind("<Double-1>", self.duplo_click)

    def menu(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.janela.destroy()

        menubar.add_cascade(label="Opção", menu= filemenu)

        filemenu.add_command(label="Relatorio PDF", command=self.gerar_relatorio)
        filemenu.add_command(label="Ajuda", command=self.ajuda)
        filemenu.add_command(label="Limpar cliente", command=self.limpar_clientes)
        filemenu.add_command(label="Sair", command=quit)

    def valida_entrada(self):
        self.vcpf = (self.janela.register(self.validate_cpf), "%P")
        self.vtelefone = (self.janela.register(self.validate_tel), "%P")

MeuApp()