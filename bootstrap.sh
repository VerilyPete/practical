#!/usr/bin/env bash

apt-get update
apt-get install -y apache2 git
if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi
git clone https://github.com/tastejs/todomvc.git
cp -R ./todomvc/examples/angular2/ /var/www/
sudo rm -fr ./todomvc/
