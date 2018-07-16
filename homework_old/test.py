from openpyxl import Workbook, load_workbook
wb = Workbook()
sheet = wb.active

stimulusTimes = [1, 2, 3]
reactionTimes = [2.3, 5.1, 7.0]

for i in range(len(stimulusTimes)):
    sheet['A' + str(i + 1)].value = stimulusTimes[i]
    sheet['B' + str(i + 1)].value = reactionTimes[i]

wb.save('example.xlsx')