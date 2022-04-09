#from Parser import Parser
import Parser2


while True:
    text = input('Javpie > ')
    result, error = Parser2.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)

