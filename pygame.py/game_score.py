import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# ウィンドウサイズとタイトル
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("障害物を避けるゲーム")

# 色の定義 (RGB)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# フォントの設定
font = pygame.font.Font(None, 36)

# 円の初期位置とサイズ
circle_x, circle_y = 400, 300
circle_radius = 30
circle_speed = 5

# 障害物の初期位置とサイズ
obstacle_width, obstacle_height = 50, 50
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = random.randint(0, screen_height - obstacle_height)
obstacle_speed_x = random.choice([-3, 3])
obstacle_speed_y = random.choice([-3, 3])

# スコアの初期値
score = 0
clock = pygame.time.Clock()

# ゲームループ
running = True
while running:
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

    # 障害物の移動
    obstacle_x += obstacle_speed_x
    obstacle_y += obstacle_speed_y

    # 障害物が画面の端で跳ね返る
    if obstacle_x <= 0 or obstacle_x + obstacle_width >= screen_width:
        obstacle_speed_x *= -1
    if obstacle_y <= 0 or obstacle_y + obstacle_height >= screen_height:
        obstacle_speed_y *= -1

    # 衝突判定
    if (circle_x - circle_radius < obstacle_x + obstacle_width and
        circle_x + circle_radius > obstacle_x and
        circle_y - circle_radius < obstacle_y + obstacle_height and
        circle_y + circle_radius > obstacle_y):
        print("ゲームオーバー！ スコア:", score)
        running = False

    # 背景色を白で塗りつぶす
    screen.fill(white)

    # 青い円を描画
    pygame.draw.circle(screen, blue, (circle_x, circle_y), circle_radius)

    # 赤い障害物を描画
    pygame.draw.rect(screen, red, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # スコアの表示
    score_text = font.render(f"スコア: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # 画面を更新
    pygame.display.flip()

    # スコアを更新（時間経過をスコアに加算）
    score += 1

    # フレームレートの制御
    clock.tick(60)

# ゲームオーバー画面
game_over_text = font.render("ゲームオーバー！リスタートするにはRを押してください", True, black)
screen.blit(game_over_text, (screen_width // 2 - 300, screen_height // 2))
pygame.display.flip()

# リスタート待機ループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Rキーで再スタート
                exec(open(__file__).read())  # 再実行
