import yaml

def load_yml(file_path):
    d = {}
    with open(file_path, 'r', encoding="utf-8") as f:
        d = yaml.load(f, Loader=yaml.SafeLoader)
    return d

if __name__ == "__main__":
    print(load_yml("config/config.yml"))


