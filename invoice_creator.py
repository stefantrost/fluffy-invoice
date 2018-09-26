from invoice import Invoice

def main():
    print("An wen geht die Rechnung?")
    invoicee_business_name = input("Ggf. Unternehmensname (oder leer lassen): ")
    invoicee_title = input("Anrede (Frau/Herr): ")
    invoicee_name = input("Vorname und Nachname: ")
    invoicee_street_houseno = input("Strasse und Hausnummer: ")
    invoicee_postcode_city = input("Plz und Ort: ")

    invoice_item = input("Was soll abgerechnet werden? ")
    invoice_value = input("Wieviel soll abgerechnet werden? ")

    if invoicee_business_name:
        display_name = f"{invoicee_business_name}\n{invoicee_name}"
    else :
        display_name = invoicee_name
    my_invoice = Invoice(invoicee_title, invoicee_name)
    my_invoice.new_line()
    my_invoice.my_address("My Name", "Street No 5", "54321 City", "mail@me.com", "0800 555 444 33")
    my_invoice.invoice_address(display_name, invoicee_street_houseno, invoicee_postcode_city)
    my_invoice.header()

    my_invoice.invoice_items([{'label': "32 Stunden a 70 EUR/Stunde", 'value': "2240,01"}, {'label': "20 T-Shirts a 20 EUR/Stück", 'value': "400,03"}])

    my_invoice.greetings()

    my_invoice.print_invoice()


if __name__ == "__main__":
    main()
