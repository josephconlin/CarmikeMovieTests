__author__ = 'Joseph Conlin'
"""
Classes for test input from files
"""
from openpyxl import Workbook, load_workbook

# Setup common variables
_defaultFileName = "SearchParams"


class ReadExcel:
    defaultFileExtension = ".xlsx"

    @staticmethod
    def get_sheet_values(fileName=_defaultFileName+defaultFileExtension):
        """
        :return: Two dimensional list containing the values of each of the cells in the sheet
        """
        sheet = []
        wb = load_workbook(filename = fileName)
        ws = wb.active
        for row in ws.rows:
            cells = []
            for cell in row:
                cells.append(cell.value)

            sheet.append(cells)

        return sheet
