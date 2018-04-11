import io
from sanic import Sanic
from sanic.response import json, raw, text
import pyarrow as pa
context = pa.default_serialization_context()

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/post', methods=["POST"])
async def post_handler(request):
    # print(request.body)
    # bb = io.BytesIO(request.body)
    bb = pa.py_buffer(request.body)
    # br = pa.BufferReader(request.body)
    df = pa.deserialize_pandas(bb)
    print(df.shape)
    return raw(b'HI')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
