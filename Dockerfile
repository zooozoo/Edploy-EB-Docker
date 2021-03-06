FROM        zoozoo/base
MAINTAINER  shz0309@gmail.com

ENV         LANG C.UTF-8
ENV         DJANGO_SETTINGS_MODULE config.settings.dev

# 파일 복사 및 requirements설치
COPY        . /srv/app
RUN         /root/.pyenv/versions/app/bin/pip install -r /srv/app/requirements.txt

# pyenv local
WORKDIR     /srv/app
RUN         pyenv local app

# Nginx
RUN         cp /srv/app/.config/dev/nginx/nginx.conf /etc/nginx/nginx.conf
RUN         cp /srv/app/.config/dev/nginx/app.conf /etc/nginx/sites-available/
RUN         rm -rf /etc/nginx/sites-enabled/*
RUN         ln -sf /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf

#uWSGI
RUN         mkdir -p /var/log/uwsgi/app

#namage.py
WORKDIR     /srv/app/instagram_practice
RUN         /root/.pyenv/versions/app/bin/python manage.py collectstatic --noinput
RUN         /root/.pyenv/versions/app/bin/python manage.py migrate --noinput

#supervisor
RUN         cp /srv/app/.config/dev/supervisor/* /etc/supervisor/conf.d/
CMD         supervisord -n

EXPOSE      80