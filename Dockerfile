FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /modularblog
WORKDIR /modularblog
ADD requirements.txt /modularblog/
RUN pip install -r requirements.txt
ADD . /modularblog/
RUN chmod 755 run.sh
ENV DJANGO_SETTINGS_MODULE=modularblog.settings
