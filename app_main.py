from flask import Flask
from bs4 import BeautifulSoup as soup



# opening UI file as a beautifulsoup obj
html = soup(open('.\\static\\ui.html', 'r', encoding='utf-8').read(), features='html.parser')
app = Flask(__name__)

def output(button_key):
    # finds <textarea id="output"> 
    output_tag = html.find('textarea', attrs={'id': 'output'})

    # changes output tag value to the according pressed key
    output_tag.string.replace_with(button_key)

    # prints the entire tag already changed for debugging
    print(f'    {output_tag}')



@app.route('/', methods=['GET','POST'])
def ui():
    # returning str of html obj in the UI because flask doesnt accept anything else
    return str(html)

@app.route('/a')
def a():
    # button A onclick function 
    output('a')

    return ('') # a.k.a. return 0

@app.route('/b')
def b():
    # button B onclick function 
    output('b')

    return ('') # a.k.a. return 0

@app.route('/c')
def c():
    # button C onclick function 
    output('c')

    return ('') # a.k.a. return 0

@app.route('/d')
def d():
    # button D onclick function 
    output('d')

    return ('') # a.k.a. return 0


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)