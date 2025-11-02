# Inheritance:
# The Paddle and Ball classes both inherit from a base class GameObject.
# The GameObject class defines common properties (like rect for dimensions and position) and methods (like draw()).
# This promotes code reuse since both objects share similar attributes but can have their own specific methods.

# Polymorphism:
# Both Paddle and Ball override the draw() method of GameObject to provide their own specific implementations (polymorphism).
# Paddle uses pygame.draw.rect() to draw a rectangle.
# Ball uses pygame.draw.ellipse() to draw a ball.
# In the game loop, the same draw() method is called for both the Paddle and Ball objects, even though they each implement it differently.

# Encapsulation:
# The game objects (Paddle and Ball) manage their internal state (like position, speed, and dimensions) and expose methods (like move() and draw()) to interact with them. External code cannot directly modify the internal state of these objects but can interact with them through methods.

# Summary of Concepts Demonstrated:
# Encapsulation: The internal properties of each object are encapsulated within their class (e.g., the ball's position and speed).

# Polymorphism: Both the Paddle and Ball classes override the draw() method, and the same method call behaves differently depending on the object type.

# Inheritance: The Paddle and Ball classes inherit from a common GameObject class, allowing shared functionality and properties, reducing code duplication.

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bat and Ball Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Base class for all game objects (Inheritance)
class GameObject:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    # Polymorphic draw method
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Derived class for the Paddle (inherits from GameObject)
class Paddle(GameObject):
    def __init__(self):
        # Inherit GameObject's constructor
        super().__init__(WIDTH // 2 - 50, HEIGHT - 30, 100, 10, BLUE)
        self.speed = 10
    
    # Paddle-specific movement methods
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed
    
    def move_right(self):
        if self.rect.right < WIDTH:
            self.rect.x += self.speed

    # Paddle has its own draw method, can be further customized
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)  # Inherited method, but could be customized further

# Derived class for the Ball (inherits from GameObject)
class Ball(GameObject):
    def __init__(self):
        # Inherit GameObject's constructor
        super().__init__(WIDTH // 2, HEIGHT // 2, 20, 20, RED)
        self.speed_x = random.choice([-5, 5])
        self.speed_y = -5
    
    # Ball-specific movement logic
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off the walls
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

    # Reset ball position after missing the paddle
    def reset_position(self):
        self.rect.x = WIDTH // 2 - 10
        self.rect.y = HEIGHT // 2 - 10
        self.speed_y *= -1  # Change direction after reset

    # Overriding draw method to show polymorphism
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)  # Different from Paddle's rectangular draw

# Game loop
def main():
    clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball()
    running = True
    score = 0
    font = pygame.font.SysFont(None, 36)

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()

        # Move ball
        ball.move()

        # Check collision between ball and paddle
        if ball.rect.colliderect(paddle.rect):
            ball.speed_y *= -1
            score += 1  # Increase score when the ball hits the paddle

        # Check if ball goes below the paddle (misses)
        if ball.rect.bottom >= HEIGHT:
            ball.reset_position()
            score = 0  # Reset score on miss

        # Clear screen
        screen.fill(BLACK)

        # Draw paddle and ball (polymorphism in action)
        paddle.draw(screen)
        ball.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update screen
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
