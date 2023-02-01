import json
import logging
import os

class JSONHelper:
    def __init__(self, file_path):
        self.file_path = f"{os.getcwd()}/{file_path}"  
        try:
            with open(self.file_path, 'r') as j:
                self.json_obj = json.loads(j.read())         
        except:
            logging.log(logging.ERROR, "Failed to locate file")
       
    
    def get_value_from_key_list(self, key_list = []):
        if len(key_list) == 0:
            logging.log(logging.INFO, "KeyList can not be Empty")
            raise Exception("KeyList can not be Empty")
            # base case end of recursion
        key = key_list.pop(0)
        value = self.json_obj[key]

        if len(key_list) == 0: # key
            return value
        # elif type(value) is not dict:
        #     logging.log(logging.INFO, f"Value is not Dict {value}")
        #     raise Exception( f"Value is not Dict {value}")
        else:
            return self.get_value_from_key_list(key_list)


    
    def write_value_to_key_list(self, value, key_list=[]):
        pass
    

    # def 