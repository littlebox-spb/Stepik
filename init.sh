sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/hello.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 hello:wsgi_first
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application

#sudo /etc/init.d/mysql start