import json
import os


def read_json_data(file_name):

    project_root = os.path.dirname(os.path.dirname(__file__))

    file_path = os.path.join(project_root, "test_data", file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)