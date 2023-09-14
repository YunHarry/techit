FROM python:3.11.5

WORKDIR /home/

RUN git clone https://github.com/YunHarry/techit.git

WORKDIR/home/techit/

RUN pip install django django-bootstrap4 pillow

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]