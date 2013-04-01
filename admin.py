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
import mymodule
import os 

from google.appengine.api import users
from google.appengine.api import urlfetch
from google.appengine.ext import db
from google.appengine.ext.webapp import template
 
class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            if user.nickname() == 'smartwangbo':
                results = db.GqlQuery("SELECT * FROM Mydb")
                template_values = {'user' : user.nickname(),
                                'results' : results,
                                }
                path = os.path.join(os.path.dirname(__file__), 'static/template.html')
                self.response.out.write(template.render(path, template_values))
            else:
                self.response.out.write(mymodule.show_page(user.nickname()))
        else:
            self.redirect(users.create_login_url(self.request.uri))    
            
app = webapp2.WSGIApplication(
                                     [('/admin', MainHandler),
                                     ],
                                     debug=True)   