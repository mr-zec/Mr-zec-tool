import requests

def test_proxy(proxy, test_url="http://www.google.com"):
    """
    Test whether a proxy is working by attempting to connect to a test URL.

    Parameters:
        proxy (str): The proxy address (e.g., "123.456.789.0:8080").
        test_url (str): The URL to test the proxy against (default is http://www.google.com).

    Returns:
        bool: True if the proxy is working, False otherwise.
    """
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        response = requests.get(test_url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except Exception as e:
        print(f"Failed to connect using proxy {proxy}: {e}")
        return False

def main():
    # Read proxy list from a file
    with open("proxy", "r") as file:
        proxy_list = [line.strip() for line in file if line.strip()]

    test_url = "http://www.google.com"  # URL to test against

    # Open the results file
    with open("results.txt", "w") as file:
        for proxy in proxy_list:
            if test_proxy(proxy, test_url):
                result = f"Proxy {proxy} is working.\n"
            else:
                result = f"Proxy {proxy} is not working.\n"
            
            # Write the result to the file
            file.write(result)
            print(result)  # Optionally print the result to the console

if __name__ == "__main__":
    main()
