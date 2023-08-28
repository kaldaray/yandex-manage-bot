import re
from re import Match

regex_phone = re.compile('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')


def check_phone(text: str) -> Match[str] | None:
    return regex_phone.match(text)
