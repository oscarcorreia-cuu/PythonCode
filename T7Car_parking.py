import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Parking Game")

# Clock object
clock = pygame.time.Clock()

# Define classes
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.Surface((50, 100), pygame.SRCALPHA)
        pygame.draw.rect(self.original_image, RED, (0, 0, 50, 100))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0
        self.angle = 0

    def update(self):
        self.rotate()
        self.move()

    def rotate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 2
        if keys[pygame.K_RIGHT]:
            self.angle -= 2
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speed = 5
        elif keys[pygame.K_DOWN]:
            self.speed = -5
        else:
            self.speed = 0

        radians = self.angle * (3.14 / 180)
        dx = -self.speed * math.sin(radians)
        dy = -self.speed * math.cos(radians)
        self.rect.x += dx
        self.rect.y += dy

class ParkingSpot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 110), pygame.SRCALPHA)
        pygame.draw.rect(self.image, GREEN, (0, 0, 60, 110), 5)
        self.rect = self.image.get_rect(center=(x, y))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect(center=(x, y))

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create player car
player_car = Car(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
all_sprites.add(player_car)

# Create parking spot
parking_spot = ParkingSpot(SCREEN_WIDTH // 2, 100)
all_sprites.add(parking_spot)

# Create obstacles
obstacle_positions = [
    (200, 300, 100, 30),
    (600, 300, 100, 30),
    (400, 200, 30, 100),
    (400, 400, 30, 100),
]

for pos in obstacle_positions:
    obstacle = Obstacle(*pos)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Font for messages
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Game variables
game_over = False
win = False

# Game loop
while True:
    clock.tick(60)  # 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Update sprites
        all_sprites.update()

        # Collision detection with obstacles
        if pygame.sprite.spritecollideany(player_car, obstacles):
            game_over = True

        # Check if player has parked
        if pygame.sprite.collide_rect(player_car, parking_spot):
            # Check alignment and position for successful parking
            if abs(player_car.angle % 360) < 10 and player_car.speed == 0:
                win = True
                game_over = True

    # Drawing
    screen.fill(WHITE)

    # Draw parking spot text
    parking_text = small_font.render("Park Here", True, GREEN)
    screen.blit(parking_text, (parking_spot.rect.x - 30, parking_spot.rect.y - 70))

    all_sprites.draw(screen)

    if game_over:
        if win:
            message = font.render("You Parked Successfully!", True, GREEN)
        else:
            message = font.render("Game Over!", True, RED)
        screen.blit(message, (SCREEN_WIDTH // 2 - message.get_width() // 2, SCREEN_HEIGHT // 2))
        restart_text = small_font.render("Press R to Restart or Q to Quit", True, GRAY)
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset the game
            player_car.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
            player_car.angle = 0
            player_car.speed = 0
            game_over = False
            win = False
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    # Flip the display
    pygame.display.flip()
