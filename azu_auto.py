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
		#pyautogui.click(none_x,none_y)
		return False

def serch_click_image2(img_path, none_x, none_y, wait_time, conf):
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
			serch_click_image('./img/syutugeki01.PNG', none_x, none_y, 2)
			return 1

	return True

def serch_click_image_all2(img_path, none_x, none_y, wait_time):
	print(img_path)
	box = pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=0.95)
	count_max = len(list(box))
	for i, pos in enumerate(pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=0.95)):
		(x,y) = pyautogui.center(pos)
		print("({}/{})X:{}, Y:{}, {}".format(i+1, count_max, x, y, img_path))
		#画像の中心をクリックする
		loc = pyautogui.position()
		#pyautogui.moveTo(x+30,y+30, duration=4)
		pyautogui.click(x+30,y+30)
		pyautogui.moveTo(loc[0], loc[1], duration=0)
		#pyautogui.click(loc)
		time.sleep(wait_time)

		if(serch_click_image('./img/syutugeki02.PNG', none_x, none_y, 0)):
			return 1

		if(serch_click_image('./img/kaihi.PNG', none_x, none_y, 0)):
			serch_click_image('./img/syutugeki01.PNG', none_x, none_y, 2)
			return 1

	return True

def main():
	#serch_click_image('./img/stage01_04.PNG', none_x, none_y, 2)


	serch_click_image_all2('./img/level2.PNG', none_x, none_y, 0)
	serch_click_image_all2('./img/level1.PNG', none_x, none_y, 0)
	aaa

	serch_click_image2('./img/sea04.PNG', none_x, none_y, 0, 0.75)
	serch_click_image2('./img/sea05.PNG', none_x, none_y, 0, 0.75)
	serch_click_image2('./img/sea06.PNG', none_x, none_y, 0, 0.75)

	serch_click_image('./img/stage02_04.PNG', none_x, none_y, 2)
	serch_click_image('./img/stage03_02.PNG', none_x, none_y, 2)
	serch_click_image('./img/syutugeki01.PNG', none_x, none_y, 2)
	serch_click_image('./img/syutugeki01.PNG', none_x, none_y, 2)
	serch_click_image('./img/syutugeki02.PNG', none_x, none_y, 2)

	#serch_click_image('./img/boss.PNG', none_x, none_y, 0)
	serch_click_image_all('./img/enemy08.PNG', none_x, none_y, 0)
	#serch_click_image('./img/boss.PNG', none_x, none_y, 0)
	serch_click_image_all('./img/enemy01.PNG', none_x, none_y, 0)
	serch_click_image_all('./img/enemy02.PNG', none_x, none_y, 0)
	#serch_click_image_all('./img/enemy02.PNG', none_x, none_y, 0)
	#serch_click_image('./img/boss.PNG', none_x, none_y, 0)
	#serch_click_image('./img/boss.PNG', none_x, none_y, 0)
	serch_click_image_all('./img/enemy05.PNG', none_x, none_y, 0)
	#serch_click_image('./img/boss.PNG', none_x, none_y, 0)
	serch_click_image_all('./img/enemy06.PNG', none_x, none_y, 0)
	#serch_click_image('./img/boss.PNG', none_x, none_y, 0)
	#serch_click_image_all('./img/lv.PNG', none_x, none_y, 0)

	serch_click_image('./img/boss.PNG', none_x, none_y, 0)
	serch_click_image2('./img/boss2.PNG', none_x, none_y, 0, 0.9)

	serch_click_image('./img/tauch.PNG', none_x, none_y, 2)
	serch_click_image('./img/kakunin.PNG', none_x, none_y, 2)
	serch_click_image('./img/kakutei.PNG', none_x, none_y, 2)
	serch_click_image('./img/chara_get.PNG', none_x, none_y, 2)
	serch_click_image('./img/kaihi.PNG', none_x, none_y, 2)

	serch_click_image('./img/kirikae.PNG', none_x, none_y, 4)

	if(serch_click_image('./img/itaku.PNG', none_x, none_y, 1)):
		serch_click_image('./img/back.PNG', none_x, none_y, 0)


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
