# TLSPSK Wrapper for Socket

OpenSSL TLS-PSK wrapper for Python. Plain socket can be wrapped by pytlspsk wrapper to enable TLS-PSK channel.

### Installation
`pip install pytlspsk`

### Sample Usage for Python
Use `ssl_psk.wrap_socket` with `psk` paramater set to PSK key string.

```
from pytlspsk import ssl_psk

...
...

wrapper = ssl_psk.wrap_socket(sock, psk='really secret secret', ciphers='PSK-AES256-CBC-SHA',
                              ssl_version=ssl.PROTOCOL_TLSv1,
                              server_side=True)
 >> sock: plain socket
 >> psk: psk key for the channel
```

### How to run test cases

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
