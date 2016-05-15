# timewebsite [![Build Status](https://travis-ci.org/dhmncivichacks/timewebsite.svg?branch=master)](https://travis-ci.org/dhmncivichacks/timewebsite)
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

See [the wiki](https://github.com/dhmncivichacks/timewebsite/wiki) for more details of the intent of this project.

This community web site project encourages participation and contribution no matter your experience level with web development. If you have a question, need some help, or want to participate some other way, open an [issue](https://github.com/dhmncivichacks/timewebsite/issues) and ask away! If you know you way around web development, look for something that needs fixing, fix it and open a [pull request](https://github.com/dhmncivichacks/timewebsite/pulls)!

As a learning-friendly endeavor, the project is based on the learnings acquired from following this excellent tutorial series of Youtube videos: https://github.com/realpython/discover-flask

## Prerequisites:

#### On Linux, \*BSD, Mac OS X, and Windows:
1. Install [Docker Engine](https://docs.docker.com/engine/installation/)
1. (If Linux or \*BSD) Install [Docker Compose](https://docs.docker.com/compose/install/)
1. Install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
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

1. Build/Run the docker container

  `docker-compose up`

1. Create the local sqlite development database (one time):

  `docker-compose exec web python db_create.py"`

1. Find the IP address assigned to the running docker container

  `docker inspect -f 'http://{{ .NetworkSettings.Networks.timewebsite_default.IPAddress}}:5000' timewebsite_web_1`

Now you should be able to view the application in your browser using the IP address just discovered!

Try logging in with username `admin` password `admin`

## Unit tests and code coverage


- Run the tests

  `docker-compose exec web python manage.py test`

- Run the test coverage report

  `docker-compose exec web python manage.py cov`
