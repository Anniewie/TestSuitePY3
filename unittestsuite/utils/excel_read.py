from openpyxl import load_workbook
class ParseExcel():
    def __init__(self, excel_path, sheetName):
        self.wb = load_workbook(excel_path)
        self.sheet = self.wb[sheetName]

    # pop the thead
    def getDataFromSheetWithOneCol(self):
        dataList = []
        for line in self.sheet:
            dataList.append(line[0].value)
        dataList.pop(0)
        return dataList

    #pop the thead
    def getDataFromSheetWithMultiCol(self):
        dataList = []
        for line in self.sheet:
            dataList.append([line[0].value, line[1].value])
        dataList.pop(0)
        return dataList
if __name__ == '__main__':
    excel_path = './../data/test_data.xlsx'
    sheetName = 'data_new'
    sheetName2 = 'data_sou'
    pe = ParseExcel(excel_path, sheetName)
    print(pe.getDataFromSheetWithOneCol())
    pe2 = ParseExcel(excel_path, sheetName2)
    print(pe2.getDataFromSheetWithMultiCol())