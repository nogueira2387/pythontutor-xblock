"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import urllib
from string import Template

from xblock.core import XBlock
from xblock.fields import Scope, Boolean, String
from xblock.fragment import Fragment


DEFAULT_CODE = """
def listSum(numbers):
    if not numbers:
      return 0
    else:
      (f, rest) = numbers
      return f + listSum(rest)

myList = (1, (2, (3, None)))
total = listSum(myList)

"""

WORKBENCH_SCENARIO = """
<vertical_demo>
  <pythontutor>
  </pythontutor>
</vertical_demo>
"""

class PythonTutorXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    code = String(
        help="The code",
        scope=Scope.settings,
        default=DEFAULT_CODE
    )

    vertical = Boolean(
        help="Display vertically",
        scope=Scope.settings,
        default=False
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    def student_view(self, context=None):
        """      """

        code = self.code

        context = {
            'raw_code': code,
            'urlencoded_code': urllib.quote(code),
            'vertical': 'true' if self.vertical else 'false',
        }

        template = Template(self.resource_string("templates/pythontutor.html"))
        html = template.substitute(context)

        frag = Fragment(html)

        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [(PythonTutorXBlock, WORKBENCH_SCENARIO)]
