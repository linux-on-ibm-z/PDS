import unittest
import requests

class TestFlask(unittest.TestCase):

    routes = ['pds','getSupportedDistros','faq']
    base_route='http://127.0.0.1:80/'

    def test_web_app_running(self):
        try:
             r = requests.get(self.base_route)
        except:
            self.fail("Could not open web app. Not running, or crashed. Test Failed")

    def test_routes(self):
        for i in self.routes:
            try:
                r = requests.get(self.base_route + i)
            except:
                self.fail('Can not render route: {0}'.format(i))


if __name__ == "__main__":
    unittest.main(warnings='ignore', failfast = True)
