FROM python:3.8

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /src/staticfiles
COPY manage.py /src/manage.py
COPY static /src/static
COPY templates /src/templates
COPY ButtonPressWeb /src/ButtonPressWeb
COPY auth /src/auth
COPY button_clicks /src/button_clicks

WORKDIR /src

EXPOSE 80
CMD ["gunicorn", "ButtonPressWeb.wsgi", "-b", "0.0.0.0:80"]
