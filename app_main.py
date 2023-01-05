from flask import Flask
from time import sleep
from bs4 import BeautifulSoup as soup



html = soup(open('static/ui.html', 'r', encoding='utf-8').read(), features='html.parser')
app = Flask(__name__)

def output(button_key):
    # finds <textarea id="output"> and changes its value according to the pressed button 
    output_tag = html.find('textarea', attrs={'id': 'output'})
    output_tag.string.replace_with(button_key)
    print(f'    {output_tag}')
    sleep(2)
    output_tag.string.replace_with(' ')



@app.route('/', methods=['GET','POST'])
def ui():
    return str(html)

@app.route('/a')
def a():
    #playsound(f'{getcwd()}/A.wav') # actual path + sound file name
    output('a')

    return ('')

@app.route('/b')
def b():
    #playsound(f'{getcwd()}/B.wav')
    output('b')

    return ('')

@app.route('/c')
def c():
    #playsound(f'{getcwd()}/C.wav')
    output('c')

    return ('')

@app.route('/d')
def d():
    output('d')
    
    return ('')


if __name__ == '__main__':
    app.run()