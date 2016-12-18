import openpyxl
from jinja2 import Environment, FileSystemLoader


def generate_config(model=None,config_sheet=None):
    env = Environment(loader=FileSystemLoader('./template/'))
    # Modelによって場合分けできるようにする
    config_template = env.get_template('c2960-8tc-l.template.txt')

    parameters = {}

    basic_settigs(parameters=parameters,config_sheet=config_sheet)

    generated_config = config_template.render(parameters)
    return generated_config


def basic_settigs(parameters=None,config_sheet=None):
    # 基本設定の項目を抜き出す
    for i in range(1,60):
        cell = "C" + str(i)
        if('hostname'==config_sheet[cell].value):
            hostname = config_sheet["D" + str(i)].value
            parameters['hostname'] = hostname
        if('enable password'==config_sheet[cell].value):
            enable_password = config_sheet["D" + str(i)].value
            parameters['enable_password'] = "enable password " + enable_password
            print(parameters['enable_password'])
        if('default gateway'==config_sheet[cell].value):
            ip_default_gateway = config_sheet["D" + str(i)].value
            parameters['ip_default_gateway'] = "ip default-gateway " + ip_default_gateway
            print(parameters['ip_default_gateway'])
        if('NTP server'==config_sheet[cell].value):
            ntp_server = config_sheet["D" + str(i)].value
            parameters['ntp_server'] = "ntp server " + ntp_server
            print(parameters['ntp_server'])
        if('timezone'==config_sheet[cell].value):
            timezone = config_sheet["D" + str(i)].value
            parameters['timezone'] = "clock timezone " + timezone
            print(parameters['timezone'])
        if('loggig buffer size'==config_sheet[cell].value):
            logging_buffed_size = config_sheet["D" + str(i)].value
            parameters['logging_buffered_size'] = "logging buffered " +  logging_buffed_size
            print(parameters['logging_buffered_size'])
        if('logging timestamps'==config_sheet[cell].value):
            logging_timestamps = config_sheet["D" + str(i)].value
            parameters['logging_timestamps'] = logging_timestamps
            print(parameters['logging_timestamps'])
