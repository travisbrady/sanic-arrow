# sanic-arrow
Repo to test sending DataFrame via pyarrow

Currently segfaults when trying to deserialize DataFrame

```
pip install -r requirements
```

Sanic-based server in one window:
```
$ python app.py
[2018-04-11 17:58:10 -0500] [36086] [INFO] Goin' Fast @ http://0.0.0.0:8000
[2018-04-11 17:58:10 -0500] [36086] [INFO] Starting worker [36086]
```

Now run the client script:
```
$ python test_request.py
Traceback (most recent call last):
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/connectionpool.py", line 601, in urlopen
    chunked=chunked)
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/connectionpool.py", line 387, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/connectionpool.py", line 383, in _make_request
    httplib_response = conn.getresponse()
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/http/client.py", line 1331, in getresponse
    response.begin()
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/http/client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/http/client.py", line 266, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/requests/adapters.py", line 440, in send
    timeout=timeout
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/connectionpool.py", line 639, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/util/retry.py", line 357, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/packages/six.py", line 685, in reraise
    raise value.with_traceback(tb)
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/connectionpool.py", line 601, in urlopen
    chunked=chunked)
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/connectionpool.py", line 387, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/urllib3/connectionpool.py", line 383, in _make_request
    httplib_response = conn.getresponse()
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/http/client.py", line 1331, in getresponse
    response.begin()
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/http/client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/http/client.py", line 266, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response',))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "test_request.py", line 13, in <module>
    headers={'Content-Type': 'application/octet-stream'})
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/requests/api.py", line 112, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/requests/api.py", line 58, in request
    return session.request(method=method, url=url, **kwargs)
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/requests/sessions.py", line 508, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/requests/sessions.py", line 618, in send
    r = adapter.send(request, **kwargs)
  File "/Users/travisbrady/anaconda3/envs/py36/lib/python3.6/site-packages/requests/adapters.py", line 490, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response',))
```

Note segfault back in the server window the
```
[1]    36086 segmentation fault  python app.py
```
