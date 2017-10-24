#!/usr/bin/env python

#   购物车
#	用户入口
#	1商品信息存在文件里
#	2已购商品，余额记录
#	商家入口
#	1可以修改商品价格，添加新商品

__author__ = "Zhou ShunCheng"

class Shopping_cart():

    def __init__(self,username):
        self.username = username
        self.items = []
        # 读取商品文件,转为二级列表items
        shopping_cart_file = 'shopping_cart.txt'
        with open(shopping_cart_file, 'r') as items_file:
            items_list = items_file.readlines()
            for item in items_list:
                item = item.rstrip()
                self.items.append(item.split('|'))

        self.users = []
        #读取用户名,余额,已购物品文件，转为二级列表user
        users_file = 'users_shoplist.txt'
        with open(users_file, 'r') as users_information_file:
            users = users_information_file.readlines()
            for user_str in users:
                user_str = user.rstrip()
                self.users.append(user_str.split('|'))




#验证用户名/密码函数
def user_confirm(username_input,userpassword_input):
    #将用户名/密码文件转为列表
    userinform_file = 'user_inform.txt'
    users_inform = []
    with open(userinform_file, 'r') as userinform:
        users = userinform.readlines()
        for user in users:
            user = user.rstrip('\n')
            users_inform.append(user.split('|'))
    #验证用户名/密码
    for user_information in users_inform:
        if username_input == user_information[0]:
            if userpassword_input == user_information[1]:
                print("转到购物车页面")
                break
                #转到购物车
            else:
                print("password error!")
                # 调用用户登录模块
                user_login()
        else:
            continue
    else:
        #新用户，存入用户名密码到列表中，打印欢迎信息
        new_user = [username_input,userpassword_input]
        new_user_str = ''
        new_user_str = '|'.join(new_user)
        print("welcome!{}!you are the NO.{} user.".format(username_input,len(users_inform)+1))
        #将用户名密码列表存入文件。
        with open(userinform_file, 'a') as userinform:
            userinform.write("\n"+new_user_str)


#用户登录模块
def user_login():
    username = input("please input your name(press 'b' to exit):")
    if username != 'b':
        pass
    else:
        exit()
    userpassword = input("please input your password:")
    user_confirm(username,userpassword)

#程序开始
if __name__ == '__main__':
    user_login()