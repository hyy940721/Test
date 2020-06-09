import json
import os


def read_data():
    login_path=os.path.dirname(os.path.abspath(__file__))+"/data/login_data.json"
    with open(login_path,mode="r",encoding="utf-8") as f:
        jsonData= json.load(f)
        result_list=[]
        for data in jsonData:
            result_list.append((data.values()))
    print(result_list)
    return result_list
