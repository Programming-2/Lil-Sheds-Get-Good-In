import pygame

from states.State import State
from utils.Colors import colors


class Pong(State):
    def __init__(self, name, handler):
        super().__init__(name)
        self.handler = handler
        self.left_paddle_speed = 10
        self.left_paddle_height = 100
        self.left_paddle_width = 20
        self.left_paddle_x = 30
        self.left_paddle_y = 350
        self.left_paddle_rect = pygame.Rect(self.left_paddle_x, self.left_paddle_y, self.left_paddle_width, self.left_paddle_height)
        self.left_paddle_color = colors.get("WHITE")
        self.left_score = 0
        
        self.right_paddle_speed = 10
        self.right_paddle_height = 100
        self.right_paddle_width = 20
        self.right_paddle_x = 1040
        self.right_paddle_y = 350
        self.right_paddle_rect = pygame.Rect(self.right_paddle_x, self.right_paddle_y, self.right_paddle_width, self.right_paddle_height)
        self.right_paddle_color = colors.get("WHITE")
        self.right_score = 0

        self.ball_speed_x = 5
        self.ball_speed_y = 5
        self.ball_width = 20
        self.ball_height = 20
        self.ball_x = 540
        self.ball_y = 390
        self.ball_rect = pygame.Rect(self.ball_x, self.ball_y, self.ball_width, self.ball_height)
        self.ball_color = colors.get("WHITE")

        self.font = pygame.font.SysFont("Boogaloo", 48)

    def resetState(self):
        self.left_paddle_rect.x = self.left_paddle_x
        self.left_paddle_rect.y = self.left_paddle_y

        self.right_paddle_rect.x = self.right_paddle_x
        self.right_paddle_rect.y = self.right_paddle_y

        self.ball_rect.x = self.ball_x
        self.ball_rect.y = self.ball_y

    def clear_score(self):
        self.left_score = 0
        self.right_score = 0

    def update(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.handler.setDone(True)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.handler.getStateManager().setCurrentState("MainMenuState")
                    self.clear_score()
                    self.resetState()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.left_paddle_rect.y -= self.left_paddle_speed
        if keys[pygame.K_s]:
            self.left_paddle_rect.y += self.left_paddle_speed
        if keys[pygame.K_UP]:
            self.right_paddle_rect.y -= self.right_paddle_speed
        if keys[pygame.K_DOWN]:
            self.right_paddle_rect.y += self.right_paddle_speed
        self.ball_rect.x += self.ball_speed_x
        self.ball_rect.y += self.ball_speed_y

        screen.fill(colors.get("BLACK"))
        pygame.draw.rect(screen, self.left_paddle_color, self.left_paddle_rect)
        pygame.draw.rect(screen, self.right_paddle_color, self.right_paddle_rect)
        pygame.draw.rect(screen, self.ball_color, self.ball_rect)

        left_score = self.font.render(str(self.left_score), False, colors.get("WHITE"))
        right_score = self.font.render(str(self.right_score), False, colors.get("WHITE"))
        screen.blit(left_score, (100, 20))
        screen.blit(right_score, (950, 20))

        if pygame.Rect.colliderect(self.ball_rect, self.left_paddle_rect) or pygame.Rect.colliderect(self.ball_rect, self.right_paddle_rect):
            self.ball_speed_x *= -1
        if self.ball_rect.y <= 0 or self.ball_rect.y >= 780:
            self.ball_speed_y *= -1
        if self.ball_rect.x <= 0:
            self.right_score += 1
            self.resetState()
        if self.ball_rect.x >= 1100:
            self.left_score += 1
            self.resetState()
        if self.left_paddle_rect.y < 0:
            self.left_paddle_rect.y = 0
        if self.left_paddle_rect.y > 700:
            self.left_paddle_rect.y = 700
        if self.right_paddle_rect.y < 0:
            self.right_paddle_rect.y = 0
        if self.right_paddle_rect.y > 700:
            self.right_paddle_rect.y = 700