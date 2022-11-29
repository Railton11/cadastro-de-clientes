from tkinter import END, messagebox
import sqlite3
import os


class Funcs():
    def limpar_clientes(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.valor_entry.delete(0, END)

    def conectar_bd(self):
        self.conn = sqlite3.connect("banco.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")

    def criar_tabela_clientes(self):
        self.conectar_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                codigo INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                cpf NUMERIC(11) UNIQUE NOT NULL,
                telefone NUMERIC(11),
                valor REAL,
                criado DATETIME DEFAULT CURRENT_TIMESTAMP

            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.cpf = self.cpf_entry.get()
        self.telefone = self.telefone_entry.get()
        self.valor = self.valor_entry.get()

    def add_cliente(self):
        self.variaveis()
        if self.nome_entry.get() == "":
            msg = "Para cadastra um novo cliente, é necessário inserir um nome."
            messagebox.showinfo("Cadastro de clientes - Aviso!", msg)

        elif self.cpf_entry.get() == "":
            msg = "Para cadastra um novo cliente, é necessário inserir um CPF."
            messagebox.showinfo("Cadastro de clientes - Aviso!", msg)

        else:
            self.conectar_bd()

            self.cursor.execute("""
                INSERT INTO clientes (nome_cliente, cpf, telefone, valor)
                VALUES (?, ?, ?, ?)""", (self.nome, self.cpf, self.telefone, self.valor))
            self.conn.commit()
            self.desconecta_bd()
            self.limpar_clientes()
            self.select_lista()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conectar_bd()
        lista = self.cursor.execute(""" SELECT codigo, nome_cliente, telefone, cpf, valor  FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
        
    def duplo_click(self, event):
        self.limpar_clientes()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5 = self.listaCli.item(n, "values")
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cpf_entry.insert(END, col4)
            self.valor_entry.insert(END, col5)

    def deleta_cliente(self):
        self.variaveis()
        self.conectar_bd()
        self.cursor.execute(""" DELETE FROM clientes WHERE codigo= ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_clientes()
        self.select_lista()

    def alterar_cliente(self):
        self.variaveis()
        self.conectar_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, cpf = ?, telefone = ?, valor = ? WHERE codigo = ? """,
        (self.nome, self.cpf, self.telefone, self.valor, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_clientes()

    def ajuda(self):
            self.arquivo = ("ajuda.txt")
            os.startfile(self.arquivo)

    def buscar_cliente(self):
        self.conectar_bd()
        self.listaCli.delete(*self.listaCli.get_children())
        self.nome_entry.insert(END, "%")
        #self.cpf_entry.insert(END, "%")
        nome = self.nome_entry.get()
        #cpf = self.cpf_entry.get()
        self.cursor.execute("""
            SELECT codigo, nome_cliente, telefone, cpf, valor FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC;
        """ % nome)
        buscar = self.cursor.fetchall()
        for i in buscar:
            self.listaCli.insert("", END, values=i)
        self.limpar_clientes()
        self.desconecta_bd()

    