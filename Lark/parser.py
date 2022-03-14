from lark import Lark

parser = Lark(open("rules.txt", 'r').read())
little_duck = parser.parse

test_files = ['test1.in', 'test2.in', 'test3.in', 'test4.in']

for i, test in enumerate(test_files):
    try:
        s = open('tests/' + test, 'r').read()
        little_duck(s).pretty()
        print("test no.", i + 1, ": Apropiado")
    except Exception:
        print("test no.", i + 1, ": No apropiado")
