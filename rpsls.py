#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��
def name_to_number(name):
	if name=="ʯͷ":
		return int(0)
	elif name=="ʷ����":
		return int(1)
	elif name=="��":
		return int(2)
	elif name=="����":
		return int(3)
	elif name=="����":
		return int(4)
	else:
		return int(5)
		


    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
	if number==0:
		return "ʯͷ"
	elif number==1:
		return "ʷ����"
	elif number==3:
		return "����"
	elif number==4:
		return "����"
	elif number==2:
		return "��"

   

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
	number=name_to_number(player_choice)
	print("----------------")
	if number==5:
		return print("Error: No Correct Name")
	elif c-number==2 or c-number==1 or number-c==3 or number-c==4:
		print("����ѡ���ǣ�",number_to_name(number))
		print("�������ѡ���ǣ�",number_to_name(c))
		print("��Ӯ�ˣ�")
	elif number-c==2 or number-c==1 or c-number==3 or c-number==4:
		print("����ѡ���ǣ�",number_to_name(number))
		print("�������ѡ���ǣ�",number_to_name(c))
		print("�����ˣ�")
	else:
		print("����ѡ���ǣ�",number_to_name(number))
		print("�������ѡ���ǣ�",number_to_name(c))
		print("ƽ��")
		
	
   

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

     #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
c = int(random.randint(0, 4))
rpsls(choice_name)


