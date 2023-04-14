FROM python:3.10

RUN pip install --upgrade pip
RUN pip install virtualenv

ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3

ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

# install dependencies
RUN pip install -r requirements.txt

# expose port
EXPOSE 5000

# run application
# CMD ["python", "app_light.py"]