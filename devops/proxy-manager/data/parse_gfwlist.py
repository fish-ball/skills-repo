import re
import os

DATA_DIR = "/home/沐缘/.hermes/skills/devops/proxy-manager/data"
GFW_RAW = os.path.join(DATA_DIR, "gfwlist_raw.txt")
GFW_CLEAN = os.path.join(DATA_DIR, "gfwlist_domains.txt")

def extract_domains():
    domains = set()
    with open(GFW_RAW, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("||"):
                domain = line[2:].split('/')[0]
                domains.add(domain)
            elif line.startswith("|http"):
                domain = line.split('/')[2]
                domains.add(domain)
    
    with open(GFW_CLEAN, 'w') as f:
        for d in sorted(domains):
            f.write(d + '\n')

if __name__ == "__main__":
    extract_domains()
