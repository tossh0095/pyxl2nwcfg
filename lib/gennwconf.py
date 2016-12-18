from lib import pyxl2catalystcfg
import sys
import openpyxl

def generate_config(model=None,config_sheet=None):
    if(model==None):
        print("model is not defined")
        sys.exit()
    else:
        # 将来的にはmodelでgenerateするコンフィグを分ける
        return pyxl2catalystcfg.generate_config(model=model,config_sheet=config_sheet)
