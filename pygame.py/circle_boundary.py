import pygame
import sys

# Pygameの初期化
pygame.init()

# ウィンドウサイズとタイトル
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("円が画面外に出ないように制限する")

# 色の定義 (RGB)
white = (255, 255, 255)
blue = (0, 0, 255)

# 円の初期位置とサイズ
circle_x, circle_y = 400, 300
circle_radius = 30
circle_speed = 5

# ゲームループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 閉じるボタンをクリックしたら終了
            pygame.quit()
            sys.exit()

    # キー入力を取得
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and circle_y - circle_radius > 0:    # 上矢印キー
        circle_y -= circle_speed
    if keys[pygame.K_DOWN] and circle_y + circle_radius < screen_height:  # 下矢印キー
        circle_y += circle_speed
    if keys[pygame.K_LEFT] and circle_x - circle_radius > 0:  # 左矢印キー
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT] and circle_x + circle_radius < screen_width: # 右矢印キー
        circle_x += circle_speed

    # 背景色を白で塗りつぶす
    screen.fill(white)

    # 青い円を描画
    pygame.draw.circle(screen, blue, (circle_x, circle_y), circle_radius)

    # 画面を更新
    pygame.display.flip()

    # フレームレートの制御
    pygame.time.Clock().tick(60)
