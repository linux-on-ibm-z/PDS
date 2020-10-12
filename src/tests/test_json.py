import unittest
import requests
import json

class TestDistro(unittest.TestCase):

##GET request to route responsible for displaying provided JSON.
##Both the web content and JSON are retrieved, and later compared.
    src = "http://127.0.0.1:80/getSupportedDistros"
    r = requests.get(src)
    tx = r.text
    js = r.json()


##Validate provided JSON (distro_data)
    def test_data_is_valid_json(self):
        try:
            json.loads(self.tx)
        except ValueError as err:
            self.fail("distro_data is not valid json")


##Create a list out of JSON object.
    pkgs = []
    for i in js:
        pkgs.append(str(i))

    versions = []
    for i in pkgs:
        for k in js[i]:
            versions.append(str(k))


##Verify that Json and Front-End render match.
    def test_data_render(self):
        data = self.tx
        for i in self.versions:
            if data.find(i) < 0:
                self.fail("Distro data is not present")



if __name__ == "__main__":
    unittest.main(warnings='ignore', failfast = True)
