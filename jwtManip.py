#!/usr/bin/env python
# -------------------------------------------------------------
# A Burp extension to handle encoding/decoding JSON web tokens
# -------------------------------------------------------------
from __future__ import print_function;
import sys
import base64
import json
import jwt

# getopts is cooler
method = sys.argv[1]
indata = sys.argv[2]

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
jsonPayload = '{ "_id": "560361162610430639a6a8cc", "username": "testuser", "password": "usrpass", "admin": true, "__v": 0 }';

# takes in a JSON string, dumps it in pretty format
def formatJson(jsonData):
    return json.dumps(jsonData, sort_keys=True, indent=4, ensure_ascii=False)

# takes in a Json string and converts it to JWT
def createToken(jsonData, jwtSecret, algorithm):
    #return jwt.encode({'some': 'data'}, jwtSecret, algorithm=algorithm)
    return jwt.encode(json.loads(jsonData), jwtSecret, algorithm=algorithm)

# takes in a JWT as string, reutrns the claims as JSON data
def getClaims(token):
    return jwt.decode(token, options=options)

# takes in a JWT as string, reutrns the headers as JSON data
def getHeaders(token):
    # TODO figure out how to get at the header data!
    return jwt.decode(token, options=options)


def main(argv):
    if method == 'encode':
        # take the JSON data and convert it to JWT
        print( createToken(indata, 'secret', 'HS256') )

    elif method == 'decode':
        claims = getClaims(indata)
        print( formatJson(claims) )

if __name__ == "__main__":
    #main([method, indata])
    main(sys.argv[1:])
