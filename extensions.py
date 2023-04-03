import requests
import json
from config import keys
class ApiException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quate: str, base: str, amount:str):



        if quate == base:
            raise ApiException(f'нельзя конвертировать {base} в {base}')

        try:
            quate_ticker = keys[quate]
        except KeyError:
            raise ApiException(f'нельзя обработать валюту {quate}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ApiException(f'нельзя обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'нельзя обработать количество {amount}')
        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={quate_ticker}{base_ticker}&key=9e7a06049b2ff6dacd39f281ae83f87a')
        total = json.loads(r.content)['data']
        total = dict(total)
        total_base=''
        for value in  total.values():
            total_base += value
        total_base=float(total_base)
        return total_base