# Usage:
# docker build --build-arg APP_SETTINGS=config.DevelopmentConfig . -t appletonmakerspace/timewebsite
#
# The "onbuild" image automatically runs pip install -r requirements.txt for us
FROM python:3.5.2-onbuild
COPY . /usr/src/app
ARG APP_SETTINGS
ENV APP_SETTINGS=$APP_SETTINGS
ENTRYPOINT python run.py
EXPOSE 5000
