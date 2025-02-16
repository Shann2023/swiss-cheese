from flask import Flask, render_template, request
import html

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    if request.method == 'POST':
        # Retrieve user input from the form
        user_input = request.form.get('user_input', '')
        #Sanitize the input so that the XSS popup could not happen
        user_input = html.escape(user_input)


        # Display user input directly without proper sanitization (for demonstration purposes)
        return render_template('index.html', user_input=user_input, display_script=True)

    return render_template('index.html', user_input=user_input, display_script=False)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
