from bottle import route, run, template
import package_reader

status = package_reader.return_packages_info()

@route('/')
def packagesRoute():
    return template('packages_template', status=status)

@route('/<name>')
def packageInfo(name):
    return template('info_template', status=status, name=name)

run(host='0.0.0.0', port=3000, debug=True)
