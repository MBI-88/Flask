# Modules
import sys,os,click,unittest
from app import create_app,db
from app.models import User,Role,Follow,Permission,Comment,Post
from flask_migrate import Migrate,upgrade


# Config

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True,include='app/*')
    COV.start()

app = create_app(os.getenv('FLASK_ENV') or 'default') 
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context() -> dict:
    return dict(db = db ,User = User,Follow=Follow,Role=Role,Permission=Permission,Post=Post,Comment=Comment)


@app.cli.command()
@click.option('--coverage/--no-coverage', default = False, help = 'Enable code coverage')
@click.argument('test_names', nargs = -1)
def test(coverage:bool, test_names:str) -> None:
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    if test_names:
        tests = unittest.TestLoader().loadTestsFromName(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')

    unittest.TextTestRunner(verbosity = 2).run(tests)
    
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir,'temp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html'% covdir)


@app.cli.command()
@click.option('--length',default = 25,help = 'Number of functions to include in the profiler report')
@click.option('--profile-dir',default = None, help = 'Directory where profiler data, files are saved')
def profile(length:int,profile_dir:str) -> None:
    from werkzeug.middleware.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app,restrictions = [length],profile_dir = profile_dir)
    
    app.run()


@app.cli.command()
def deploy() -> None:
    upgrade()
    Role.insert_roles()
    
    User.add_self_follows()