import requests

response = requests.get("https://api.github.com/users/akki-live/repos")

my_repo = response.json()

#print(my_repo.keys())

for repo in my_repo:
    print(f"Repo name: {repo['clone_url']}")
    print(f"Git url: {repo['git_url']}")