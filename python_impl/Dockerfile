FROM python:3

COPY server.py .
COPY cert.pem .
COPY key.pem .
COPY tls.log .

CMD [ "python3", "server.py" ]
