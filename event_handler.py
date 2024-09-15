import pygame
import constants as c

class EventHandler:
	def __init__(self):
		pygame.joystick.init()
		self.num_joysticks = pygame.joystick.get_count()
		self.joystick = None
		if self.num_joysticks:
			self.joystick = pygame.joystick.Joystick(0)
			self.joystick.init()

	def handle_events(self, actor):
		for event in pygame.event.get():               # Calling the event queue is also the way of pygame to interact with the operating
			self.check_quit_event(event)	
			self.check_keyboard_event(event, actor)
			self.check_joystick_event(event, actor)

	@staticmethod
	def check_quit_event(event):
		if event.type == pygame.QUIT:              # system internally. If the event queue isn't called regularly, your operating system 
			pygame.quit()                          # will assume that your program doesn't work correctly anymore and possibly make it look 
			quit()                                 # like the program crashed

	def check_keyboard_event(self, event, actor):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:             # event.type ------ pygame.QUIT,KEYDOWN,KEYUP
				actor.vel_x = -actor.speed       	# event.key  ------ pygame.K_keyboardcharacter
			elif event.key == pygame.K_d:
				actor.vel_x = actor.speed
			elif event.key == pygame.K_SPACE:
				actor.shoot() 
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				actor.vel_x = 0
			elif event.key == pygame.K_d:
				actor.vel_x = 0
			elif event.key == pygame.K_SPACE:
				pass

	def check_joystick_event(self, event, actor):
		if event.type == pygame.JOYHATMOTION:
			if self.joystick.get_hat(0) == c.XB_HAT_LEFT:
				actor.vel_x = -actor.speed
			elif self.joystick.get_hat(0) == c.XB_HAT_RIGHT:
				actor.vel_x = actor.speed
			if self.joystick.get_hat(0) == c.XB_HAT_NEUTRAL:
				actor.vel_x = 0
		if event.type == pygame.JOYBUTTONDOWN:
			if self.joystick.get_button(c.XB_A):
				actor.shoot()