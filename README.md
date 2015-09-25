# jwtManip
A Burp extension to manage decoding/encoding JSON web tokens

## Useage
jwtManip.py can accept a JSON string or a JSON Web Token as input.
The script requires 2 parameters:
1. The method to use
1. The data to pass

### Methods
1. encode
  - Requires the supplied input data to be a JSON string.
  - example usage:
  ./jwtManip.py  encode '{
      "id": "56036e8c185a9a042239becb",
      "username": "testuser",
      "password": "usrpass",
      "iat": 1443213069,
      "exp": 1443216669
    }'

1. decode
  - Requires the supplied input data to be a JSON Web Token string.
  - example usage:
     ./jwtManip.py decode eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3R1c2VyIiwiaWF0IjoxNDQzMjEzMDY5LCJwYXNzd29yZCI6InVzcnBhc3MiLCJpZCI6IjU2MDM2ZThjMTg1YTlhMDQyMjM5YmVjYiIsImV4cCI6MTQ0MzIxNjY2OX0.dMwrvCeRSRRwJ5a8NvN0-ema-RJiBtHLXpCF-cGhVRQ
