Password to the private key: password

Generate the cert:
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

Test tool to check handshake compability:
https://superuser.com/questions/109213/how-do-i-list-the-ssl-tls-cipher-suites-a-particular-website-offers

If no certificate is pressent, all handshake


Test connection with ./test.sh localhost:4443


sudo docker build -t tls_log_server .
sudo docker run -it --rm --name py_tls -p 8449:8449/tcp --hostname localhost tls_log_server

I cant seem to send my tlsstuff through the docker-proxy

TODO
https://www.docker.com/blog/containerized-python-development-part-1/
