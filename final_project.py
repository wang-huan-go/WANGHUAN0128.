#coding:gbk
"""
����:�����ϵ����gephi�нڵ�ͱߵ����
����:����
"""
import jieba
import codecs
import jieba.posseg as pseg


names = {}	
relationships = {}
lineNames = []
jieba.load_userdict("F:/��ƻ�/������Ŀ/dict.txt")	
with codecs.open("F:/��ƻ�/������Ŀ/���������Ľֵ�.txt", "r", "gbk") as f:
	for line in f.readlines():
		poss = pseg.cut(line)
		lineNames.append([])		# Ϊ�¶����һ��������������б�
		for w in poss:
			if w.flag != "nr" or len(w.word) < 2:
				continue			# ���ִʳ���С��2��ôʴ��Բ�Ϊnrʱ��Ϊ�ôʲ�Ϊ����
			lineNames[-1].append(w.word)
			if names.get(w.word) is None:
				names[w.word] = 0
				relationships[w.word] = {}
			names[w.word] += 1					# ��������ִ�����1
for line in lineNames:
	for name1 in line:					
		for name2 in line:				# ÿ���е�����������
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:		# ��������δͬʱ�������½���
				relationships[name1][name2]= 1
			else:
				relationships[name1][name2] = relationships[name1][name2]+ 1		# ���˹�ͬ���ִ����� 1

with codecs.open("F:/��ƻ�/������Ŀ/���������Ľֵ�_node.txt", "a+", "utf-8") as f:
	f.write("Id Label Weight\r\n")
	for name, times in names.items():
		f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("F:\��ƻ�\������Ŀ\���������Ľֵ�_edge.txt", "a+", "utf-8") as f:
	f.write("Source Target Weight\r\n")
	for name, edges in relationships.items():
		for v, w in edges.items():
			if w > 3:
				f.write(name + " " + v + " " + str(w) + "\r\n")
