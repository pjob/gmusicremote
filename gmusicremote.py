#!/usr/bin/env python

import os
import random
import subprocess
from getpass import getpass

from bottle import route, run
from gmusicapi import api
import vlc

import player

goog_api = api.Api()
media_play = player.Player()


# @route('/home')
# def home():
# 	song = songs[random.randint(0, len(songs))]
# 	media_play.next_song = song 
# 	return '<a href="/play">Prev</a> | <a href="/play">Play</a> | <a href="/stop">Stop</a> | <a href="/play">Next</a>'

@route('/play')
@route('/play/<song_id>')
def play(song_id=None):
	if media_play.vlc_instance:
		if media_play.vlc_instance.get_state == vlc.State.Paused:
			media_play.vlc_instance.play()
		else:
			media_play.vlc_instance.stop() # stop song before playing next one
	songs = media_play.songs
	if song_id:
		song = song_id 
	else:
		song = media_play.next_song

	media_play.vlc_instance = vlc.MediaPlayer(
			goog_api.get_stream_url(song['id']))
	media_play.vlc_instance.play()
	media_play.next_song = songs[random.randint(0, len(songs))]
	# process = subprocess.Popen(['cvlc', goog_api.get_stream_url(
	# 	song['id'])])
	return '<a href="/play">Prev</a> | <a href="/pause">Pause</a> | <a href="/stop">Stop</a> | <a href="/play">Next</a><br><h1>%s</h1><br><b>%s</b><br><img src="%s">' % (song['name'], song['artist'], song.get('albumArtUrl', '#'))

@route('/stop')
def stop():
	media_play.vlc_instance.stop()
	return '<a href="/play">Prev</a> | <a href="/play">Play</a> | <a href="/stop">Stop</a> | <a href="/play">Next</a>'

@route('/pause')
def pause():
	media_play.vlc_instance.pause()
	return '<a href="/play">Prev</a> | <a href="/play">Play</a> | <a href="/stop">Stop</a> | <a href="/play">Next</a>'



if __name__ == '__main__':
	email = ''
	password=getpass()
	goog_api.login(email, password)
	media_play.songs = goog_api.get_all_songs()
	media_play.next_song = media_play.songs[random.randint(0, len(media_play.songs))] 
	run(host='0.0.0.0', port='8080')


