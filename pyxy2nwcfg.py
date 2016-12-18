import openpyxl
import sys
from lib import gennwconf

target_xlsx = sys.argv[1]

config_sheet = openpyxl.load_workbook(target_xlsx)['config']

# パラメータシートからmodelを調べる

for i in range(1,60):
    cell = "C" + str(i)
    if('model'== config_sheet[cell].value):
        target_model = config_sheet["D" + str(i)].value
        break

generated_config = gennwconf.generate_config(model=target_model,config_sheet=config_sheet)

destination_cofig_file = target_xlsx.split('.')[0] + '.txt'

print(destination_cofig_file)
file = open(destination_cofig_file, 'w')
file.write(generated_config)
