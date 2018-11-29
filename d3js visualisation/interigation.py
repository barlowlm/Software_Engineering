from github import Github
import json
#writing a jason file
# -*- coding: utf-8 -*-
# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data:  this should be done in the loop below
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

print(data == data_loaded)
# using username and password
#g = Github("barlowlm", "Spassword")

# or using an access token
g = Github("d1045bd2897fb8b960e5617dde1c9f78ff2708f5")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="0bbc2698d53a08d1693bddd39bdc3ed10b0263e5")

for repo in g.get_user().get_repos():
    print(repo.name)
i=0
for repo in g.get_user().get_repos():
    i+=1
    print(repo.name)
    print(repo.git_commits_url + str(i))
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
    print("\n")