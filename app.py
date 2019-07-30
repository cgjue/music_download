#!coding=utf8
from flask import Flask, g, request, jsonify, render_template
from flask import copy_current_request_context
from threading import Thread
import json
from api import NetEase
from music_download import music_download
import requests
from db import taskDb
app = Flask(__name__)
netease = NetEase()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    #keywords, stype=1, offset=0, total='true', limit=50
    keywords = request.args.get('keywords', None)
    stype = request.args.get('stype', 1)
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', 50)
    if keywords:
        try:
            return jsonify({'status': True, 'res': netease.search(keywords, 
                stype, offset, limit)})
        except Exception as e:
            print(e)
    return jsonify({'res': '', 'status': False})

@app.route('/play', methods=('get', ))    
def play():
    ids = []
    songid = request.args.get('songid', None)
    if songid:
        ids.append(songid)
        try:
            return jsonify({'status': True, 'res': netease.songs_url(ids)})
        except Exception as e:
            print(e)
    return jsonify({'res': '', 'status': False})

@app.route('/download', methods=('GET', ))
def download():
    #songids=['123','546','3434']
    ids = []
    songid = request.args.get('songid', None)
    savename = request.args.get('savename', None)
    if not songid:
        return jsonify({'res': '', 'status': False})
    ids.append(songid)
    try:
        url = netease.songs_url(ids)[0]['url']
        path = 'cache/' + savename +'.'+ url.split('.')[-1]
        thr = Thread(target = music_download, args = [url, path, songid])
        thr.start()
        return jsonify({'status': True, 'res': 'ok'})
    except Exception as e:
            print(e)
    return jsonify({'res': '', 'status': False})

@app.route('/download_status', methods=('GET',))
def download_status():
    songid = request.args.get('songid', None)
    if not songid:
        return jsonify({'res': '', 'status': False})
    db = taskDb()
    res = db.query(songid)
    if not res:
        return jsonify({'res': '', 'status': False})
    return jsonify({'res': res, 'status': True})
app.run(host='0.0.0.0',port=8000, debug = True)
