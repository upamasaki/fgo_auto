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


def serch_click_image(img_path, offset_x, offset_y, wait_time):
	try:
		img_x,img_y = pyautogui.locateCenterOnScreen(img_path, grayscale=True, confidence=0.8)
        img_x = img_x + offset_x
        img_y = img_y + offset_y

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
	confidence = 0.8
	box = pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=confidence)
	count_max = len(list(box))
	for i, pos in enumerate(pyautogui.locateAllOnScreen(img_path, grayscale=True, confidence=confidence)):
		(x,y) = pyautogui.center(pos)
		print("({}/{})X:{}, Y:{}, {}".format(i+1, count_max, x, y, img_path))
		#画像の中心をクリックする
		loc = pyautogui.position()
		#pyautogui.moveTo(x+30,y+30, duration=4)

		offset = 40
		pyautogui.click(x+offset,y+offset)
		pyautogui.moveTo(loc[0], loc[1], duration=0)
		#pyautogui.click(loc)
		time.sleep(wait_time)

		if(serch_click_image('./img/syutugeki02.PNG', none_x, none_y, 0)):
			return 1

		if(serch_click_image('./img/kaihi.PNG', none_x, none_y, 0)):
			serch_click_image('./img/syutugeki01.PNG', none_x, none_y, 2)
			return 1

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
	serch_click_image('./img/fgo/next.PNG', 0, 20, 3)
    #aaa
	#serch_click_image_all2('./img/level2.PNG', none_x, none_y, 0)
	#serch_click_image('./img/boss.PNG', none_x, none_y, 3)
	#serch_click_image_all2('./img/level1.PNG', none_x, none_y, 0)



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
