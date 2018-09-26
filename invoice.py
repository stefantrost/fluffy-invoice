from datetime import date
from fpdf import FPDF


class Invoice:
    def __init__(self, title, name):
        self.title = title
        self.name = name
        self.pdf = PDF()
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
        self.pdf.write(5, f"Sehr geehrte {self.title} {self.name},\n\nwie vereinbart berechne ich Ihnen für folgende Leistungen den folgenden Betrag:")
        self.new_line(3)

    def invoice_items(self, items_list):
        for item in items_list:
            self.pdf.write(5, item['label'])
            value = f"{item['value']} EUR"
            self.pdf.set_x(190 - self.pdf.get_string_width(value))
            self.pdf.write(5, value)
            self.new_line()

        total = sum([self._parse_formatted_float(item['value']) for item in items_list])
        y = self.pdf.get_y() + 1
        self.pdf.line(10, y, 193, y)
        self.pdf.write(10, "Gesamt:")
        value = f"{self._format_float(total)} EUR"
        self.pdf.set_x(190 - self.pdf.get_string_width(value))
        self.pdf.write(10, value)
        self.new_line()
        self.pdf.set_font('Times', '', 9)
        self.pdf.write(5, "Betrag zahlbar sofort ohne Abzug.")
        self.pdf.set_font('Times', '', 12)
        self.new_line(3)


    def greetings(self):
        self.pdf.write(5, "Steuernummer: ")
        self.new_line()
        self.pdf.write(5, "Finanzamt: Hofheim a. Ts.")
        self.new_line(3)
        self.pdf.write(5, "Vielen Dank für Ihr Vertrauen!")
        self.new_line(4)
        self.pdf.write(5, "Mit besten Grüßen")
        self.new_line(2)
        self.pdf.write(5, "Stefan Trost")


    def print_invoice(self):
        self.pdf.output('invoice.pdf')

    def _parse_formatted_float(self, formatted_float: str):
        return float(formatted_float.replace(',', '.'))

    def _format_float(self, number: float):
        string = str(round(number, 2))
        parts = string.split('.')
        if len(parts[1]) == 1:
            parts[1] += "0"
        return ",".join(parts)




class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        self.write(4, "Bankverbindung: Bank, IBAN: DE00 XXXX XXXX XXXX XXXX XX")