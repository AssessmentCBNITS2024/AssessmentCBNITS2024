import requests

class Auth0Client:
    def __init__(self, domain, api_token):
        self.domain = domain
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def createUser(self, user_data):
        url = f"https://{self.domain}/api/v2/users"
        response = requests.post(url, json=user_data, headers=self.headers)
        return response.json()

    def getUser(self, user_id):
        url = f"https://{self.domain}/api/v2/users/{user_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def deleteUser(self, user_id):
        url = f"https://{self.domain}/api/v2/users/{user_id}"
        response = requests.delete(url, headers=self.headers)
        return response.status_code

if __name__ == "__main__":
    auth0_domain = "test-auth0-domain"
    api_token = "test-auth0-management-api-token"

    client = Auth0Client(auth0_domain, api_token)

    # Get user
    user_id = "user_id"
    user = client.getUser(user_id)
    print("User Retrieved:", user)

    # Create user
    new_user_data = {
        "email": "test@xyz.com",
        "password": "password",
        "connection": "Username-Password-Authentication"
    }
    created_user = client.createUser(new_user_data)
    print("User Created:", created_user)

    # Delete user
    deleted_user = "user_id"
    deletion_status = client.deleteUser(deleted_user)
    print("Deletion Status Code:", deletion_status)
