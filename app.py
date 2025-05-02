from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None, error=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1_str = request.form.get('num1')
        num2_str = request.form.get('num2')
        operation = request.form.get('operation')

        num1 = float(num1_str)
        num2 = float(num2_str)

        result = None
        error = None

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                error = "Error: ZeroDivisionError. Division by zero is not allowed."
            else:
                result = num1 / num2
        else:
            error = "ErrorL Invalid operation. Please select +, -, *, or /."

        return render_template('index.html', result=result, error=error, num1=num1_str, num2=num2_str, operation=operation)

    except ValueError:
        return render_template('index.html', result=None, error="Error: Please enter a valid number", num1=request.form.get('num1', ''), num2=request.form.get('num2', ''), operation=request.form.get('operation', '+'))
    except Exception as e:
        return render_template('index.html', result=None, error=f"Error: {e}", num1=request.form.get('num1', ''), num2=request.form.get('num2', ''), operation=request.form.get('operation', '+'))

if __name__ == '__main__':
    app.run(debug=True)