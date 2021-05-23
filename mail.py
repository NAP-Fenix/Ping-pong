from pygame import *



class GameSprite(sprite.Sprite):
	def __init__(self,image_player,player_x,player_y,player_speed):
		super().__init__()
		self.image = transform.scale(image.load(111-removebg-preview.png),(100,100))
		self.speed = player_speed
		self.rect = self.image.get_rect()
		self.rect.x = player_x
		self.rect.y = player_y	
	def reset(self):
		window.blit(self.image, (self.rect.x , self.rect.y))

window =  display.set_mode((0,0), FULLSCREEN)
display.set_caption('Пин-понг')
win_width,win_height = 1920,1080
background = transform.scale(image.load('gg.png'),(win_width,win_height))
	
class Rocet1(GameSprite):
	def update(self):
		global x1
		keys = key.get_pressed()
		if keys[K_a] and self.rect.x >= 5:
			self.rect.x -= self.speed
		elif keys[K_d] and self.rect.x <= win_width-80:
			self.rect.x += self.speed

		x1 = self.rect.x
class Rocet2(GameSprite):
	def update(self):
		global x1
		keys = key.get_pressed()
		if keys[K_w] and self.rect.x >= 5:
			self.rect.x -= self.speed
		elif keys[K_s] and self.rect.x <= win_width-80:
			self.rect.x += self.speed

		x1 = self.rect.x
# player1 = roket1
# a = 
finish = False
game = True
while game:
	# clock.tick(60)

	for e in event.get():
		if e.type == QUIT:
			game = False
		
			

	if finish != True:
		window.blit(background,(0,0))

		# hero.reset()
		# hero.update()

	

		



			


		# text_score = font1.render("Счёт: "+str(score),True,(255,0,0))
		# text_lost = font1.render("Пропущено: "+str(lost),True,(255,0,0))

		# window.blit(text_score, [20,20])
		# window.blit(text_lost, [20,60])

		

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	display.update()

