from tornado.httpclient import HTTPClient, HTTPRequest
from tornado.ioloop import IOLoop
import tornado.options
import json
import time
import calendar
import email.utils
import mailbox
import email

http_client = HTTPClient()

DEFAULT_BATCH_SIZE = 500
ES_URL  = "http://localhost:9200/gmail"

print "Hello World!"
