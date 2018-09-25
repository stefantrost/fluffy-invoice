from datetime import date
from fpdf import FPDF


class Invoice:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_font('Times', '', 12)
        self.pdf.add_page()

    def new_line(self, no_lines=1):
        for entry in range(no_lines):
            self.pdf.ln()

    def my_address(self, name, street, city, email, tel):
        longest_line = 0

        for entry in (name, street, city, email, tel):
            width = self.pdf.get_string_width(entry)
            if longest_line < width:
                longest_line = width

        self.pdf.set_font('Times', '', 12)
        self.pdf.set_y(25)

        self.pdf.set_x(190 - longest_line)
        self.pdf.write(5, name)
        self.new_line()

        self.pdf.set_x(190 - longest_line)
        self.pdf.write(5, street)
        self.new_line()

        self.pdf.set_x(190 - longest_line)
        self.pdf.write(5, city)
        self.new_line()

        self.pdf.set_x(190 - longest_line)
        self.pdf.write(6, email)
        self.new_line()

        self.pdf.set_x(190 - longest_line)
        self.pdf.write(5, tel)
        self.new_line()

    def invoice_address(self, name, street, city):
        self.pdf.set_font('Times', '', 12)
        self.pdf.set_y(25)

        self.pdf.write(5, name)
        self.new_line()

        self.pdf.write(5, street)
        self.new_line()

        self.pdf.write(14, city)
        self.new_line()

    def header(self):
        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.set_y(80)
        self.pdf.write(7, "Rechnung")
        self.new_line(2)

        self.pdf.set_font('Times', '', 12)

        self.pdf.write(5, "Rechnungsnummer: 2018 / 1000 0001 ")
        invoice_date = date.today().strftime("%d.%m.%Y")
        self.pdf.set_x(190 - self.pdf.get_string_width(invoice_date))
        self.pdf.write(5, invoice_date)
        self.new_line(4)
        self.pdf.write(5, "Sehr geehrte Frau Gerigk,\n\nwie vereinbart berechne ich Ihnen für folgende Leistungen den folgenden Betrag:")

    def print_invoice(self):
        self.pdf.output('invoice.pdf')
