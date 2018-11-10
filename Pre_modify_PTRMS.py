import os 
import pandas as pd
from openpyxl import load_workbook


def merge_sheet(rawdata):
    folder_dir = os.path.dirname(__file__)
    print(folder_dir)
    filename = os.path.join(folder_dir,rawdata)
    print(filename,'\n')
    concentration = pd.read_excel(filename,\
    sheet_name = 3)
    print(concentration)
    time = pd.read_excel(filename,\
    sheet_name = 1,usecols = 'B:C')
    print(time)
    result = time.join(concentration)
    print(result)

    book = load_workbook(filename)
    writer = pd.ExcelWriter(filename)
    writer.book = book
    result.to_excel(writer, 'Sheet1')
    writer.save()
    writer.close()

merge_sheet('Book1.xlsx')
input('press enter to exit')
