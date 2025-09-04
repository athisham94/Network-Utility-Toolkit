import requests

def check_subdomain(domain, subdomains):
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Subdomain {sub} exists at {url}")
        except requests.exceptions.RequestException:
            print(f"Subdomain {sub} does not exist.")
