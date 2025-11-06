# Part of Full Stack Automation Book by Shahzad Qadir

import requests

class FortiAPI:
    def __init__(self, auth_token: str, device_ip:str):
        self.auth_token = auth_token
        self.base_url = f"http://{device_ip}/api/v2/cmdb"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
            }

    def print_interfaces(self):
        response = requests.get(
            url=f"{self.base_url}/system/interface/",
            headers=self.headers
            )
        for result in response.json()['results']:
            for key, value in result.items():
                if key == 'name':
                    print(f"Interface: {value}")
                if key == 'ip':
                    print(f"IP Address: {value}")
                if key == 'allowaccess':
                    print(f"Allowed Access: {value}")
            print("***************************")



if __name__ == "__main__":
    api_obj = FortiAPI("501y5grjddx5rHf6mQcc4G8N9kgz0k", "10.10.99.1")
    api_obj.print_interfaces()