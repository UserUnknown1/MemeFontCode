from urllib.request import urlopen

import bs4


def fate(sign=None):
    zodiac_signs = {
        "aries": 1,
        "taurus": 2,
        "gemini": 3,
        "cancer": 4,
        "leo": 5,
        "virgo": 6,
        "libra": 7,
        "scorpio": 8,
        "sagittarius": 9,
        "capricorn": 10,
        "aquarius": 11,
        "pisces": 12,
    }
    zodiac = zodiac_signs.get(sign)
    if zodiac is None:
        inp = input("Please enter a valid sign: ")
        fate(inp.lower())
    else:
        url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={zodiac}"
        with urlopen(url) as response:
            body = response.read()
            soup = bs4.BeautifulSoup(body, "lxml")
            ingredients = soup.find_all("p")
            print(ingredients[0].get_text())


user_input = input("Please enter your zodiac: ")
fate(user_input.lower())
