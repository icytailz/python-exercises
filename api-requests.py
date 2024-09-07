import requests


def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    # Check the request status
    if response.status_code == 200:
        user_data = response.json()
        print(f"User: {user_data['login']}")
        print(f"Name: {user_data.get('name', 'Not Provided')}")
        print(f"Company: {user_data.get('company', 'Not Provided')}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
    else:
        print(
            f"Failed to detch user information. Status Code: {response.status_code}")


if __name__ == "__main__":
    username = input("Enter the Github username: ")
    get_github_user_info(username)
