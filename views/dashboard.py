from main import app,lm

@app.route('/shizz')
def shizz():
    return 'crap'