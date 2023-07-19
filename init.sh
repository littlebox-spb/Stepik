sudo ln -fs /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/Hello.py   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 Hello:wsgi_first

#sudo /etc/init.d/mysql start