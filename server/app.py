from flask import Flask

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route to print a string and display it
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # prints the text in the console
    return f'<h1>{text}</h1>'  # displays the text in the browser

# Route to count numbers up to a given integer
@app.route('/count/<int:number>')
def count(number):
    numbers = '\n'.join([str(i) for i in range(1, number + 1)])
    return f'<pre>{numbers}</pre>'

# Route to perform math operations
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Cannot divide by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation'
    
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
