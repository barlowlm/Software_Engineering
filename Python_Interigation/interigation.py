from github import Github

# using username and password
#g = Github("barlowlm", "Spassword")

# or using an access token
g = Github("d1045bd2897fb8b960e5617dde1c9f78ff2708f5")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="0bbc2698d53a08d1693bddd39bdc3ed10b0263e5")

for repo in g.get_user().get_repos():
    print(repo.name)

for repo in g.get_user().get_repos():
    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))