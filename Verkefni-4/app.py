from flask import Flask, render_template, sessions
import os
from datetime import datetime

app = Flask(__name__)

app.secret_key = os.urandom(8)
print(os.urandom(8))

vorur = [
    [0, "Peysa","peysa.jpg",2500],
    [1, "Buxur", "buxur.jpg",1500],
    [2, "Skór", "skor.jpg", 4500],
    [3, "Bolur", "bolur.jpg", 1500],
    [4, "Úlpa", "ulpa.jpg", 55000],
    [5, "Húfa", "hufa.jpg", 2550]

]

@app.route('/karfa')
def karfa():
    karfa= []
    summa = 0

    if 'karfa' in session:
        karfa=session['karfa']
        fjoldi = len(karfa)
        for i in karfa:
            summa += int(i[3])
        return render_template('karfa.html', k=karfa, tom=False, fjoldi =fjoldi, samtals=summa)
    else:
        return render_template('karfa.html', k=karfa, tom=True)

@app.route('/add/<int:id>')
def teljari(id):
    karfa=[]
    fjoldi=[]
    if 'karfa' in sessions:
        karfa = session['karfa']
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)
    return render_template('index.html')

@app.route('/eydavoru/<int:id>')
def delete(id):
    karfa=[]
    karfa = session['karfa']
    vara=0

    for i in range(len(karfa)):
        if karfa[i][0] == id:
            vara = i
    karfa.remove(karfa[vara])
    session['remove'] = karfa
    return redirect(url_for('karfa'))

@app.route('/')
def index():
    karfa = []
    fjoldi = []
    if 'karfa' in session:
        karfa = sessions['karfa']
        fjoldi = len(karfa)
    return render_template('index.html', v=vorur, fjoldi=fjoldi)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.errorhandler(500)
def page_not_found(error):
    return render_template('server_not_found.html'), 500

if __name__ == "__main__":
    app.run(debug=True)