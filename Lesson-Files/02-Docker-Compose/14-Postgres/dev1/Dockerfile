FROM python:alpine

COPY ./app/requirements.txt /app/requirements.txt 

WORKDIR /app

RUN pip install -r requirements.txt

ENV DEVICE="dev1"

COPY ./app/ /app

ENTRYPOINT [ "python" ]

HEALTHCHECK --interval=5s --timeout=3s CMD curl -f http://localhost:5000 || nc -zv localhost 5000 || exit 1

CMD [ "app.py" ]

