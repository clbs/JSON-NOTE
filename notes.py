
import sys
import json
import os
import time

def getargs():
    log = "/var/www/html/notes/notes.log"
    noteslog = ""
    if len(sys.argv) == 3:
        title = sys.argv[1]
        note = sys.argv[2]
        note = note.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')
        title = title.replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;')
        with open(log, "r+") as f:
            for line in f:
                noteslog  = noteslog + line
            f.close()
        with open(log, "w+") as f:
            noteslog  = str(noteslog + "note: '" + note +"'" + "\r\n" + "title: '" + title + "'" +"\r\n")
            f.write(noteslog)
            f.close()
        if   " ":
            genjson(title, note)
    elif len(sys.argv) == 2:
        delete = sys.argv[1]
        deletepost(delete)
        print(delete)
        with open(log, "r+") as f:
            for line in f:
                noteslog = noteslog + line
            f.close()
            with open(log, "w+") as f:
                noteslog = str(noteslog + "delete: " + delete + "\r\n")
                f.write(noteslog)
                f.close()
    else:
        with open(log, "r") as f:
            for line in f:
                noteslog = noteslog + line
                f.close
        with open(log, "w+") as f:
            noteslog = str(noteslog + "\r\n Error: Incorrect number of arguments \r\n Argument Count: " + str(len(sys.argv)))
            f.write(noteslog)
            f.close()
        print("Error: Incorrect number of arguments.")
        print("Argument: " + sys.argv[1])
    # genoutput()

def deletepost(post):
    file = '/var/www/html/notes/notes.json'
    if os.path.exists(file):
        with open(file,'r') as q:
            data = json.load(q)
            for key in data['notes']:
                for p in key:
                    if p == post:
                        del key[p]
                        break
                print(key)
                print(post)
            if key == post:
                print(key)
                del key[post]
            q.close()
        with open(file,'w+') as q:
            data = json.dump(data, q)
            q.close()


def genjson(titles, notes):
    file = '/var/www/html/notes/notes.json'
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
           # for key in newdict:
           #     print(key)
           #     print(newdict[key]['note'])
           #     print(newdict[key]['title'])

getargs()
    


   
