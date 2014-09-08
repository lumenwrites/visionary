############################################################
# Dockerfile to build Nginx Installed Containers
# Based on Ubuntu
# to run:
# sudo docker build -t visionary_server_img .
# sudo docker run --name visionary_server_insance -p 80:80 -i -t visionary_server_img
############################################################

# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Ray Alez

ENV REFRESHED_AT 2014-09-0

run apt-get update

# Install necessary tools, nginx
RUN apt-get install -y emacs wget dialog net-tools
run apt-get install -y build-essential git libpq-dev
run apt-get install -y python3.4 python3.4-dev python-setuptools
run apt-get install -y python-software-properties
run apt-get install -y nginx supervisor

ADD https://github.com/pypa/pip/raw/645180e2714b4ffcf40363a608239e089c9dafab/contrib/get-pip.py /root/get-pip.py
RUN python3.4 /root/get-pip.py

# install uwsgi now because it takes a little while
run pip3.4 install uwsgi


# Pull visionary
run cd
run git clone https://github.com/raymestalez/visionary.git

run cd /visionary && pip3.4 install -r requirements.txt

# Configure nginx
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
#run ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/
#run ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/

# Expose ports
EXPOSE 80

# Set the default command to execute
# when creating a new container
#CMD service nginx start

