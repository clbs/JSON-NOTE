import sys
import json
import os
import time

def getargs():
    if len(sys.argv) == 3:
        print("Title: " + sys.argv[1] + " Note: " + sys.argv[2])
        title = sys.argv[1]
        note = sys.argv[2]
        note = note.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')
        title = title.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')
        genjson(title, note)
    else:
        print("Error: Incorrect number of arguments.")
        return["Error","Incorrect number of arguments."]
    
def genjson(titles, notes):
    file = 'notes.json'
    teim = time.ctime()
    if os.path.exists(file):
        append = 'a'
        with open(file,'r') as q:
            data = json.load(q)
            data['notes'].append({
                teim: {
                'note': notes,
                'title': titles,
                }
                })
        with open(file,'w') as t:
            data = json.dump(data, t)

    else:
        append = 'w'
        data = {}
        data['notes'] = []
        data['notes'].append({
            teim: {
            'note': notes,
            'title': titles,
            }
            })
        with open(file,append) as q:
            data = json.dump(data, q)
            q.close()

def genoutput():
    file = 'notes.json'
    with open (file, 'r') as q:
        data = json.load(q)
        for keys in data['notes']:
            newdict = keys
            for key in newdict:
                print(key)
                print(newdict[key]['note'])
                print(newdict[key]['title'])

getargs()
genoutput()
    


   
