from invoice import Invoice

my_invoice = Invoice()
my_invoice.new_line()
my_invoice.my_address("Stefan Trost", "Schlehenweg 5", "65719 Hofheim", "stefan@stefantrost.co", "0152 - 561 88 357")
my_invoice.invoice_address("Justso Gmbh\nChristiane Gerigk", "Prauenheimer Landstrasse 95", "60488 Frankfurt a. M.")
my_invoice.header()

my_invoice.print_invoice()