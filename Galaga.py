import pygame
from Ship import Ship
from Star import Star
from Bg import Bg
from Enemyspawners import Enemy_spwaner
from Particlespawners import Particle_spawner
from event_handler import EventHandler
from alert_box import Alert_Box
import constants as c

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Display Setup
display = pygame.display.set_mode(c.DISPLAY_SIZE)    # (Width,Height)
fps = 60
clock = pygame.time.Clock()
# black = (0,0,0)                                      (red,green,blue)

# Object Setup
event_handler = EventHandler()
bg = Bg()                                            # Seperating ship and bg as we want to display the 
bg_group = pygame.sprite.Group()                     # bg first and then ship
bg_group.add(bg)                                     # If we dont seperate them then it can display anyone first
player = Ship()                                      # randomly ,which we dont want
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spwaner = Enemy_spwaner()
particle_spawner = Particle_spawner()
alert_box_group = pygame.sprite.Group()

# Music Setup
pygame.mixer.music.load('Theme.ogg')
pygame.mixer.music.play(loops = True)

while True:
    # Ticking the Clock
    clock.tick(fps)                                # Makes sure that it runs the loop 60 times in 1 sec

    # Handle the Events
    event_handler.handle_events(player)
        
    # Update all the objects
    bg_group.update()
    sprite_group.update()
    enemy_spwaner.update()
    particle_spawner.update()
    alert_box_group.update()

    # Check Collision
    collided = pygame.sprite.groupcollide(player.bullet_group, enemy_spwaner.enemy_group, True, False)
    for bullets, enemy in collided.items():
        enemy[0].get_hit()
        player.hud.score.update_score(enemy[0].score_value)
        if not enemy[0].is_invincible:
            particle_spawner.spawn_particles((bullets.rect.x,bullets.rect.y))

    collided = pygame.sprite.groupcollide(sprite_group, enemy_spwaner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible and not player.is_invincible:
            player.get_hit()
            enemy[0].hp = 0
            enemy[0].get_hit()

    # Check for game over
    if not player.is_alive:
        enemy_spwaner.clear_enemies()
        alert_box = Alert_Box('Game Over')
        alert_box_group.add(alert_box)

    # Render the display
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullet_group.draw(display)              # IMP....
    enemy_spwaner.enemy_group.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.score_group.draw(display)
    player.hud.icons_group.draw(display)
    alert_box_group.draw(display)

    pygame.display.update()                        # display.flip() will update the contents of the entire display.
                                                   # display.update() allows to update a portion of the screen, instead of the entire 
                                                   # area of the screen. Passing no arguments, updates the entire display
                                                   # Hence display.update is more faster in most cases
