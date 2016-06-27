__author__ = 'Tommy Lundgren'

import wsgiref.simple_server

import wattle
import wattle.ext.authentication

app = wattle.App()
auth = wattle.ext.authentication.Authentication(app)


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
    c = wattle.Cookie('test', 'ilikecookies2')
    wattle.response.add_cookie(c)
    return wattle.render_template('simple_page.html', title='Cookie test')


@auth.require
@app.route('/auth')
def auth_test():
    return wattle.render_template('simple_page.html', title='Auth test')

if __name__ == '__main__':
    server = wsgiref.simple_server.make_server('', 8090, app)
    server.serve_forever()