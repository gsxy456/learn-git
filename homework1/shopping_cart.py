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
        # 读取商品文件,转为二级列表self.items
        shopping_cart_file = 'shopping_cart.txt'
        self.items = file_to_list(shopping_cart_file)

        #读取用户名,余额,已购物品文件，转为二级列表users_list
        users_file = 'users_shoplist.txt'
        self.users_list = file_to_list(users_file)

        #初始化列表属性：某个用户的购物清单
        for user in self.users_list:
            if username == user[0]:
                self.user_shoppingcart = user
            else:
                continue

    #打印购物车
    def show_shoplist(self):
        for item in self.items:
            print(item)

    #修改购物车内容（商家入口）
    def change_shoplist(self):
        item_choosen = input("please enter the item code you want to edit(press 'd' to delete item):")
        if item_choosen == 'd':
            #删除物品
            item_delete = input("please enter the item code you want to delete:")
            if item_delete.isdigit():
                item_code = int(item_delete)-1
                self.items.pop(item_code)
                new_list = list_to_file(self.items,'shopping_cart.txt')
                print("---delete success!---")
                print(new_list)
            else:
                print('please enter correct format!')
        elif item_choosen.isdigit():
            #编辑物品
            item_code = int(item_choosen)-1
            item_name = input("please enter the item name:")
            item_price = input("please enter the price:")
            self.items[item_code] = [item_choosen,item_name,item_price]
            #将商品信息存入文件
            list_to_file(self.items,'shopping_cart.txt')
            #打印商品信息
            self.show_shoplist()

        else:
            print("please enter correct item code!")

    #添加商品（用户入口）,输入商品编号，自动扣除余额，添加商品，如余额不够则提示
    def add_item(self,item_str):
        #判断输入是否为数值
        if item_str.isdigit():
            item_code = int(item_str)
            #判断是否买得起
            if int(self.user_shoppingcart[1]) >= int(self.items[item_code][2]):
                #修改用户余额，购物车
                self.user_shoppingcart[1] = str(int(self.user_shoppingcart[1]) - int(self.items[item_code][2]))
                self.user_shoppingcart.append(self.items[item_code][1])
                return
            #买不起的情况
            else:
                print('you can\'t afford it!')
                return
        #输入错误的情况
        else:
            print("format error!")
            return

    #存放购物目录
    def save_shoplist(self):
        #把用户购物车存入用户总购物表中
        for user in self.users_list:
            if self.user_shoppingcart[0] == user[0]:
                user =


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
                #转到购物车页面
                user_shoppingcart = Shopping_cart(username_input)

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
        #请用户输入余额数字，将余额数字存入users_shoplist中
        salary = input('hey!you are new customer!please enter your salary here...')
        usershoplist = 'users_shoplist.txt'
        if salary.isdigit():
            new_user_shoplist = [username_input,salary]
            usershoplist_str = '|'.join(new_user_shoplist)
            with open(usershoplist,'a') as shoplist:
                shoplist.write('\n'+usershoplist_str)
            #转到购物车页面

        else:
            print("please enter the correct format!")

#列表转文件函数，输入为列表和文件名字符串，返回值为文件内容字符串
def list_to_file(list_input,filename):
    #将二级列表转为字符串
    list_str = ''
    for secondary_list in list_input:
        list_str = list_str + '|'.join(secondary_list) + '\n'
    #将字符串写入文件
    with open(filename,'w') as f:
        f.write(list_str)
    return list_str

#文件转列表函数，输入为文件名字符串，返回值为二级列表
def file_to_list(filename):
    with open(filename, 'r') as f:
        list_output = []
        str_list = f.readlines()
        for string in str_list:
            list_output.append(string.rstrip().split('|'))
    return list_output

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