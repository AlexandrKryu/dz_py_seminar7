

opSelect = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: int(x) / int(y),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)}
string = ''


def expression(x):
    global string
    string = x
    string = string.replace(' ', '').strip()
    string = string.replace('+', ' + ') \
        .replace('-', ' - ') \
        .replace('*', ' * ') \
        .replace('/', ' / ')
    string = string.split()


def deleteElement(string, i):
    string.pop(i + 1)
    string.pop(i)


def operation(string, i, oper):
    if string[i] == oper:
        string[i - 1] = opSelect.get(oper)(int(string[i - 1]), int(string[i + 1]))
        deleteElement(string, i)
        return True


def calc_exp():
    while len(string) > 1:
        if '*' in string or '/' in string:
            for i in range(len(string)):
                if operation(string, i, '*'): break
                if operation(string, i, '/'): break

        elif '+' in string or '-' in string:
            for i in range(len(string)):
                if operation(string, i, '+'): break
                if operation(string, i, '-'): break
    return string[0]

