from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html", times=int(3), colorj = "#9fc5f8")


@app.route('/play/<times>')
def playrepeat(times):
    return render_template("index.html", times = int(times), colorj = "#9fc5f8")

@app.route('/play/<times>/<colorc>')
def playrepeatcolors(times, colorc):
    return render_template("index.html", times = int(times), colorj = colorc)



if __name__=="__main__":
    app.run(debug=True)