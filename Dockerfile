FROM python:3.11.5

WORKDIR /home/

RUN echo "dkanrjsk"

RUN git clone https://github.com/YunHarry/techit.git

WORKDIR /home/techit/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=techit.settings.deploy.py"]
CMD ["bash", "-c", "python manage.py migrate --settings=techit.settings.deploy.py"]
CMD ["bash", "-c", "gunicorn --env DJANGO_SETTINGS_MODuLE=techit.settings.deploy techit.wsgi --bind 0.0.0.0:8000"]