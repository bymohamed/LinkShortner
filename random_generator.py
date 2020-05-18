import uuid
import os
import validators
import sys
from generate_php import generate_php

url = sys.argv[1]

if ( validators.url(url) ):
    code = uuid.uuid4().hex[:6]
    generate_php(url,code)
    print ( os.path.abspath(code+'.php') )

else:
    print('invalid url')
