__author__ = 'Tommy Lundgren'

import wsgiref.simple_server

import wattle

app = wattle.App()

@app.route('/')
def home():
    return wattle.render_template('home.html')

@app.route('/test1')
def test1():
    param1 = 'This is the first parameter'
    param2 = 'The number is: '
    param3 = 100
    return wattle.render_template('test1.html', param1=param1, param2=param2, param3=param3)

if __name__ == '__main__':
    server = wsgiref.simple_server.make_server('', 8090, app)
    server.serve_forever()