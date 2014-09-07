################################################################
# Dockerfile for the Visionary
# Ubuntu 14.04.1, Visionary, py3.4, postgres
# Version: 0.0.1
################################################################

# Set the base image to Ubuntu 14.04
FROM ubuntu:14.04

# File Author/Maintainer
MAINTAINER Ray Alez "raymestalez@gmail.com"

# to update everything down this line
ENV REFRESHED_AT 2014-08-30 
RUN apt-get update

# Install basic applications
apt-get install -y git build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip python-setuptools

# Copy the application folder inside the container
ADD . /visionary

# Get pip to download and install requirements:
RUN pip install -r /visionary/requirements.txt

RUN pip install uwsgi



# install postgres
# RUN apt-get install -y build-essential postgresql-contrib python3-dev
# RUN apt-get install -y postgresql  libpq-dev
# RUN apt-get install -y python-dev  python-pip
# RUN apt-get install -y libxml2-dev libxslt1-dev
# RUN apt-get install -y libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev  

# Pulling from git instead of mounting with -v flag
#RUN git clone git://github.com/django/django.git django-trunk
#RUN pip install -e django-trunk/

# Wagtail demo
#RUN cd ~/ && pip install -e git://github.com/torchbox/wagtail.git#egg=wagtail

## //
# RUN cd /wagtaildemo && pip install -r requirements/dev.txt

# CMD /etc/init.d/postgresql start && cd /vid && echo "Wagtail started on port 8000" && ./manage.py runserver 0.0.0.0:8000 

EXPOSE 80

# Set the default directory where CMD will execute
WORKDIR /visionary

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
# CMD python manage.py runserver 0.0.0.0:8000
