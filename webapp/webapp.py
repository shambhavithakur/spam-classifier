from text_classifier import classify_text
from flask import Flask, render_template, url_for, request, escape

app = Flask(__name__)


@ app.route('/')
@ app.route('/index')
def display_form() -> 'html':
    '''Displays a form that lets users interact with this app'''
    return render_template('index.html', the_title='Spam Classifier')


@ app.route('/result')
def display_blank() -> 'html':
    '''Displays the initial version of the results page, when no user request has been received'''
    return render_template('result.html', the_title='Waiting to classify text...', the_result='Tap the following button to begin classifying a text snippet.', button_text='Go to classifier', no_input=True)


@ app.route('/result', methods=['POST'])
def display_result() -> 'html':
    '''Handles the result of a user request—stores the divisors and displays the result in HTML format'''

    title = 'Could not classify text'

    text_class = ''
    snippet = ''
    details = ''

    try:
        pred, data = classify_text(request)
        if pred == 1:
            text_class = 'spam'
            title = 'It is spam.'
        else:
            text_class = 'ham'
            title = 'It is not spam.'
        snippet = ''.join(data)
    except Exception as e:
        print('*****Could not obtain prediction', str(e))

    details = f'The text that you gave us for classification has a 98% chance of being {text_class}. Here is the text for your reference:'

    return render_template('result.html', the_title=title, detailed_response=details, snippet=snippet, button_text="Classify another text snippet", no_input=False)


if __name__ == "__main__":
    app.run(debug=True)
