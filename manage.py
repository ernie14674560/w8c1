from simpledu.app import create_app
from flask import render_template
app = create_app('development')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
