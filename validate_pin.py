'''
Банкоматы позволяют использовать 4- или 6-значные PIN-коды, а PIN-коды не могут содержать ничего,
кроме ровно 4 или ровно 6 цифр.
Если функции передана допустимая строка PIN-кода, верните true, иначе верните false.
'''


def validate_pin(pin: str) -> bool:
    try:
        if len(pin) == 4 or len(pin) == 6:
            specSymb = [' ', '\n', '-', '+']
            pinArr = list(pin)

            for iPinArr in pinArr:
                if iPinArr in specSymb:
                    return False
                else:
                    continue

            try:
                pin = int(pin)
                if pin == int(pin):
                    return True
            except:
                return False

        else:
            return False
    except:
        return False