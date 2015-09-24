#!/usr/bin/env python
# -------------------------------------------------------------
# A Burp extension to handle encoding/decoding JSON web tokens
# -------------------------------------------------------------
from __future__ import print_function;
import sys
import base64
import json

# OMGDEBUG
jwt_string = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ'
json_string = '{"first_name": "Jason", "last_name":"Ross"}'

# getopts is cooler
#method = sys.argv[1]
#indata = sys.argv[2]


def encode(data):
    print( base64.b64encode(json.loads(indata)) )

def prep(token):
    header, payload, sig = token.split('.')
    return {'header': header, 'payload': payload, 'sig': sig}

def decode(data):
    print( json.dumps(base64.b64decode(token),
        sort_keys=True,
        indent=4,
        ensure_ascii=False)
    )

def main(argv):
    if method == 'encode':
        encode(indata)
    elif method == 'decode':
        token = prep(indata)
        print( 'Header:\n' . decode(token['header']) )
        print( 'Payload:\n' . decode(token['payload']) )
        print( 'Signature:\n' . decode(token['sig']) )

if __name__ == "__main__":
    method = 'decode'
    indata = jwt_string
    main([method, indata])
    #main(sys.argv[1:])
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1NjAzNjExNjI2MTA0MzA2MzlhNmE4Y2MiLCJ1c2VybmFtZSI6InRlc3R1c2VyIiwicGFzc3dvcmQiOiJ1c3JwYXNzIiwiYWRtaW4iOnRydWUsIl9fdiI6MH0.YbDJNhfRtbmrEaBf27i9K_tR2o51ydaT1VmWRPw1dtg
