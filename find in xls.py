import openpyxl

# Open the workbook and the sheet you want to search
wb = openpyxl.load_workbook('RCCount_Beneficiary.xls')
sheet = wb['Sheet1']

# Iterate through the rows in the sheet
for row in sheet.rows:
  # Check each cell in the row to see if it contains the name you are searching for
  for cell in row:
    if cell.value == 'Bidhideb Ghosh':
      # If the cell contains the name, print the row number
      print(f'Found name in row {cell.row}')

# Close the workbook
wb.close()
