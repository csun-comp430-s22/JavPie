from Tokenizer import Interpreter

def main():
    while True:
        try:
            text = input('JavPie > ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()