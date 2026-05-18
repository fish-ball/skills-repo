import os
import urllib.parse

DATA_DIR = "/home/huangwc21/.hermes/skills/devops/proxy-manager/data"
USER_RULES = os.path.join(DATA_DIR, "user_rules.txt")
AUTO_RULES = os.path.join(DATA_DIR, "auto_rules.txt")
GFW_RULES = os.path.join(DATA_DIR, "gfwlist_domains.txt")

def should_proxy(url):
    domain = urllib.parse.urlparse(url).netloc
    
    # Check user rules first
    if os.path.exists(USER_RULES):
        with open(USER_RULES, 'r') as f:
            for line in f:
                if line.strip() and line.strip() in domain:
                    return True
                
    # Check auto rules
    if os.path.exists(AUTO_RULES):
        with open(AUTO_RULES, 'r') as f:
            for line in f:
                if line.strip() and line.strip() == domain:
                    return True
                
    # Check GFW list
    if os.path.exists(GFW_RULES):
        with open(GFW_RULES, 'r') as f:
            for line in f:
                if line.strip() and line.strip() in domain:
                    return True
                
    return False

def add_auto_rule(url):
    domain = urllib.parse.urlparse(url).netloc
    if not domain: return
    
    # Check if already exists to avoid duplicates
    existing = set()
    if os.path.exists(AUTO_RULES):
        with open(AUTO_RULES, 'r') as f:
            existing = {l.strip() for l in f.readlines() if l.strip()}
    
    if domain not in existing:
        with open(AUTO_RULES, 'a') as f:
            f.write(domain + '\n')

def set_proxy_env():
    os.environ['http_proxy'] = 'http://172.28.80.1:1080'
    os.environ['https_proxy'] = 'http://172.28.80.1:1080'

def unset_proxy_env():
    os.environ.pop('http_proxy', None)
    os.environ.pop('https_proxy', None)
