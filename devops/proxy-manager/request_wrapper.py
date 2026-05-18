import sys
import subprocess
from data.proxy_engine import should_proxy, set_proxy_env, unset_proxy_env

def run_with_proxy_check(command_list, url):
    """
    command_list: e.g. ["curl", "-I", url]
    url: target URL to check
    """
    if should_proxy(url):
        print(f"[*] Detected proxy need for: {url}")
        set_proxy_env()
        try:
            result = subprocess.run(command_list, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"[!] Request failed via proxy. Check connectivity.")
            return result
        finally:
            unset_proxy_env()
    else:
        print(f"[*] Direct connection for: {url}")
        return subprocess.run(command_list, capture_output=True, text=True)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 request_wrapper.py <url> <curl_args...>")
        sys.exit(1)
        
    target_url = sys.argv[1]
    args = sys.argv[2:]
    
    # Simple logic: try direct, if fail, try proxy + learn
    res = run_with_proxy_check(["curl"] + args, target_url)
    
    if res.returncode != 0:
        print("[*] Direct attempt failed, trying proxy + learning...")
        from data.proxy_engine import add_auto_rule
        add_auto_rule(target_url)
        # Re-run with proxy
        set_proxy_env()
        res = subprocess.run(["curl"] + args, capture_output=True, text=True)
        unset_proxy_env()
        
    print(res.stdout)
