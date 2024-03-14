FROM python:3.10.12

RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install -g netlify-cli


WORKDIR /JumpingMind

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001

CMD python manage.py runserver