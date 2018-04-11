import io
import requests
import pandas as pd
import pyarrow as pa

df = pd.DataFrame([dict(a=99, b=100.0), dict(a=5, b=77.77)])
context = pa.default_serialization_context()
serialized_df = context.serialize(df)
bb = io.BytesIO()
dat = serialized_df.write_to(bb)
r = requests.post('http://0.0.0.0:8000/post',
        data=bb.getvalue(),
        headers={'Content-Type': 'application/octet-stream'})
