import socket, ssl

HOST, PORT, CERT = '127.0.0.1', 8449, './cert.pem'

def handle(conn):
  print(conn.recv())
  with open("tls.log", "a") as fd:
      fd.write(conn.recv())
      fd.write("\r\n")

  conn.write(b'HTTP/1.1 200 OK\n\n%s' % conn.getpeername()[0].encode())

def main():
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(5)
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    #context.load_cert_chain(certfile=CERT)  # 1. key, 2. cert, 3. intermediates
    context.load_cert_chain('cert.pem', 'key.pem')
    #context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # optional
    context.set_ciphers("PSK-AES128-CBC-SHA")
    print("Listening...")
    while True:
        conn = None
        ssock, addr = sock.accept()
        try:
          conn = context.wrap_socket(ssock, server_side=True)
          handle(conn)
        except ssl.SSLError as e:
          print(e)
        finally:
          if conn:
            conn.close()
if __name__ == '__main__':
  main()
  print("Exiting...")
