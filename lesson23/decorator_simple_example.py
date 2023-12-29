


def add_and_symbol(func):
    def inner(*args):
        header, footer = '&'*20, '&'*20
        return f'{header}\n{func(*args)}\n{footer}'
    return inner


def add_footer_header(sign, quantity):
    def middle_level(func):
        def inner(msg):
            header = sign*quantity
            footer = sign * quantity
            return f'{header}\n{func(msg)}\n{footer}'
        return inner
    return middle_level

@add_footer_header('$', 20)
@add_and_symbol
def hi(msg):
    return '1 ' + msg + ' 2'
print(hi('hello there'))