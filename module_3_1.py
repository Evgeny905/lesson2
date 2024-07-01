calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(x):
    count_calls()
    return len(x), x.upper(), x.lower()


def is_contains(stroka, spisok):
    count_calls()
    string = stroka.lower()
    for i in range(len(spisok)):
        if spisok[i].lower() == string:
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)