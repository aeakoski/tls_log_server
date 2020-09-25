FROM python:3

COPY server.py .
COPY cert.pem .
COPY key.pem .
COPY tls.log .

EXPOSE 8443
EXPOSE 8449


CMD [ "python", "server.py" ]
