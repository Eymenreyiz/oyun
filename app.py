from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def anasayfa():
    return render_template('anasayfa.html')

@app.route('/xox')
def xox():
    return render_template('xox.html')

@app.route('/yilan')
def yilan():
    return render_template('yilan.html')

if __name__ == '__main__':
    app.run(debug=True)
