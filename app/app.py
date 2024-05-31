from flask import Flask,render_template
from config import config

app=Flask(__name__)

#@app.route('/')
def index():
    return render_template('index.html')

def page_not_found(error):
    return render_template('404.html'),404
if __name__=='__main__':
    app.config.from_object(config['development'])
    
    #Error handlers
    app.register_error_handler(404,page_not_found)

    app.run(debug=True)
