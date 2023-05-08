#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2

# 画像を読み込み
image = cv2.imread("images/banana.png")

# グレースケールに変換
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2値化
ret, img_thresh = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

# 画像を表示
cv2.imshow("Result", img_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
