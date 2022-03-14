from lark import Lark

parser = Lark(open("rules.txt", 'r').read())
little_duck = parser.parse

test_files = ['test1.in', 'test2.in', 'test3.in', 'test4.in']

for test in test_files:
    try:
        s = open('tests/' + test, 'r').read()
        little_duck(s).pretty()
        print("Apropiado")
    except Exception:
        print("No apropiado")
