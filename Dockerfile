FROM python:3.6.1

RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list

RUN apt-get update
RUN apt-get install mysql-client -y

RUN mkdir /code/
WORKDIR /code/

ADD ./.keys/id_rsa /etc/id_rsa

RUN find . -name '*.pyc' -delete

RUN mkdir -p ${HOME}/.ssh/
RUN cp /etc/id_rsa ${HOME}/.ssh/id_rsa
RUN chmod 400 ${HOME}/.ssh/id_rsa
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> ${HOME}/.ssh/config

ADD ./requirements/ /code/requirements/

RUN pip install -r /code/requirements/tests.txt

RUN rm -rf /etc/id_rsa
RUN rm -rf ${HOME}/.ssh
