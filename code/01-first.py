# 01-First
# Author : jeeho.hyun@gmail.com
# Date : 2019-04-30
# Python version : 3.6.5

import numpy as np

def _list_stack_push(arr, val) :
	if arr is None :
		raise IOError('array not found')

	arr.append(val)

def _list_stack_pop(arr) :
	if arr is None :
		raise IOError('array not found')

	return arr.pop()

def list_stack_test() :
	arr = []
	while True :
		print('Push(1) / Pop(2) / View(3) or Quit(0) :')
		key_input = int(input())
		if key_input is 0 or key_input < 0 :
			print('Terminated')
			break
		else :
			if key_input is 1 :
				print('Input value : ')
				val_input = input()
				_list_stack_push(arr, val_input)
			elif key_input is 2 :
				val = _list_stack_pop(arr)
				print('Popped! : ', val)
			elif key_input is 3 :
				print('Current Stack status : ', arr)



if __name__ == '__main__' :
	list_stack_test()

