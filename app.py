from crypt import methods
from urllib import response
from flask import Flask, request, render_template, redirect, flash
from surveys import *
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY']='ketchup'
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def welcome_page():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('base.html', instructions=instructions, title=title)

num = 0
length = len(satisfaction_survey.questions)

@app.route('/questions/<int:num>')
def show_question(num):
    question = satisfaction_survey.questions[num].question
    choices = satisfaction_survey.questions[num].choices
    if responses is None:
        return redirect('/')
    if len(responses) != num:
        flash("Invalid question!")
        return redirect(f'questions/{len(responses)}')
    return render_template('question.html', question=question, choices=choices, num=num)

@app.route('/answer/<int:num>', methods=['POST'])
def answer_page(num):
    result = request.form.getlist('choice')
    responses.append(result)
    num += 1
    if num == length:
        return redirect('/thank-you')
    else:
        url = f'/questions/{num}'
        return redirect(url)

@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')




