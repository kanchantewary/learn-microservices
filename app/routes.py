from app import app

@app.route('/') #decorators
@app.route('/index') #decorators
def index():
    return 'Hello world!'
