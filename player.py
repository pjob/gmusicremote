class Player(object):
	def __init__(self):
		self.play = 0
		self.songs = []
		self.current_song = None
		self.history = []
		self.vlc_instance = None
		self.next_song = None
		
	def update_player(self,id):
		self.current_song = id
	
	def stopped(self):
		pass
	
	
	


