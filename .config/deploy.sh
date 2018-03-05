#!/usr/bin/env bash
# Nginx에 존재하던 모든 enabled 서버 설정 링크 삭제
sudo rm -rf /etc/nginx/sites-enabled/*
# 프로젝트의 Nginx 설정을 enabled에 링크
sudo cp -f /srv/ec2-deploy/.config/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
# uWSGI
sudo ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf
sudo cp -f /srv/ec2-deploy/.config/uwsgi.service /etc/systemd/system/uwsgi.service
# collectstatic을 위한 설정
cd /srv/ec2-deploy/app
#
/bin/bash -c \
'/home/ubuntu/.pyenv/versions/fc-ec2-deploy/bin/python \
/srv/ec2-deploy/app/manage.py collectstatic --noinput' ubuntu
#
sudo systemctl enable uwsgi
sudo systemctl daemon-reload
sudo systemctl restart uwsgi nginx