#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：
日期：
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数
def name_to_number(name):
	if name=="石头":
		return int(0)
	elif name=="史波克":
		return int(1)
	elif name=="布":
		return int(2)
	elif name=="蜥蜴":
		return int(3)
	elif name=="剪刀":
		return int(4)
	else:
		return int(5)
		


    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


    #编写执行代码,代码完成后将pass删除


def number_to_name(number):
	if number==0:
		return "石头"
	elif number==1:
		return "史波克"
	elif number==3:
		return "蜥蜴"
	elif number==4:
		return "剪刀"
	elif number==2:
		return "布"

   

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

    #编写执行代码,代码完成后将pass删除


def rpsls(player_choice):
	number=name_to_number(player_choice)
	print("----------------")
	if number==5:
		return print("Error: No Correct Name")
	elif c-number==2 or c-number==1 or number-c==3 or number-c==4:
		print("您的选择是：",number_to_name(number))
		print("计算机的选择是：",number_to_name(c))
		print("您赢了！")
	elif number-c==2 or number-c==1 or c-number==3 or c-number==4:
		print("您的选择是：",number_to_name(number))
		print("计算机的选择是：",number_to_name(c))
		print("您输了！")
	else:
		print("您的选择是：",number_to_name(number))
		print("计算机的选择是：",number_to_name(c))
		print("平局")
		
	
   

    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

     #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
c = int(random.randint(0, 4))
rpsls(choice_name)


