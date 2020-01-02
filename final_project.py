#coding:gbk
"""
程序:人物关系的中gephi中节点和边的输出
作者:汪欢
"""
import jieba
import codecs
import jieba.posseg as pseg


names = {}	
relationships = {}
lineNames = []
jieba.load_userdict("F:/大计基/最终项目/dict.txt")	
with codecs.open("F:/大计基/最终项目/黎明破晓的街道.txt", "r", "gbk") as f:
	for line in f.readlines():
		poss = pseg.cut(line)
		lineNames.append([])		# 为新读入的一段添加人物名称列表
		for w in poss:
			if w.flag != "nr" or len(w.word) < 2:
				continue			# 当分词长度小于2或该词词性不为nr时认为该词不为人名
			lineNames[-1].append(w.word)
			if names.get(w.word) is None:
				names[w.word] = 0
				relationships[w.word] = {}
			names[w.word] += 1					# 该人物出现次数加1
for line in lineNames:
	for name1 in line:					
		for name2 in line:				# 每段中的任意两个人
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:		# 若两人尚未同时出现则新建项
				relationships[name1][name2]= 1
			else:
				relationships[name1][name2] = relationships[name1][name2]+ 1		# 两人共同出现次数加 1

with codecs.open("F:/大计基/最终项目/黎明破晓的街道_node.txt", "a+", "utf-8") as f:
	f.write("Id Label Weight\r\n")
	for name, times in names.items():
		f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("F:\大计基\最终项目\黎明破晓的街道_edge.txt", "a+", "utf-8") as f:
	f.write("Source Target Weight\r\n")
	for name, edges in relationships.items():
		for v, w in edges.items():
			if w > 3:
				f.write(name + " " + v + " " + str(w) + "\r\n")
