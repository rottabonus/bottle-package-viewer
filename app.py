from bottle import route, run, template, error, static_file, Bottle
from waitress import serve
import package_reader

status = package_reader.return_packages_info()
bottle_app = Bottle()

@route('/')
def packagesRoute():
    return template('packages_template', status=status)

@route('/packages/<name>')
def packageInfo(name):
    return template('info_template', status=status, name=name)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == '__main__':
    serve(bottle_app, host='0.0.0.0', port=80)
