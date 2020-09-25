Password to the private key: password

Generate the cert:
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

Test tool to check handshake compability:
https://superuser.com/questions/109213/how-do-i-list-the-ssl-tls-cipher-suites-a-particular-website-offers

If no certificate is pressent, all handshake
