# jwtManip
A Burp extension to manage decoding/encoding JSON web tokens

## Status
The script works just fine on Linux, as a stand-alone tool. It presumably works
on Windows also, but I've not tested it there.

I'm currently working on getting it integrated with Burp (eg. "send to JWTManip" functionality).

## Useage
*jwtManip.py* can accept a JSON string or a JSON Web Token as input.
The script requires two parameters:

1. The method to use
1. The data to pass

#### Methods
- encode
  - Requires the supplied input data to be a JSON string.
  - example usage:
```
./jwtManip.py  encode '{
  "id": "56036e8c185a9a042239becb",
  "username": "testuser",
  "password": "usrpass",
  "iat": 1443213069,
  "exp": 1443216669
}'

Token:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3R1c2VyIiwiaWF0IjoxNDQzMjEzMDY5LCJwYXNzd29yZCI6InVzcnBhc3MiLCJpZCI6IjU2MDM2ZThjMTg1YTlhMDQyMjM5YmVjYiIsImV4cCI6MTQ0MzIxNjY2OX0.dMwrvCeRSRRwJ5a8NvN0-ema-RJiBtHLXpCF-cGhVRQ
```
- decode
  - Requires the supplied input data to be a JSON Web Token string.
  - example usage:
```
./jwtManip.py decode eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3R1c2VyIiwiaWF0IjoxNDQzMjEzMDY5LCJwYXNzd29yZCI6InVzcnBhc3MiLCJpZCI6IjU2MDM2ZThjMTg1YTlhMDQyMjM5YmVjYiIsImV4cCI6MTQ0MzIxNjY2OX0.dMwrvCeRSRRwJ5a8NvN0-ema-RJiBtHLXpCF-cGhVRQ

JSON Claims:
{
    "exp": 1443216669,
    "iat": 1443213069,
    "id": "56036e8c185a9a042239becb",
    "password": "usrpass",
    "username": "testuser"
}
```
