from github import Github
import json
import requests
import csv
import io
#import NoapiInterigation
import d3py
import pandas
import numpy as np
import networkx as nx
import logging

#import d3.v4.js

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
    



## make a flower using jason data



# some test data
#T = 100
# this is a data frame with three columns (we only use 2)
#df = pandas.DataFrame({
 #   "time" : range(T),
  #  "pressure": np.random.rand(T),
  #  "temp" : np.random.rand(T)
#})
## build up a figure, ggplot2 style
# instantiate the figure object
#fig = d3py.PandasFigure(df, name="basic_example", width=300, height=300) 
# add some red points
#fig += d3py.geoms.Point(x="pressure", y="temp", fill="red")
# writes 3 files, starts up a server, then draws some beautiful points in Chrome



##graph
#logging.basicConfig(level=logging.DEBUG)

#G=nx.Graph()
#G.add_edge(1,2)
#G.add_edge(7,3)
#G.add_edge(17,2)
#G.add_edge(35,4)
#G.add_edge(48,2)

#use 'with' if you are writing a script and want to serve this up forever
#with d3py.NetworkXFigure(G, width=500, height=500) as p:
#   p += d3py.ForceLayout()
#   p.show()


## scatter plot

n = 400

df = pandas.DataFrame({
   'd1': np.arange(0,n),
   'd2': np.random.normal(0, 1, n)
})

with d3py.PandasFigure(df, "example scatter plot using d3py", width=400, height=400) as fig:
    fig += d3py.Point("d1", "d2", fill="DodgerBlue")
    fig += d3py.xAxis('d1', label="Random")
    fig += d3py.yAxis('d2', label="Also random")
    fig.show()