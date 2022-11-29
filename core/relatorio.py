from reportlab.pdfgen import canvas
import webbrowser


class Relatorios():
    # Abrir arquivo pdf no navegador padrão
    def print_cliente(self):
        webbrowser.open("cliente.pdf")

    def gerar_relatorio(self):
        self.c = canvas.Canvas("cliente.pdf")

        #self.codigo_rel = self.codigo_entry.get()
        self.nome_rel = self.nome_entry.get()
        self.tel_rel = self.telefone_entry.get()
        self.cpf_rel = self.cpf_entry.get()
        self.valor_rel = self.valor_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, "Ficha do Cliente")

        self.c.setFont("Helvetica-Bold", 18)
        #self.c.drawString(50, 700, "Código: " + self.codigo_rel)
        self.c.drawString(50, 700, "Nome: " + self.nome_rel)
        self.c.drawString(50, 670, "CPF: " + self.cpf_rel)
        self.c.drawString(50, 640, "Telefone: " + self.tel_rel)
        self.c.drawString(50, 610, "Valor R$: " + self.valor_rel)

        self.c.showPage()
        self.c.save()
        self.print_cliente()