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


class mydeliver(webapp2.RequestHandler):
#if the number of items is large than 20, return ture, else return false
    def test_item_num(self, Cookie):
        url = "http://kindle4rss.com"
        head = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Cookie': Cookie
        }
        result = urlfetch.fetch(url,method='POST',headers=head)
        content = result.content
        match = re.search(r'\s{0,}Send <strong>\n\s{0,}\d+\n\s{0,}<.strong> new items now!', content, re.I)
            
        if match:
            str = match.group(0)
            match2 = re.search(r'\d+', str, re.I)
            if match2:
                if (int(match2.group(0))>2):
                    return True
                else:
                    return False
        else:
            return False
                    
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
            if(self.test_item_num(Cookie)):
                self.response.write(self.deliever_items(Cookie))
            else:
                self.response.write("not deliver!")  

#        Cookie = "pgv_pvi=321104896; user_id=41457$1$ba23cfc7da973e4053c3104eb7fa147def75ce0a; pgv_si=s1629130752; sessionid=fbab564964e3bf77e1e3d5a7dc1e300f; __utma=236643806.1351645578.1363779381.1364354854.1364357571.3; __utmc=2366438"
 
          
app = webapp2.WSGIApplication([
    ('/deliver', mydeliver)
], debug=True)
