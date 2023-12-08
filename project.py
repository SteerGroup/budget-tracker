import yaml


class Project:
    def __init__(self, yaml_path):
        self.yaml_path = yaml_path
        self.parse_yaml()

    def parse_yaml(self):
        with open(self.yaml_path, "r") as file:
            project_yaml = yaml.safe_load(file)
            self.name = project_yaml["name"]
            self.code = project_yaml["code"]
            self.open = project_yaml["open"]
