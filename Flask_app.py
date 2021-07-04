from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def goedu():

    return "<h1>Hello!<h1/><br/><h2> Welcome to Jupiter!</h2>"


@app.route("/courses")
def course():

    return "<h1>FLASK BASIC TUTORIAL</h1>"


@app.route("/user/<name>")
def user(name):

    return f"<h1>Hello {name}! Welcome to Mars!</h1>"


@app.route('/results/<int:marks>')
def results(marks):

    return redirect(url_for('success', marks=marks))


@app.route('/success/<int:marks>')
def success(marks):
    final = ""
    if marks < 45:
        final = 'Fail'
    else:
        final = 'Pass'
    return "<h1/>Student has result<h1/>"+str(final)


@app.route("/about")
def about():
    return render_template('about.html')

# Asking the application to run the program


if __name__ == "__main__":

    app.run(debug=True, port=8000)
