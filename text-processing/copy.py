import pyperclip
import time
import re

iter_1 = pyperclip.paste()
iter_3 = ''
while iter_1 != "stop ":
	time.sleep(0.1)

	iter_2 = pyperclip.paste()

	# 如果剪切板发生变化
	if len(iter_2) > 1 and iter_1 != iter_2 and iter_1 != iter_3:
		# print('监听到变化！')
		# 改变现在的剪切板
		iter_3 = re.sub(r"\s{2,}", " ", iter_2) + ' '
		# 把改变后的剪切板保存起来
		pyperclip.copy(iter_3)
		print('改变后的剪切板: '+ iter_3)

		iter_1 = iter_3
		iter_3 = ''
