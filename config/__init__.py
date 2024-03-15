import yaml


def load_config():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


config = load_config()

Users = config["Users"]
Localtion = config["Localtion"]
Action = config["Action"]
