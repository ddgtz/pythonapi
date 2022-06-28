"""
    02_celeb_auth.py
    Run this with 03_test_celeb_auth.py as the client.

    This demonstrates JWT (JSON Web Tokens).  Begin
    by issuing the /login URL with Basic Auth enabled (either from the client or from within Postman).
    This should give you back a token.
    This token will need to be supplied in the headers of a subsequent request with a
    header name of x-access-token, to each method that will require authentication.

    Mark methods that require authentication with the @auth_required decorator

    The basic auth for an admin user is:
    admin / admin
    The auth for a normal user is:   John / password

"""
import datetime
from functools import wraps
from pathlib import Path
import sys
import uuid

from flask import Flask, request, jsonify, make_response
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

student_files_dir = Path(__file__).parents[1]     # our student_files directory
db_file = student_files_dir / 'data/course_data.db'

if not db_file.exists():
    print(f'Database file does not exist at: {db_file}--exiting.', file=sys.stderr)
    sys.exit()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'              # should use  config['SECRET_KEY] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(db_file)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'user_auth'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class CelebrityModel(db.Model):
    __tablename__ = 'celebrity'
    paging_size = 20

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    pay = db.Column(db.Float)
    year = db.Column(db.String(15))
    category = db.Column(db.String(50))

    def __init__(self, name, pay, year, category):
        self.name = name
        self.pay = pay
        self.year = year
        self.category = category

class CelebritySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'year', 'pay', 'category')   # Fields to expose


celebrity_schema = CelebritySchema()
celebrities_schema = CelebritySchema(many=True)


def auth_required(orig_func):
    """
        Place this as a decorator above any function that requires authentication.
    """
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try: 
            data = jwt.decode(jwt=token,
                              key=app.config['SECRET_KEY'],
                              algorithms=['HS256'])

            current_user = User.query.filter_by(public_id=data.get('public_id')).first()
        except Exception as err:
            print('Token is invalid--> ', err)
            return jsonify({'message': 'Token is invalid!'}), 401

        return orig_func(current_user, *args, **kwargs)

    return wrapper


@app.route('/api/user', methods=['GET'])
@auth_required
def get_all_users(current_user):

    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()

    results = []

    for user in users:
        user_data = {'public_id': user.public_id, 'name': user.name, 'password': user.password, 'admin': user.admin}
        results.append(user_data)

    return jsonify({'users': results})


@app.route('/api/user/<public_id>', methods=['GET'])
@auth_required
def get_one_user(current_user, public_id):

    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    return celebrity_schema.jsonify(user)


@app.route('/api/user', methods=['POST'])
@auth_required
def create_user(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Must be admin to create a user!'})

    name, password, admin = None, None, None
    try:
        name, password, admin = request.form.get('name'), request.form.get('password'), request.form.get('admin')
        admin = bool(admin.capitalize() == 'True')
    except Exception as err:
        return jsonify({'message': 'Unable to create user, check data values supplied!', 'name': name,
                        'admin': admin, 'err_msg': str(err)})

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), name=name, password=hashed_password, admin=admin)

    user_check = User.query.filter_by(public_id=new_user.public_id).first()
    if user_check:
        return jsonify({'message': 'User already exists!'})

    try:
        db.session.add(new_user)
        db.session.commit()
        message = 'New user added!'
    except Exception as err:
        message = f'Error adding new user.  Message: {err}'

    return jsonify({'message': message, 'public_id': new_user.public_id, 'name': new_user.name})


@app.route('/api/user/<public_id>', methods=['DELETE'])
@auth_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message': 'Must be admin to delete a user!'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'User not found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'The user was deleted!'})


@app.route('/api/login')
def login():
    auth = request.authorization          # credentials from auth (Basic Auth) headerneed to be sent with TLS enabled!

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode(payload={'public_id': user.public_id,
                                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           key=app.config['SECRET_KEY'],
                           algorithm='HS256')
        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


@app.route('/api/celebrities', methods=['GET'])
@auth_required
def get_all_celebrities(current_user):
    page = request.args.get('page') or '1'
    celebrities = CelebrityModel.query.paginate(int(page), CelebrityModel.paging_size)
    return jsonify(message='authenticated for get_all_celebrities',
                   celebrities=celebrities_schema.dump(celebrities.items))


@app.route('/api/celebrities/<id>', methods=['GET'])
@auth_required
def get_one_celeb(current_user, id):
    celeb = CelebrityModel.query.get(id)

    if not celeb:
        return jsonify({'message': 'No celebrity found!'})

    return celebrity_schema.jsonify(celeb)


@app.route('/api/celebrities/<id>', methods=['PATCH'])
@auth_required
def update_pay(current_user, id):
    celeb = CelebrityModel.query.get(id)

    if not celeb:
        return jsonify({'message': 'No celebrity found!'})

    pay = request.form.get('pay')
    if pay:
        celeb.pay = pay
        db.session.commit()
        return jsonify({'message': 'Celebrity pay updated.!'})

    return jsonify({'message': 'No pay update occurred.'})


app.run(host='localhost', port=8051)
