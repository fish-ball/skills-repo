import os

def init_proxy():
    data_dir = os.path.expanduser("~/.hermes/skills/devops/proxy-manager/data")
    for filename in ["user_rules.txt", "auto_rules.txt"]:
        path = os.path.join(data_dir, filename)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write("")
    print("Proxy rules initialized.")

if __name__ == "__main__":
    init_proxy()
