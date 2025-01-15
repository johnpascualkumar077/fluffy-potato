import pygame
import sys

# Pygameの初期化
pygame.init()

# ウィンドウサイズとタイトル
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("シンプルなPygameウィンドウ")

# 色の定義 (RGB)
white = (255, 255, 255)
blue = (0, 0, 255)

# ゲームループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 閉じるボタンをクリックしたら終了
            pygame.quit()
            sys.exit()

    # 背景色を白で塗りつぶす
    screen.fill(white)

    # 青い円を描画
    pygame.draw.circle(screen, blue, (400, 300), 50)

    # 画面を更新
    pygame.display.flip()
