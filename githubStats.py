from urllib import request
import json
import contributor
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def getJsonFromUrl(url):
    html = request.urlopen(url)

    res = html.read().decode("utf-8")

    return json.loads(str(res))


def contributor_graph():
    j = getJsonFromUrl('https://api.github.com/repos/bitcoin/bitcoin/stats/contributors')

    X = []
    Y1 = []
    Y2 = []

    max_total = 0

    for i in j:
        d = contributor.Contributor(i)
        X.append(d.login)
    
        additions = [a['a'] for a in d.commit_list]
        additions = sum(additions)

        deletions = [de['d'] for de in d.commit_list]
        deletions = sum(deletions)

        total_commits = d.total

        if max_total < total_commits:
            max_total = total_commits

        total_changes = additions + deletions

        norm_add = (additions / total_changes) * total_commits
        norm_del = (deletions / total_changes) * total_commits

        Y1.append(norm_add)
        Y2.append(norm_del)


    N = len(j)

    ind = np.arange(N)

    width = 0.35

    p1 = plt.bar(ind, Y1, width, color="g")
    p2 = plt.bar(ind, Y2, width, bottom=Y1, color="r")

    plt.ylabel('Commits')
    plt.title("Total Commits with Normalised Addition and Deletion")
    plt.xticks(ind, X)
    plt.yticks(np.arange(0, max_total + 1, 10))
    plt.legend((p1[0], p2[0]), ("Additions", "Deletions"))

    plt.show()

def getLastYearByWeek():
    j = getJsonFromUrl('https://api.github.com/repos/bitcoin/bitcoin/stats/commit_activity')

    max_total = 0

    X = []
    Y1 = []
    Y2 = []
    Y3 = []
    Y4 = []
    Y5 = []
    Y6 = []
    Y7 = []

    for i in j:
        week = datetime.utcfromtimestamp(i['week'])
        week = str(week.day) + "/" + str(week.month) + "/" + str(week.year)
        X.append(week)
    
        Y1.append(i['days'][1])
        Y2.append(i['days'][2])
        Y3.append(i['days'][3])
        Y4.append(i['days'][4])
        Y5.append(i['days'][5])
        Y6.append(i['days'][6])
        Y7.append(i['days'][0])
        
        total_commits = i['total']

        if max_total < total_commits:
            max_total = total_commits


    N = len(j)

    ind = np.arange(N)

    width = 0.35

    p1 = plt.bar(ind, Y1, width, color="g")
    p2 = plt.bar(ind, Y2, width, bottom=Y1, color="r")
    p3 = plt.bar(ind, Y3, width, bottom=Y2, color="b")
    p4 = plt.bar(ind, Y4, width, bottom=Y3, color="y")
    p5 = plt.bar(ind, Y5, width, bottom=Y4, color="m")
    p6 = plt.bar(ind, Y6, width, bottom=Y5, color="c")
    p7 = plt.bar(ind, Y7, width, bottom=Y6, color="k")

    plt.ylabel('Commits')
    plt.title("Total Commits Split By Day Of Week")
    plt.xticks(ind, X)
    plt.yticks(np.arange(0, max_total + 1, 10))
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0]), ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"))

    plt.show()

def getWeekAddDel(last=0):
    j = getJsonFromUrl('https://api.github.com/repos/bitcoin/bitcoin/stats/code_frequency')

    max_total = 0

    X = []
    Y1 = []
    Y2 = []

    for i in j[-last:]:
        week = datetime.utcfromtimestamp(i[0])
        week = str(week.day) + "/" + str(week.month) + "/" + str(week.year)
        X.append(week)
    
        Y1.append(i[1])
        Y2.append(-1 * i[2])
        
        total_commits = i[1] + -1 * i[2]

        if max_total < total_commits:
            max_total = total_commits


    N = len(j) if last == 0 else last

    ind = np.arange(N)

    width = 0.35

    p1 = plt.bar(ind, Y1, width, color="g")
    p2 = plt.bar(ind, Y2, width, bottom=Y1, color="r")

    plt.ylabel('Commits')
    plt.title("weekly aggregate of the number of additions and deletions")
    plt.xticks(ind, X)
    plt.yticks(np.arange(0, max_total + 1, 10))
    plt.legend((p1[0], p2[0]), ("Additions", "Deletions"))

    plt.show()

def getOwnerVs():
    j = getJsonFromUrl('https://api.github.com/repos/bitcoin/bitcoin/stats/participation')

    max_total = 0

    X = np.arange(1, 53, 1)
    Y1 = []
    Y2 = []
        
    for i in range(52):
    
        Y1.append(j['owner'][i])
        Y2.append(j['all'][i] - j['owner'][i])
        
        total_commits = j['all'][i]

        if max_total < total_commits:
            max_total = total_commits


    N = 52

    ind = np.arange(N)

    width = 0.35

    p1 = plt.bar(ind, Y1, width, color="b")
    p2 = plt.bar(ind, Y2, width, bottom=Y1, color="r")

    plt.ylabel('Commits')
    plt.title("Total Commits In Last Year Owner Vs Everyone Else")
    plt.xticks(ind, X)
    plt.yticks(np.arange(0, max_total + 1, 10))
    plt.legend((p1[0], p2[0]), ("Owner", "Others"))

    plt.show()

contributor_graph()
getLastYearByWeek()
getWeekAddDel(52)
getOwnerVs()
