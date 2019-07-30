#!coding=utf8
import urllib.request as urllib2
import os
from db import taskDb

def music_download(url, path, songid):
    if os.access(path, os.F_OK):
        return 
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    req = urllib2.Request(url,headers=headers)
    res = urllib2.urlopen(req)
    meta = res.info()
    print(meta)
    content_size = int(meta["Content-Length"])
    chunk_size=20480
    fin = 0
    db = taskDb()
    with open(path, 'wb') as f:
        db.delete(songid)
        db.add(songid, content_size)
        while fin*chunk_size< content_size:
            f.write(res.read(chunk_size))
            fin += 1
            if fin%10==1:
                db.update(songid, fin*chunk_size)      
        db.update(songid, content_size)
        print(fin)
    res.close()
    print('ok')

