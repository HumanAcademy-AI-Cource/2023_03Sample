#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2

# 画像を読み込み
image = cv2.imread("images/banana.png")

# グレースケール化
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 画像の表示
cv2.imshow("GrayImage", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
