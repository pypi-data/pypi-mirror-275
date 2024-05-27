import random
import requests
from PIL import Image
from io import BytesIO
from apscheduler.schedulers.blocking import BlockingScheduler
import matplotlib
matplotlib.use('Agg')  # GUIを使わないバックエンドを使用
import matplotlib.pyplot as plt

# ハンバーガー店のリスト（例）
burger_shops = [
    {"name": "DQ Grill&Chill", "location": "CAN", "image_url": "https://dairyqueen-prod.dotcdn.io/dA/61d26f8b33/fileAsset/backyard_bacon_ranch_US_duo.png/webp","URL":"https://www.dairyqueen.com/en-us/"},
    {"name": "In-N-Out Burger", "location": "California", "image_url": "https://www.in-n-out.com/ResourcePackages/INNOUT/content/images/menu/hamburger-meal.png?package=INNOUT&v=2023","URL":"https://www.in-n-out.com/menu"},
    {"name": "Smashburger", "location": "Washington, D.C", "image_url": "https://smashburger.com/cdn-cgi/image/format=auto,width=1220,quality=75/https://sbprod-web-assets.s3.us-west-2.amazonaws.com/smashburger_double_classic_hero_195c5015ee.png","URL":"https://smashburger.com/"},
    {"name": "shakeshack", "location": "Tokyo,aoyama", "image_url": "https://shakeshack.jp/wp2/wp-content/themes/shake_shack/assets/img/menu/sec_01/022.jpg","URL":"https://shakeshack.jp/"},
    # 他のハンバーガー店を追加
]

def notify_burger_shop():
    # ランダムにハンバーガー店を選ぶ
    shop = random.choice(burger_shops)
    name = shop["name"]
    location = shop["location"]
    image_url = shop["image_url"]
    URL = shop["URL"]

    print(f"Selected shop: {name} in {location}")
    print(f"Image URL: {image_url}")
    print(f"home page URL: {URL}")

    try:
        # 画像をダウンロードして表示
        response = requests.get(image_url)
        response.raise_for_status()  # HTTPエラーが発生した場合は例外を発生させる
        img = Image.open(BytesIO(response.content))
        
        # 画像を表示
        plt.imshow(img)
        plt.title(f"{name} in {location}")
        plt.axis('off')  # 軸を非表示
        plt.savefig(f"{name}.png")  # 画像をファイルに保存
        plt.close()  # プロットを閉じる
        print(f"Image saved as {name}.png")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    except Exception as e:
        print(f"Error displaying image: {e}")
    
    # 通知メッセージを作成
    print(f"Today's recommended burger shop: {name} in {location}")

# スケジューラの設定
scheduler = BlockingScheduler()
# 毎日午前9時に実行するように設定
scheduler.add_job(notify_burger_shop, 'cron', hour=9, minute=0)

try:
    print("Burger shop reminder started.")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("Burger shop reminder stopped.")






# burger_shops = [
#     {"name": "DQ Grill&Chill", "location": "CAN", "image_url": "https://dairyqueen-prod.dotcdn.io/dA/61d26f8b33/fileAsset/backyard_bacon_ranch_US_duo.png/webp"},
#     {"name": "In-N-Out Burger", "location": "California", "image_url": "https://www.in-n-out.com/ResourcePackages/INNOUT/content/images/menu/hamburger-meal.png?package=INNOUT&v=2023"},
#     {"name": "Smashburger", "location": "Washington, D.C", "image_url": "https://smashburger.com/cdn-cgi/image/format=auto,width=1220,quality=75/https://sbprod-web-assets.s3.us-west-2.amazonaws.com/smashburger_double_classic_hero_195c5015ee.png"},
#     {"name": "shakeshack", "location": "Tokyo,aoyama", "image_url": "https://shakeshack.jp/wp2/wp-content/themes/shake_shack/assets/img/menu/sec_01/022.jpg"},
#     # 他のハンバーガー店を追加
# ]