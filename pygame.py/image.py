import pygame
import sys
import random
import os

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("現在の作業ディレクトリ:", os.getcwd())  # 確認用


# Pygameの初期化
pygame.init()

# ウィンドウサイズとタイトル
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("画像を使ったゲーム")

# 色の定義
white = (255, 255, 255)

# キャラクター画像のロード
character = pygame.image.load("character.png")
character = pygame.transform.scale(character, (50, 50))  # サイズを調整

# 障害物画像のロード
obstacle_img = pygame.image.load("obstacle.png")
obstacle_img = pygame.transform.scale(obstacle_img, (50, 50))  # サイズを調整

# キャラクターの初期位置
character_x, character_y = 400, 300
character_speed = 5

# 障害物の初期位置
obstacle_x = random.randint(0, screen_width - 50)
obstacle_y = random.randint(0, screen_height - 50)
obstacle_speed_x = random.choice([-3, 3])
obstacle_speed_y = random.choice([-3, 3])

# ゲームループ
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力を取得
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and character_y > 0:
        character_y -= character_speed
    if keys[pygame.K_DOWN] and character_y < screen_height - 50:
        character_y += character_speed
    if keys[pygame.K_LEFT] and character_x > 0:
        character_x -= character_speed
    if keys[pygame.K_RIGHT] and character_x < screen_width - 50:
        character_x += character_speed

    # 障害物の移動
    obstacle_x += obstacle_speed_x
    obstacle_y += obstacle_speed_y

    # 障害物が画面端にぶつかると反転
    if obstacle_x <= 0 or obstacle_x + 50 >= screen_width:
        obstacle_speed_x *= -1
    if obstacle_y <= 0 or obstacle_y + 50 >= screen_height:
        obstacle_speed_y *= -1

    # 衝突判定
    character_rect = pygame.Rect(character_x, character_y, 50, 50)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 50, 50)
    if character_rect.colliderect(obstacle_rect):
        print("ゲームオーバー！")
        running = False

    # 背景を描画
    screen.fill(white)

    # キャラクターと障害物を描画
    screen.blit(character, (character_x, character_y))
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    # 画面を更新
    pygame.display.flip()
    clock.tick(60)
