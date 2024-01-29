
def symbols_check(forbidden, login):
    for c in forbidden:
        if c in login:
            return True
    return False

forbidden = '=?*^$№@_'
login = str(input('логин '))

if symbols_check(forbidden, login):
    print(f'запрещенные символы {forbidden} присутствуют в логине')