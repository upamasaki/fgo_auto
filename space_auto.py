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

def serch_click_image(img_path, none_x, none_y, wait_time):
	try:
		img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=0.8)
		print("X:{}, Y:{}, {}".format(img_x, img_y, img_path))
		pyautogui.moveTo(img_x, img_y, duration=0.1)
		#pos         = pyautogui.locateCenterOnScreen('search.png')
		pyautogui.click(img_x,img_y)
		time.sleep(wait_time)
		return True
	except:
		print(img_path + ' is none')
		#pyautogui.click(none_x,none_y)
		return False



def main():
	serch_click_image('./img/stage01_04.PNG', none_x, none_y, 4)
	serch_click_image('./img/syutugeki01.PNG', none_x, none_y, 4)
	serch_click_image('./img/syutugeki01.PNG', none_x, none_y, 4)
	serch_click_image('./img/syutugeki02.PNG', none_x, none_y, 4)

	serch_click_image('./img/enemy01.PNG', none_x, none_y, 10)
	serch_click_image('./img/enemy01.PNG', none_x, none_y, 10)

	serch_click_image('./img/tauch.PNG', none_x, none_y, 4)
	serch_click_image('./img/kakunin.PNG', none_x, none_y, 4)
	serch_click_image('./img/kakutei.PNG', none_x, none_y, 4)
	time.sleep(2)


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
		main()
