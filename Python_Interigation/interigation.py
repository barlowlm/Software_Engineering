from github import Github
import json
import requests
import csv
import io
import NoapiInterigation

#writing a jason file
# -*- coding: utf-8 -*-
# Make it work for Python 2+3 and with Unicode

#print(data == data_loaded)
# using username and password
#g = Github("barlowlm", "")

# or using an access token
g = Github("d1045bd2897fb8b960e5617dde1c9f78ff2708f5")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="0bbc2698d53a08d1693bddd39bdc3ed10b0263e5")



#APIv3 utilized to print directory
for repo in g.get_user().get_repos():
    print(repo.name)
i=0
for repo in g.get_user().get_repos():
    i+=1
    print(repo.name)
    print(repo.git_commits_url + str(i))
    # to see all the available attributes and methods
    print(dir(repo))
    print("\n")

for repo in g.get_user().get_repos():
    print(repo.get_commits().totalCount)


#
#scrapping to find commits per repository
#

#total = 0
#print('\n')
#print(g.get_user())
##print('\n')

#for repo in NoapiInterigation.count_user_commits('barlowlm'):
#   print ("Repo `%(name)s` has %(num_commits)d commits, size %(size)d." % repo)
    
#total += repo['num_commits']


#print ("Total commits: %d" % total)



## input into a csv

with open('commits.csv', mode='w') as csv_file:
    fieldnames = ['Repo_Name', 'Commits', 'size']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for repo in g.get_user().get_repos():
        print(repo.get_commits().totalCount)
        writer.writerow({'Repo_Name': repo.name , 'Commits': repo.get_commits().totalCount , 'size': repo.get_commits().totalCount})
    
