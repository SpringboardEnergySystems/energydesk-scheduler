# pull official base image
FROM springboardenergysystems/energyservices-slender:2.5

# create directory for the app user

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y dos2unix
RUN apt-get install gettext -y

# All normal Python dependencies are contained in the slim-image above. This installs GitHub code from django-apps
RUN pip3 install --upgrade pip
COPY ./mqttreceiver/buildconfig/requirements.git.txt ./requirements.txt
RUN pip3 install --upgrade --force-reinstall -r requirements.txt


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the appropriate directories
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/logs
WORKDIR $APP_HOME



RUN echo "HOME : $APP_HOME"
RUN chmod 777 $APP_HOME

# copy project
COPY ./mqttreceiver/ $APP_HOME
COPY ./mqttreceiver/buildconfig/entrypoint.sh $APP_HOME/entrypoint.sh


# chown all the files to the app user
RUN chmod 777 $APP_HOME
RUN chmod 777 $APP_HOME/entrypoint.sh

# change to the app user

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
