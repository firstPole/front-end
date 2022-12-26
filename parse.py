import json

import os

import sys





f = open('sensitive-report.json')



data = json.load(f)



total_incidents = data['total_incidents']

files = []

for x in range(total_incidents):

    files.append(data['entities_with_incidents'][x]['filename'])
   

print ("Total Incidents : " + str(total_incidents))
print ("File names : " + str(files))
f.close()
