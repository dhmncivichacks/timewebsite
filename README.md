# timewebsite
Alpha website, NE Wisc creatives / TIME community (tech, innovators, makers, entrepreneurs)

```
 ___________________________________________________________
/ It's T.I.M.E!                                             \
|                                                           |
| N.E. Wisconsin's Community of...                          |
|                                                           |
\ [T]echnologists, [I]nnovators, [M]akers, [E]ntrepreneurs! /
 -----------------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```

See [the wiki](https://github.com/mikeputnam/timewebsite/wiki) for more details of the intent of this project.

This community web site project encourages participation and contribution no matter your experience level with web development. If you have a question, need some help, or want to participate some other way, open an [issue](https://github.com/dhmncivichacks/timewebsite/issues) and ask away! If you know you way around web development, look for something that needs fixing, fix it and open a [pull request](https://github.com/dhmncivichacks/timewebsite/pulls)!

As a learning-friendly endeavor, the project is based on the learnings acquired from following this excellent tutorial series of Youtube videos: https://github.com/realpython/discover-flask

## Development Tools:
- [Atom](https://atom.io/) editor + [linter-flake8](https://atom.io/packages/linter-flake8) Atom package (or the editor of your choice)
- [git](https://git-scm.com/) and an account here on Github.
- [Python 3.5.1](https://www.python.org/)
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)

#### Setup tools on Mac OSX:
1. FIXME

#### Setup tools on Windows:
1. Install [Python 3.5.1](https://docs.python.org/3/using/windows.html) (make sure you check `[x] Add to PATH!`)
1. Open a "Command Prompt" (not Powershell)
1. Ensure Python is working
  - Type `python --version` and press Enter. You should see a confirmation that Python is working. If instead you see something like `'python' is not recognized...` repeat Step 1. making sure to check [x] Add to PATH`.
1. Type `pip install virtualenvwrapper-win`
1. FIXME howto virtualenv on windows
1. (Optional) Install [Atom](https://atom.io/) editor + [linter-flake8](https://atom.io/packages/linter-flake8) Atom package

#### Setup tools on Linux (Ubuntu 14.04.4 LTS):
1. Install Python 3.5.1
1. `pip install virtualenvwrapper`
1. Add to your .bashrc or equivalent
```
export WORKON_HOME=$HOME/venv
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3' # This needs to be placed before the virtualenvwrapper command
source /usr/local/bin/virtualenvwrapper.sh
```
1. (Optional) Install [Atom](https://atom.io/) editor + [linter-flake8](https://atom.io/packages/linter-flake8) Atom package

## Setup the project on your computer

#### Fork the repository

1. Create an account on Github and add your SSH keys. These are used to authenticate your git commands with Github. Github has nice documentation on this step.
1. Log in to Github
1. Visit https://github.com/dhmncivichacks/timewebsite
1. Click the word "Fork" in the upper right of this page. This makes a copy of the source code under your user account with Github.

#### From your command prompt:

1. "Make a directory" for storing your source code:

  `mkdir src`

1. "Change directory" into your source code directory:

  `cd src`

1. Download your forked copy to your source code directory:

  `git clone git@github.com:<YOUR GITHUB USERNAME>/timewebsite.git`

1. "Change directory" into the project:

  `cd timewebsite`

1. Create a Python virtualenv to run the project within.

  `mkvirtualenv timewebsite`

  When you return to work on the project again, you will need to re-activate the same virtualenv. This is done by running `workon timewebsite` before attempting to run the project.

1. Install all the Python packages the project uses.

  `pip install -r requirements.txt`

1. Create the local sqlite development database (one time):

  `APP_SETTINGS="config.DevelopmentConfig" DATABASE_URL="sqlite:///posts.db" python db_create.py`

1. Create the test users (one time):

  `APP_SETTINGS="config.DevelopmentConfig" DATABASE_URL="sqlite:///posts.db" python db_create_users.py`

1. Run the application!

  `APP_SETTINGS="config.DevelopmentConfig" DATABASE_URL="sqlite:///posts.db" python run.py`

Now you should be able to view the application in your browser at http://localhost:5000

Try logging in with username `admin` password `admin`

## Unit tests and code coverage


- Run the tests

  `APP_SETTINGS="config.DevelopmentConfig" DATABASE_URL="sqlite:///posts.db" python manage.py test`

- Run the test coverage report

  `APP_SETTINGS="config.DevelopmentConfig" DATABASE_URL="sqlite:///posts.db" python manage.py cov`
