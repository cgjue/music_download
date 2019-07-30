import json
class taskDb(object):
    task={}
    flag = False
    def __init__(self):
        if not self.__class__.flag:
            self.__class__.flag=True
            try:
                with open('instance/music.db', 'rw') as f:
                    self.__class__.task = json.load(f)
            except Exception as e:
                print(e)
                self.__class__.task = {}
    def add(self, songid, content_size):
        self.__class__.task[songid] = {
            'fin': 0,
            'songid': songid,
            'content_size': content_size
        }
    
    def update(self, songid, fin):
        self.__class__.task[songid]['fin'] = fin
        print(fin)
    def delete(self, songid):
        if self.__class__.task.get(songid, None):
            self.__class__.task.pop(songid)
    def query(self, songid):
        return self.__class__.task.get(songid, None)
        
    def export(self):
        with open('instance/music.db', 'w') as f:
            self.__class__.task = json.dump(f)
