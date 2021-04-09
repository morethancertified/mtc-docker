FROM python

# ensure i mention why this is important...layers
COPY ./app/requirements.txt /app/requirements.txt 

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app/ /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py", "--host", "0.0.0.0" ]

