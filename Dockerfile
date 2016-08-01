FROM python:3.5
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE config.settings
ENV SECRET_KEY m87g_s@zf^9!%x9_u-q$3dea!__gg^7#op=tu5)n6b$*ounw3q
ENV DEBUG True
ENV DATABASE_URL postgres://postgres@db/postgres
RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project/
RUN apt-get update
RUN apt-get install -y pkg-config libfreetype6-dev libpng12-dev
RUN pip install -r requirements.txt
ADD . /project/
