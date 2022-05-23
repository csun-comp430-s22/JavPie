import JavPie

while True:
    text = input('Javpie > ')
    result, error = JavPie.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)