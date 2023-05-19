import json
import logging
import os

class JSONHelper:
    def __init__(self, file_path):
        self.file_path = f"{os.getcwd()}/{file_path}" 
        with open(self.file_path, 'r') as j:
                self.json_obj = json.loads(j.read())  
        # try:
        #     with open(self.file_path, 'r') as j:
        #         self.json_obj = json.loads(j.read())         
        # except:
        #     logging.log(logging.ERROR, "Failed to locate file")
       
    
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

    
    def get_value_from_parent(self, parent='parameters', key='Acquisition_Blocking_Immunity_Decay_Rate'):
        return self.json_obj[parent][key]

    
    def write_actions(self, irs, itns): 
        # get values from the simulation and output to campaigns file
        print(f"\n\n*** WRITING TO CAMPAIGNS FILE ***")
        self.json_obj["Events"][0]["Event_Coordinator_Config"]["Demographic_Coverage"] = float(irs)
        self.json_obj["Events"][1]["Event_Coordinator_Config"]["Demographic_Coverage"] = float(itns)

        json_object = json.dumps(self.json_obj, indent=4)

        # Writing to sample.json
        with open(self.file_path, "w") as outfile:
            outfile.write(json_object)

        print("*** SUCCESSFULLY CHANGED CAMPAIGNS FILE*** \n\n")
        
    

    # def 