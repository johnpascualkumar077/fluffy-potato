import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# ウィンドウサイズとタイトル
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("複数の障害物を追加")

# 色の定義
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# キャラクターの設定
circle_x, circle_y = 400, 300
circle_radius = 30
circle_speed = 5

# 障害物の設定
num_obstacles = 5  # 障害物の数
obstacles = []
for _ in range(num_obstacles):
    obstacle = {
        "x": random.randint(0, screen_width - 50),
        "y": random.randint(0, screen_height - 50),
        "width": 50,
        "height": 50,
        "speed_x": random.choice([-3, 3]),
        "speed_y": random.choice([-3, 3]),
    }
    obstacles.append(obstacle)

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
    if keys[pygame.K_UP] and circle_y - circle_radius > 0:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN] and circle_y + circle_radius < screen_height:
        circle_y += circle_speed
    if keys[pygame.K_LEFT] and circle_x - circle_radius > 0:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT] and circle_x + circle_radius < screen_width:
        circle_x += circle_speed

    # 障害物の移動
    for obstacle in obstacles:
        obstacle["x"] += obstacle["speed_x"]
        obstacle["y"] += obstacle["speed_y"]

        # 壁で跳ね返る
        if obstacle["x"] <= 0 or obstacle["x"] + obstacle["width"] >= screen_width:
            obstacle["speed_x"] *= -1
        if obstacle["y"] <= 0 or obstacle["y"] + obstacle["height"] >= screen_height:
            obstacle["speed_y"] *= -1

    # 背景を塗りつぶす
    screen.fill(white)

    # キャラクターを描画
    pygame.draw.circle(screen, blue, (circle_x, circle_y), circle_radius)

    # 障害物を描画
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, (obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"]))

        # 衝突判定
        character_rect = pygame.Rect(circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2, circle_radius * 2)
        obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"])
        if character_rect.colliderect(obstacle_rect):
            print("ゲームオーバー！")
            running = False

    # 画面を更新
    pygame.display.flip()

    # フレームレートを制御
    clock.tick(60)
