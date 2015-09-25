#!/usr/bin/env python
# -------------------------------------------------------------
# A Burp extension to handle encoding/decoding JSON web tokens
# -------------------------------------------------------------
from __future__ import print_function;
import sys
import base64
import json

# sample JSON Web Token
jwtString = 'geyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1NjAzNjExNjI2MTA0MzA2MzlhNmE4Y2MiLCJ1c2VybmFtZSI6InRlc3R1c2VyIiwicGFzc3dvcmQiOiJ1c3JwYXNzIiwiYWRtaW4iOnRydWUsIl9fdiI6MH0.YbDJNhfRtbmrEaBf27i9K_tR2o51ydaT1VmWRPw1dt'

# sample JSON strings to convert to JWT
jsonHeader = '{ "typ": "JWT", "alg": "HS256" }';
jsonPayload = '{ "_id": "560361162610430639a6a8cc", "username": "testuser", "password": "usrpass", "admin": true, "__v": 0 }';

def encode(data):
    # takes a JSON string and base64 encodes it
    print( base64.b64encode(json.loads(indata)) )

def prepJson(token):
    # takes a JWT as a string and splits out the
    # header, payload, and signature sections into
    # JSON objects and returns them as a dictionary
    print("token: " + token)
    header, payload, sig = token.split('.')
    print("header: " + header)
    print("payload: " + payload)
    print("sig: " + sig)
    header = base64.b64decode(header)
    payload = base64.b64decode(payload)
    sig = base64.b64decode(sig)
    return {'header': header, 'payload': payload, 'sig': sig}

def printJson(data):
    # takes in a JWT as string, dumps it into pretty JSON format
    return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)

def prepToken(header, payload):
    # encode the header and payload into base64
    # and return as a JWT 'dot delimited' pair
    header = encode( json.loads(header) )
    payload = encode( json.loads(payload) )
    return( header + '.' + payload )

def makeToken(encodedData):
    # TODO make this function sign the passed in header.payload data
    sig = "sig" # this needs to sign encodedData instead of doing nothing
    return encodedData + "." + sig


def main(argv):
    if method == 'encode':
        # take the JSON data and convert it to JWT
        data = prepToken(json_header, json_payload)
        jwt = makeToken(data)

    elif method == 'decode':
        jsonDict = prepJson(indata)
        print( 'Header:\n' . printJson(jsonDict['header']) )
        print( 'Payload:\n' . printJson(jsonDict['payload']) )
        print( 'Signature:\n' . printJson(jsonDict['sig']) )

if __name__ == "__main__":
    method = 'decode'
    indata = jwtString
    main([method, indata])
    #main(sys.argv[1:])
