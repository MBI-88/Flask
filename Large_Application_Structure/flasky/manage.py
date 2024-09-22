# Script to make the aplication

# Modules
import sys, os, click, unittest
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate, upgrade

# Config

app = create_app(os.getenv('FLASK_ENV') or 'default') 
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context() -> dict:
    return dict(db = db , User = User, Role = Role)


@app.cli.command()
@click.option('--coverage/--no-coverage', default = False, help = 'Enable code coverage')
@click.argument('test_names', nargs = -1)
def test(coverage:bool, test_names:str) -> None:
    
    
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = -1
        sys.exit(subprocess.call(sys.argv))

    if test_names:
        tests = unittest.TestLoader().loadTestsFromName(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')

    unittest.TextTestRunner(verbosity = 2).run(tests)






