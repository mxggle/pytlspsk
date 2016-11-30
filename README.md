# TLSPSK Wrapper for Socket

OpenSSL TLS-PSK wrapper for Python. Plain socket can be wrapped by pytlspsk wrapper to enable TLS-PSK channel.

### How to use it
Use `ssl_psk.wrap_socket` instead of 'ssl.wrap_socket' with `psk` paramater set to PSK key string.

```
wrapper = ssl_psk.wrap_socket(sock, psk='really secret secret', ciphers='PSK-AES256-CBC-SHA',
                              ssl_version=ssl.PROTOCOL_TLSv1,
                              server_side=True)
```

### how to run test cases

#### Start server:
```
python test.py -v TLSPSKTest.testServer

```
This will keep server running until test client executes simple test case.

#### Run client:
```
python test.py -v TLSPSKTest.testClient
```

Client will send simple text to server and server will echo it back.