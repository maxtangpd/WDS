from flask_script import Manager
import os
from App import create_app
from flask_migrate import MigrateCommand

env = os.environ.get("FLASK_ENV", "development")

app = create_app(env)

manager = Manager(app = app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()