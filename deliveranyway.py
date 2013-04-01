#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
import userdb

from google.appengine.api import urlfetch
from google.appengine.ext import db

class deliveranyway(webapp2.RequestHandler):
    def deliever_items(self,Cookie):
        url = "http://kindle4rss.com/send_now/"
        head = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Cookie': Cookie
        }
        result = urlfetch.fetch(url,method='POST',headers=head)
        return result.content
        
    def get(self):
        results = db.GqlQuery("SELECT * FROM Mydb")
        for result in results:
            Cookie = result.cookies
            self.response.write(self.deliever_items(Cookie)) 


app = webapp2.WSGIApplication([
    ('/deliveranyway', deliveranyway)
], debug=True)