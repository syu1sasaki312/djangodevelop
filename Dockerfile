FROM python:3.9.16
ENV PYTHONUNBUFFERED 1
RUN mkdir /workspace
WORKDIR /workspace
ADD . /workspace/
RUN pip install --upgrade pip
RUN pip install django-adminlte-3
RUN pip install django-widgets-improved
RUN pip install -r requirements.txt
