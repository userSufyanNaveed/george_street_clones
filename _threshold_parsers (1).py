from default_parsers import parse_comma_list, UserInputException
import datetime


def parse_threshold_format(_format: str):
    formats = parse_comma_list(_format)
    options = ['.xls', '.pdf']
    for x in formats:
        if x not in formats:
            raise UserInputException(f"Each format in list of formats must be one of {options}, given <{x}>")
    return formats


def parse_download_month(month: str):
    try:
        datetime.strptime(month, '%m-%Y')
    except ValueError:
        raise UserInputException(f'Date "{month}" not recognized, must be entered in MM-YYYY format.')
    return month
    ###if month not in format (YYYY-MM):
    ###    raise UserInputException(f'Month "{month}" not recognized, must be 01 through 12')

def parse_download_type(type: str):
    formats = parse_threshold_format(type)
    options = ['specials', 'regular']
    for x in formats:
        if x not in formats:
            raise UserInputException(f'Type "{type}" not recognized. Must be one of {options} given <{x}>')
    return formats