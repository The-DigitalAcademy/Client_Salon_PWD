from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/hair_salon')
def hair_salon():
    
   
    
 return render_template('hair_salon.html')

if __name__ == '__main__':
    app.run(debug=True)



