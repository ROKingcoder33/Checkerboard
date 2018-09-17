from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<int:x>/<int:y>')
def youChoose(x, y):
    return render_template('index.html', title='yourChoice',
                           x_coor=x, y_coor=y)


if __name__ == '__main__':
    app.run(debug=True)
