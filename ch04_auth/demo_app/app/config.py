from pathlib import Path
import sys

student_files_dir = Path(__file__).parents[3]     # our student_files directory
db_file = student_files_dir / 'data/course_data.db'

if not db_file.exists():
    print(f'Database file does not exist at: {db_file}--exiting.', file=sys.stderr)
    sys.exit()

class Config:
    SECRET_KEY = b'our_secret_key'
    DEBUG = False
    FLASK_DEBUG = 1
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Normally, make an environment variable for this
    # and use os.environ.get('SQLALCHEMY_DATABASE_URI')
    # For different databases, different URIs will be used,
    # for example: mysql://username:password@server/db
    # For more on these configuration keys, see:
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#configuration-keys
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(db_file)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

