from utils.json_helper import JSONHelper
import unittest
import json
import os

class TestJSONHelper(unittest.TestCase):
    def setUp(self):
        self.jsonH = JSONHelper(file_path="data/campaign.json")
        json_file_path = f"{os.getcwd()}/data/campaign.json"
        # print(f"File Location: {json_file_path}")

        with open(json_file_path, 'r') as j:
            self.actual_json = json.loads(j.read())
            
    def test_read_json_file(self):
        self.assertEqual(self.actual_json, self.jsonH.json_obj)
    
    def test_get_value_from_key_list(self):
        value = self.jsonH.get_value_from_key_list(['Events'])
        self.assertEqual(self.actual_json['Events'], value)

    def test_get_value_from_key_list_multiple_values(self):
        pass
        # value = self.jsonH.get_value_from_key_list(['Events',0,'Event_Coordinator_Config'])
        # self.assertEqual(self.actual_json['Events'][0]['Event_Coordinator_Config'], value)


if __name__ == '__main__':
    unittest.main()