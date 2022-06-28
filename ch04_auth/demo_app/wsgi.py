"""

    The following demonstrates a Flask app that includes the use of Flask-SQLAlchemy
    and Flask-login and Flask-wtf (forms) to provide a mini-authentication app.

    It demonstrates how flask can be create properly across multiple files rather
    than via a single file as we have been doing.

    Our registered user is: name=Samwise, username=sam, password=mount.doom6000bc, email=samwise@midrth.com

"""
from ch04_auth.demo_app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', port=8051)
