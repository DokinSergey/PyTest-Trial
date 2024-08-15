import win32print
import win32api

# Открываем диалоговое окно выбора принтера
printer_name = win32print.GetDefaultPrinter()
# Указываем настройки принтера
hPrinter = win32print.OpenPrinter(printer_name)
docInfo = (
'Test Print Document',
None,
{'OutputProtocol': 'RAW'})
# Печать текста
try:
    print_job = win32print.StartDocPrinter(hPrinter, 1, docInfo)
    win32print.StartPagePrinter(hPrinter)
    win32api.WritePrinter(hPrinter, "Hello World!")
    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)
except:
    print("Failed to print")