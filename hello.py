from bottle import route, run, template
import package_reader


@route('/hello')
def hello():
    count_of_packages = package_reader.return_packages_list()
    return template('hello_template', count_of_packages=count_of_packages)

run(host='0.0.0.0', port=3000, debug=True)
