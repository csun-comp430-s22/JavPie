import Tokenizer

while True:
    text = input('Javpie > ')
    result, error = Tokenizer.run(text)

    if error: print(error.as_string())
    else: print(result)