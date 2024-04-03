#!/usr/bin/env python3
#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/count/<int:number>')
def count_to(number):
    return '\n'.join(str(num) for num in range(number)) + '\n'

@app.route('/print/hello')
def print_hello():
    print('hello')
    return 'hello'

@app.route('/math/<int:num1>/<op>/<int:num2>')
def math_operation(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == 'div' and num2 != 0:
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        abort(404)
        return
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)



