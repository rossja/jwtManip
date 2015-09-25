#!/usr/bin/env python
# -------------------------------------------------------------
# A Burp extension to handle encoding/decoding JSON web tokens
# -------------------------------------------------------------
from __future__ import print_function;
import sys
import base64
import json
import jwt

options = {
   'verify_signature': False,
   'verify_exp': False,
   'verify_nbf': False,
   'verify_iat': False,
   'verify_aud': False,
   'require_exp': False,
   'require_iat': False,
   'require_nbf': False
}

# sample JSON Web Token
jwtString = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1NjAzNjExNjI2MTA0MzA2MzlhNmE4Y2MiLCJ1c2VybmFtZSI6InRlc3R1c2VyIiwicGFzc3dvcmQiOiJ1c3JwYXNzIiwiYWRtaW4iOnRydWUsIl9fdiI6MH0.YbDJNhfRtbmrEaBf27i9K_tR2o51ydaT1VmWRPw1dtg'

# sample JSON strings to convert to JWT
jsonHeader = '{ "typ": "JWT", "alg": "HS256" }';
jsonPayload = '{ "_id": "560361162610430639a6a8cc", "username": "testuser", "password": "usrpass", "admin": true, "__v": 0 }';

def encode(jsonData):
    # takes a JSON string and base64 encodes it
    print( base64.b64encode(json.loads(jsonData)) )

def formatJson(jsonData):
    # takes in a JSON string, dumps it in pretty format
    return json.dumps(jsonData, sort_keys=True, indent=4, ensure_ascii=False)

def getClaims(token):
    # takes in a JWT as string, reutrns the claims as JSON data
    return jwt.decode(token, options=options)

def getHeaders(token):
    # TODO figure out how to get at the header data!
    # takes in a JWT as string, reutrns the claims as JSON data
    return jwt.decode(token, options=options)

def encodeJson(jsonData, jwtSecret, algorithm):
    # takes in a Json string and converts it to JWT
    encoded = jwt.encode(jsonData, jwtSecret, algorithm=algorithm)

def main(argv):
    if method == 'encode':
        # take the JSON data and convert it to JWT
        encodeJson(indata, 'secret', 'HS256')

    elif method == 'decode':
        claims = getClaims(indata)
        print( formatJson(claims) )

if __name__ == "__main__":
    method = 'decode'
    indata = jwtString
    main([method, indata])
    #main(sys.argv[1:])
