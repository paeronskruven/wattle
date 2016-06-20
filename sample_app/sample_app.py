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

@app.route('/cookie')
def cookie_test():
    wattle.Cookie('test', 'ilikecookies')
    return wattle.render_template('simple_page.html', title='Cookie test')

@app.route('/cookie2')
def cookie_test_modify():
    c = wattle.cookie_collection['test']
    c.value = 'a new value'
    return 'wiie'

if __name__ == '__main__':
    server = wsgiref.simple_server.make_server('', 8090, app)
    server.serve_forever()