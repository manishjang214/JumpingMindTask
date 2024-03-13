FROM python:3.10.12

WORKDIR /JumpingMind

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001

CMD python manage.py runserver