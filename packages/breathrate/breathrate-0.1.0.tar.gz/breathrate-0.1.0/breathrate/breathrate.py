# 必要なライブラリのインポート
import cv2
import time
import _thread
from datetime import datetime
import numpy as np
from Plot import run


# Webカメラを使うときはこちら
cap = cv2.VideoCapture(1)
def camRun():

    print('time,breath',  file=open('file.csv', 'w'))
    breath_data = 1
    time_data = 1
    before = None
    count = 1
    now = datetime.now()
    nowtime= now.strftime("%H:%M:%S")
    start_time = time.time()
    breath_count = 0
    print("動体検知を開始します。")
    print(nowtime)

    while True:
        # 画像を取得
        ret, frame = cap.read()

        # 再生が終了したらループを抜ける
        if ret == False:
            break

        # 白黒画像に変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if before is None:
            before = gray.astype("float")
            continue

        # 現在のフレームと移動平均との差を計算
        cv2.accumulateWeighted(gray, before, 0.5)
        frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(before))
        
        # frameDeltaの画像を２値化
        thresh = cv2.threshold(frameDelta, 3, 255, cv2.THRESH_BINARY)[1]
        #print (thresh.mean())
        

        #　動きを計算する
        if thresh.mean() >=1 and thresh.mean() <= 100:
            breath_count = breath_count + 1
            

        # 輪郭のデータを取得
        contours = cv2.findContours(thresh,
                        cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[0]
    
        # 差分があった点を画面に描画
        for target in contours:
            x, y, w, h = cv2.boundingRect(target)
        
            
            # 小さい変更点は無視
            if w < 35:
                continue 

            areaframe = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            

            breath_data = thresh.mean().tolist()
            now = datetime.now()
            time_data = now.strftime("%H:%M:%S")
    


        # ウィンドウで表示
        cv2.imshow('BreathSense', frame)
        current_time = time.time()
        # Enterキーが押されたらループを抜ける
        if cv2.waitKey(1) == 13 or current_time - start_time > 60:
            print("closed")
            break
        
        print(str(time_data) + ',' + str(breath_data) ,  file=open('file.csv','a')) 
        




	
def breathrate():
# _thread.start_new_thread(run,())
    start_time = time.time()
    camRun()
    run()
    cap.release()
    now = datetime.now()
    nowtime= now.strftime("%H:%M:%S")
    current_time = time.time()
    test_time = current_time - start_time
    print("動体検知を終了します。")
    print(nowtime)


# ウィンドウの破棄
cv2.destroyAllWindows()

