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
import logging
import userdb
import os
import mymodule
import datetime
import time

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db

class MainHandler(webapp2.RequestHandler):     
    def post(self):
        user_name = self.request.get('user_name')
        cookies = self.request.get('Cookies')
        description = self.request.get('description')
        push_time = self.request.get('push_time')
        if cookies:
            results = db.GqlQuery("SELECT * FROM Mydb WHERE name=:1 AND cookies=:2", user_name, cookies)
            if results.get() == None:
                item = userdb.Mydb(name=user_name, cookies=cookies,description=description)
                item.push = datetime.time(22,0,0)
                item.push_time_str = push_time
                item.put()
        
        user = users.get_current_user()
        if user:
            time.sleep(1)
            self.response.out.write(mymodule.show_page(user.nickname()))
        else:
            self.redirect(users.create_login_url(self.request.uri))  
    
    
app = webapp2.WSGIApplication(
                                     [('/put', MainHandler),
                                     ],
                                     debug=True)   
