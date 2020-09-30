import xlsxwriter
import pandas as pd
import sys
import os
import tabula
from zipfile import ZipFile
import sys


def tabExtract(filePath):  # ocr_api\media\sfbt.pdf

    #print("Python version")
    # print(sys.version)
    #print("Version info.")
    # print(sys.version_info)

    # Read and Extract tables from the pdf file
    tables = tabula.read_pdf('media/'+filePath, multiple_tables=True,
                             pages='all',  encoding='ISO-8859-1')

    writer = pd.ExcelWriter(
        'media/output/' + filePath[:-4] + '.xlsx', engine='xlsxwriter')

    i = 0
    for table in tables:
        table.columns = table.iloc[0]
        table = table.reindex(table.index.drop(0)).reset_index(drop=True)
        table.columns.name = None
        # To write Excel
        table.to_excel(writer, header=True,
                       sheet_name='tab'+str(i), index=False)
        # To write CSV
        # table.to_csv('output'+str(i)+'.csv',sep='|',header=True,index=False)

        # add excel table to the zip object

        i += 1
    writer.save()
    writer.close()
    print(len(tables), ' tables was extracted')
