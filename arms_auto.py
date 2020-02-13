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

def serch_click_image2(img_path, wait_time, conf):
	try:
		img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=conf)
		#print(img_x)
		loc = pyautogui.position()
		print("X:{}, Y:{}, {}".format(img_x, img_y, img_path))
		pyautogui.moveTo(img_x, img_y, duration=0)
		#pos         = pyautogui.locateCenterOnScreen('search.png')
		pyautogui.click(img_x,img_y)
		pyautogui.moveTo(loc[0], loc[1], duration=0)
		time.sleep(wait_time)
		return True
	except:
		print(img_path + ' is none')
		return False



def main():

	#serch_click_image2('./arms_img/stage_00_03.PNG', 1, 0.9)
	serch_click_image2('./arms_img/stage_01_06.PNG', 1, 0.9)
	serch_click_image2('./arms_img/battle_go.PNG', 2, 0.9)
	serch_click_image2('./arms_img/repair.PNG', 1, 0.9)
	serch_click_image2('./arms_img/battle_go.PNG', 1, 0.9)
	serch_click_image2('./arms_img/auto_btn2.PNG', 1, 0.6)
	serch_click_image2('./arms_img/tri.PNG', 1, 0.9)
	serch_click_image2('./arms_img/tri.PNG', 1, 0.9)

#以下、メインルーチン
if __name__ == "__main__":
	while 1:
		main()
