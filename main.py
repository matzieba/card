from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    is_main = True
    return render_template('index.html', is_main=is_main)

@app.route("/manager")
def manager():
    is_main = False
    return render_template('manager.html', is_main=is_main)

@app.route("/developer")
def developer():
    is_main = False
    return render_template('developer.html', is_main=is_main)

if __name__ == "__main__":
    app.run(debug=True)

