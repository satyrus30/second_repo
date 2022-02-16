'''

В этой ката вы должны, учитывая строку, заменить каждую букву ее позицией в алфавите.

Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.

«а» = 1, «б» = 2 и т. д.

'''


def alphabet_position(text):
    def apply(i):
        i = i.lower()
        if ord(i) < 97 or 122 < ord(i):
            return i.replace(i, '')
        else:
            return ord(i) - 96
    arr = list(map(apply, text))

    item = 0
    while item < len(arr):
        if type(arr[item]) != int:
            if item == 0:
                arr.pop(item)
                item = 0
            else:
                arr.pop(item)
                item -= 1
        else:
            item += 1
    return ' '.join(map(str, arr))
