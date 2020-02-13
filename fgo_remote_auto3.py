# -*- coding: utf-8 -*-
##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import re
import os
import subprocess
import sys
import time
import array

###Win32のUI情報と制御用モジュール
#import win32api
#import win32gui
#import win32con

import time
from tqdm import tqdm

none_x = 1745
none_y =  658
move_FLAG = 1
battle_turn = 3

def serch_click_image(img_path, offset_x, offset_y, wait_time):
    try:
        img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=0.8)
        img_x = img_x + offset_x
        img_y = img_y + offset_y

        loc = pyautogui.position()
        print("{:27} is click ({:4}, {:4})".format(img_path, img_x, img_y))
        pyautogui.moveTo(img_x, img_y, duration=0)
        #pos         = pyautogui.locateCenterOnScreen('search.png')
        pyautogui.click(img_x,img_y)
        pyautogui.moveTo(loc[0], loc[1], duration=0)
        time.sleep(wait_time)
        return True
    except:
        print('{:27} is none'.format(img_path))
        #pyautogui.click(none_x,none_y)
        return False

def img_Judgment(img_path, wait_time, conf):
    try:
        img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=0.8)
        loc = pyautogui.position()
        print("{:27} is click ({:4}, {:4})".format(img_path, img_x, img_y))
        pyautogui.moveTo(img_x, img_y, duration=0)
        #pos         = pyautogui.locateCenterOnScreen('search.png')
        pyautogui.moveTo(loc[0], loc[1], duration=0)
        time.sleep(wait_time)
        return True
    except:
        print('{:27} is none'.format(img_path))
        #pyautogui.click(none_x,none_y)
        return False


def serch_click_image2(img_path, none_x, none_y, wait_time, conf):
    try:
        img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
        #print(img_x)
        loc = pyautogui.position()
        print("{:27} is click ({:4}, {:4})".format(img_path, img_x, img_y))
        pyautogui.moveTo(img_x, img_y, duration=0)
        #pos         = pyautogui.locateCenterOnScreen('search.png')
        pyautogui.click(img_x,img_y)
        pyautogui.moveTo(loc[0], loc[1], duration=0)
        time.sleep(wait_time)
        return True
    except:
        print('{:27} is none'.format(img_path))
        #pyautogui.click(none_x,none_y)
        return False


def serch_click_image3(img_path, img_path2, img_path3, none_x, none_y, wait_time, conf):
    try:
        img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
        #print(img_x)
        loc = pyautogui.position()
        print("X:{}, Y:{}, {}".format(img_x, img_y, img_path))
        pyautogui.moveTo(img_x, img_y, duration=0)
        #pos         = pyautogui.locateCenterOnScreen('search.png')
        pyautogui.click(img_x,img_y)
        pyautogui.moveTo(loc[0], loc[1], duration=0)
        for _ in range(wait_time):
            if(serch_click_image2(img_path2, none_x, none_y, wait_time, conf)):
                break
            if(serch_click_image2(img_path3, none_x, none_y, wait_time, conf)):
                break

            time.sleep(1)
        return True
    except:
        print(img_path + ' is none')
        #pyautogui.click(none_x,none_y)
        return False

def serch_click_image_all(img_path, none_x, none_y, wait_time):
    print(img_path)
    for pos in pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=0.9):
        cpos = pyautogui.center(pos)
        print("X:{}, Y:{}, {}".format(cpos[0], cpos[1], img_path))
        #画像の中心をクリックする
        loc = pyautogui.position()
        pyautogui.click(cpos)
        pyautogui.moveTo(loc[0], loc[1], duration=0)
        pyautogui.click(loc)
        time.sleep(wait_time)


        if(serch_click_image('./img/syutugeki02.PNG', none_x, none_y, 0)):
            return 1

        if(serch_click_image('./img/kaihi.PNG', none_x, none_y, 0)):
            serch_click_image('./img/syutugeki01.PNG', none_x, none_y, 1)
            return 1

    return True

def serch_click_image_all2(img_path, none_x, none_y, wait_time, confidence):
    print(img_path)
    #confidence = 0.95
    box = pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=confidence)
    count_max = len(list(box))
    for i, pos in enumerate(pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=confidence)):
        (x,y) = pyautogui.center(pos)
        print("({}/{})X:{}, Y:{}, {}".format(i+1, count_max, x, y, img_path))
        #画像の中心をクリックする
        loc = pyautogui.position()
        #pyautogui.moveTo(x+30,y+30, duration=4)

        offset = 0
        pyautogui.click(x+offset,y+offset)
        #pyautogui.moveTo(loc[0], loc[1], duration=0)
        #pyautogui.click(loc)
        time.sleep(wait_time)
    return True

def itaku():

    serch_click_image2('./img/itaku_comp_FLAG.png', none_x, none_y, 1, 0.8)
    serch_click_image2('./img/itaku_1h.PNG', none_x, none_y, 1, 0.8)
    serch_click_image2('./img/osusume.PNG', none_x, none_y, 0, 0.9)
    serch_click_image2('./img/itaku_kaishi.PNG', none_x, none_y, 0, 0.9)

    serch_click_image2('./img/itaku_comp_FLAG.png', none_x, none_y, 1, 0.9)
    serch_click_image2('./img/itaku_01.PNG', none_x, none_y, 1, 0.8)
    serch_click_image('./img/osusume.PNG', none_x, none_y, 0)
    serch_click_image('./img/itaku_kaishi.PNG', none_x, none_y, 0)

    serch_click_image2('./img/itaku_comp_FLAG.png', none_x, none_y, 1, 0.9)
    serch_click_image2('./img/itaku_02.PNG', none_x, none_y, 1, 0.8)
    serch_click_image('./img/osusume.PNG', none_x, none_y, 0)
    serch_click_image('./img/itaku_kaishi.PNG', none_x, none_y, 0)


def main():
    #serch_click_image_all2('./img/level3.PNG', none_x, none_y, 0)
    serch_click_image('./img/fgo/next.PNG', 0, 200, 1)
    serch_click_image('./img/fgo/next.PNG', 0, 400, 1)
    serch_click_image('./img/fgo/next.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/next3.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/next3.PNG', 0, 300, 1)

    #serch_click_image2('./img/fgo/Sun_Tane_jou2.PNG', 0, 300, 1, 0.95)
    #serch_click_image2('./img/fgo/Sun_Tsurugi_tyu.PNG', 0, 300, 1, 0.95)
    serch_click_image2('./img/fgo/Q_free.PNG', 0, 0, 1, 0.95)

    serch_click_image('./img/fgo/AP15.PNG', 0, 0, 1)
    #serch_click_image('./img/fgo/new.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/bar.PNG', 0, 200, 1)
    
    serch_click_image('./img/fgo/friend_send.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/lv.PNG', 0, 0, 1)
    
    serch_click_image('./img/fgo/battle_contine.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/close.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/close2.PNG', 0, 0, 1)
    
    

    serch_click_image('./img/fgo/end.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/q_start.PNG', 0, 0, 1)
    
    serch_click_image2('./img/fgo/skip.PNG', 0, 0, 0, 0.7)
    serch_click_image('./img/fgo/skip.PNG', 0, 0, 0)
    serch_click_image2('./img/fgo/skip.PNG', 0, 0, 0, 0.6)

    serch_click_image('./img/fgo/yes.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/sheild.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/attack.PNG', 0, 0, 1)
    #
    # confidence = 0.95
    serch_click_image('./img/fgo/weak.PNG', -50, 200, 0)
    #serch_click_image('./img/fgo/weak.PNG', -50, 200, 0)
    #serch_click_image('./img/fgo/weak.PNG', -50, 200, 0)

    if(serch_click_image('./img/fgo/battle_speed.PNG', 0, 300, 0)):
        
        if(serch_click_image2('./img/fgo/round3_3.PNG', 0, 0, 0, 0.8)):
            serch_click_image2('./img/fgo/ex_red.PNG', 0, 0, 0, 0.8)
            serch_click_image2('./img/fgo/ex_green.PNG', 0, 0, 0, 0.8)
            serch_click_image2('./img/fgo/ex_blue.PNG', 0, 0, 0, 0.8)

        serch_click_image2('./img/fgo/A3.PNG', 0, 0, 0, 0.7)
        serch_click_image2('./img/fgo/A3.PNG', 0, 0, 0, 0.7)
        serch_click_image2('./img/fgo/A3.PNG', 0, 0, 0, 0.7)

        serch_click_image('./img/fgo/B3.PNG', 0, 0, 0)
        serch_click_image('./img/fgo/B3.PNG', 0, 0, 0)
        serch_click_image('./img/fgo/B3.PNG', 0, 0, 0)

        serch_click_image('./img/fgo/Q3.PNG', 0, 0, 0)
        serch_click_image('./img/fgo/Q3.PNG', 0, 0, 0)
        serch_click_image('./img/fgo/Q3.PNG', 0, 0, 0)

    serch_click_image('./img/fgo/kizuna.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/getEXP.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/next2.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/Q_claer.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/Q_claer.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/lvUp2.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/lvUp2.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/retreat.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/decide.PNG', 0, 0, 1)
    


    print("============>  time.sleep")
    time.sleep(1)
    #aaa
    #serch_click_image_all2('./img/level2.PNG', none_x, none_y, 0)
    #serch_click_image('./img/boss.PNG', none_x, none_y, 3)
    #serch_click_image_all2('./img/level1.PNG', none_x, none_y, 0)

def story():
    #serch_click_image_all2('./img/level3.PNG', none_x, none_y, 0)
    serch_click_image('./img/fgo/next.PNG', 0, 200, 1)
    serch_click_image('./img/fgo/next.PNG', 0, 400, 1)
    serch_click_image('./img/fgo/next.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/next3.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/next3.PNG', 0, 300, 1)

    #serch_click_image2('./img/fgo/Sun_Tane_jou2.PNG', 0, 300, 1, 0.95)
    #serch_click_image2('./img/fgo/Sun_Tsurugi_tyu.PNG', 0, 300, 1, 0.95)
    #serch_click_image2('./img/fgo/Q_free.PNG', 0, 0, 1, 0.95)

    #serch_click_image('./img/fgo/AP15.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/new.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/bar.PNG', 0, 200, 1)
    
    serch_click_image('./img/fgo/friend_send.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/lv.PNG', 0, 0, 1)
    
    serch_click_image('./img/fgo/close.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/close2.PNG', 0, 0, 1)
    #serch_click_image('./img/fgo/battle_contine.PNG', 0, 0, 1)
    

    serch_click_image('./img/fgo/end.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/q_start.PNG', 0, 0, 1)
    
    serch_click_image2('./img/fgo/skip.PNG', 0, 0, 0, 0.7)
    serch_click_image('./img/fgo/skip.PNG', 0, 0, 0)
    serch_click_image2('./img/fgo/skip.PNG', 0, 0, 0, 0.6)

    serch_click_image('./img/fgo/yes.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/attack.PNG', 0, 0, 1)
    #
    # confidence = 0.95
    serch_click_image('./img/fgo/weak.PNG', -50, 200, 0)
    #serch_click_image('./img/fgo/weak.PNG', -50, 200, 0)
    #serch_click_image('./img/fgo/weak.PNG', -50, 200, 0)

    if(serch_click_image('./img/fgo/battle_speed.PNG', 0, 300, 0)):
        
        if(serch_click_image2('./img/fgo/round3_3.PNG', 0, 0, 0, 0.8)):
            serch_click_image2('./img/fgo/ex_red.PNG', 0, 0, 0, 0.8)
            serch_click_image2('./img/fgo/ex_green.PNG', 0, 0, 0, 0.8)

        serch_click_image2('./img/fgo/A3.PNG', 0, 0, 0, 0.7)
        serch_click_image2('./img/fgo/A3.PNG', 0, 0, 0, 0.7)
        serch_click_image2('./img/fgo/A3.PNG', 0, 0, 0, 0.7)

        serch_click_image('./img/fgo/B3.PNG', 0, 0, 0)
        serch_click_image('./img/fgo/B3.PNG', 0, 0, 0)
        serch_click_image('./img/fgo/B3.PNG', 0, 0, 0)

        serch_click_image('./img/fgo/Q3.PNG', 0, 0, 0)
        serch_click_image('./img/fgo/Q3.PNG', 0, 0, 0)
        serch_click_image('./img/fgo/Q3.PNG', 0, 0, 0)

    serch_click_image('./img/fgo/kizuna.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/getEXP.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/next2.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/Q_claer.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/Q_claer.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/lvUp2.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/lvUp2.PNG', 0, 0, 1)

    serch_click_image('./img/fgo/retreat.PNG', 0, 0, 1)
    serch_click_image('./img/fgo/decide.PNG', 0, 0, 1)
    
    print("============>  time.sleep")
    time.sleep(1)
    #aaa
    #serch_click_image_all2('./img/level2.PNG', none_x, none_y, 0)
    #serch_click_image('./img/boss.PNG', none_x, none_y, 3)
    #serch_click_image_all2('./img/level1.PNG', none_x, none_y, 0)

def Valentine_2020():
    global battle_turn

    if(serch_click_image2('./img/fgo_remote/battle_2_3_v2.PNG', 0, 0, 1, 0.95)):
        battle_turn = 3
    elif serch_click_image2('./img/fgo_remote/battle_3_3_v3.PNG', 0, 0, 1, 0.95):
        battle_turn = 3
    elif serch_click_image2('./img/fgo_remote/boss_1.PNG', 0, 0, 1, 0.95):
        battle_turn = 3
    elif serch_click_image2('./img/fgo_remote/tapioka2.PNG', 0, 0, 1, 0.95):
        serch_click_image2('./img/fgo_remote/close2.PNG', 0, 0, 1, 0.9)
        battle_turn = 3

    
    if(battle_turn==3):
        serch_click_image2('./img/fgo_remote/tate.PNG', 0, 0, 1, 0.8)
        serch_click_image2('./img/fgo_remote/decide3.PNG', 0, 0, 1, 0.8)
        serch_click_image2('./img/fgo_remote/makura.PNG', 0, 0, 1, 0.8)

        serch_click_image2('./img/fgo_remote/tate2.PNG', 0, 0, 1, 0.8)
        serch_click_image2('./img/fgo_remote/decide3.PNG', 0, 0, 1, 0.8)

        serch_click_image2('./img/fgo_remote/attack_skill.PNG', 0, 0, 1, 0.8)
        serch_click_image2('./img/fgo_remote/decide3.PNG', 0, 0, 1, 0.8)

  
    serch_click_image2('./img/fgo_remote/kirakira35p.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/week_class4.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/week_class5.PNG', 0, 0, 1, 0.8)
    if serch_click_image2('./img/fgo_remote/quest_start2.PNG', 0, 0, 1, 0.8):
        battle_turn = 3

    serch_click_image2('./img/fgo_remote/item_not_used2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/attack2.PNG', 0, 0, 4, 0.8)

    if(battle_turn==3):
        serch_click_image2('./img/fgo_remote/noble_weapon/sukasaha.PNG', 0, 0, 1, 0.8)
        serch_click_image2('./img/fgo_remote/noble_weapon/nago.PNG', 0, 0, 1, 0.8)
        serch_click_image2('./img/fgo_remote/noble_weapon/mash.PNG', 0, 0, 1, 0.8)

    serch_click_image2('./img/fgo_remote/arts2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/arts2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/arts2.PNG', 0, 0, 1, 0.8)

    serch_click_image2('./img/fgo_remote/buster2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/buster2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/buster2.PNG', 0, 0, 1, 0.8)

    serch_click_image2('./img/fgo_remote/quick2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/quick2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/quick2.PNG', 0, 0, 1, 0.8)

    serch_click_image2('./img/fgo_remote/kizuna_lv.PNG', 0, 0, 2, 0.8)
    serch_click_image2('./img/fgo_remote/get_kizuna2.PNG', 0, 0, 2, 0.8)
    serch_click_image2('./img/fgo_remote/get_kizuna2.PNG', 0, 0, 2, 0.8)
    serch_click_image2('./img/fgo_remote/next2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/next2.PNG', 0, 0, 1, 0.8)

    serch_click_image2('./img/fgo_remote/battle_Continuous2.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/silver_apple.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/g_apple.PNG', 0, 0, 1, 0.8)
    serch_click_image2('./img/fgo_remote/decide4.PNG', 0, 0, 1, 0.8)

    time.sleep(5)
    



#以下、メインルーチン
if __name__ == "__main__":
    #実行前の待機(秒)
    time.sleep(1)
    none_x = 1745
    none_y =  658
    count = 0
    base_t = time.time()
    t = 0
    expedi_FLAG = False

    while 1:
        Valentine_2020()
        #story()
        
