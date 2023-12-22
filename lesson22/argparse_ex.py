from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--a', help='this is variable a to store int', default=50)
parser.add_argument('--b', help='this is variable b to store int', default=100)

arguments = parser.parse_args()
arguments_dict = arguments.__dict__
print(arguments_dict['a'] +arguments_dict['b'])
print(type(arguments.a))
print(type(arguments.b))