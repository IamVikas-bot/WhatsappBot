import os
import xlsxwriter

from whatsapp import WhatsApp

#Need to create
whatsapp = WhatsApp(100, session="mysession")
if os. path. exists("ReadMessages.xlsx"):
    os.remove("ReadMessages.xlsx")
row = 0
column = 0
workbook = xlsxwriter.Workbook('ReadMessages.xlsx')
worksheet = workbook.add_worksheet()
messages = whatsapp.get_unread_messages_only()
for msg in messages:
    worksheet.write(row, column, msg)
    row += 1

workbook.close()
whatsapp.quit()