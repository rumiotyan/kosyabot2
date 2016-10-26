# -*- coding: utf-8 -*-

import os
from datetime import datetime

import twitter


api = twitter.Api(consumer_key=os.environ["jYO8YvMwme6jfHscK1v6qwrcz"],
                  consumer_secret=os.environ["YNgAEKYvQwcKRB2OZwPb645T4PbPqka1cp8SKbhdvkOlvPcw8E"],
                  access_token_key=os.environ["706722707732197377-yBErpTD3pRgtNgdnaYY3j3849M9yTpe"],
                  access_token_secret=os.environ["EZxogacuTd3n2XsLTMOcs788askj3LSohOkSZqf60WiMX"]
                  )
api.PostUpdate("system time is %s" % datetime.now())
