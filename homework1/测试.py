#join()函数的用法




#文件的读取与写入
'''
file_name = 'ceshi.txt'
with open(file_name,'r') as f:
    print(type(f))
    print(f)
    for line in f:
        print(type(line))
        print(line)
pass
        '''
#从文件转为二级列表
'''
file_name = 'ceshi.txt'
items = []
with open(file_name,'r') as f:
    lines = f.readlines()
    for line in lines:
        items.append(line.split())
print(items)'''


#查看字符串是否在二级列表中
'''
list = [['zsc','mm5524154'],['yrr','yrr19910606']]
for user in list:
    if 'zsc' in user:
        #验证密码
        #读取余额
    else:
        continue
else:
    #打印欢迎信息'''

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
        print("new user!")
        #新用户，存入用户名密码到列表中，打印欢迎信息

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