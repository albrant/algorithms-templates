from xml.etree import ElementTree
from decimal import Decimal
import requests
import datetime


def get_code_and_value(element_item) -> [str]:
    return element_item[1].text, element_item[4].text


def currency_rates(user_code: str):
    if len(user_code) != 3:
        return None

    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    tree = ElementTree.XML(response.text)

    user_code = user_code.upper()
    date_str = tree.get('Date').split('.')
    date = datetime.date(day=int(date_str[0]), month=int(date_str[1]), year=int(date_str[2]))

    for item in tree:
        code, value = get_code_and_value(item)

        if code == user_code:
            value = Decimal('.'.join(value.split(',')))
            value = value.quantize(Decimal("1.00"))
            return [value, date]

    return None