FROM python

COPY ./app/ /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py", "--host", "0.0.0.0" ]

