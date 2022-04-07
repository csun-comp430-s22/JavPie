import Tokenizer

while True:
    text = input('Javpie > ')
    result, error = Tokenizer.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)