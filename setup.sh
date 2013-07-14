#Install Apache and modwsgi
apt-get -y install apache2 libapache2-mod-wsgi python-pip
pip install flask

#Make the directory for the app
mkdir -p /var/www/myapp
cp /vagrant/app.wsgi /var/www/myapp/
cp /vagrant/myapp.py /var/www/myapp/

#Configure apace to handle the app
cp -pR /vagrant/app.conf /etc/apache2/sites-enabled/000-default

#Restart Apache
service apache2 restart
