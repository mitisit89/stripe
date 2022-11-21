FROM python:3.10-slim-bullseye
RUN mkdir -p  tmp/stripe
WORKDIR /tmp/stripe
COPY . /tmp/stripe 
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN  pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN chmod a+x *.sh
RUN sh setup.sh
