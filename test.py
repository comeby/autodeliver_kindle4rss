# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class test(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world, i am writed by test.py!')

app = webapp2.WSGIApplication([
    ('/test', test)
], debug=True)
