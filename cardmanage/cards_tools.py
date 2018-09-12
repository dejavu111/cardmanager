import re
#记录所有的名片字典
def show_menu():
    '''显示菜单'''
    print('*'*50)
    print('欢迎使用【名片管理系统V 1.0】')
    print('')
    print('1. 新增名片')
    print('2. 显示全部')
    print('3. 搜索名片')
    print('')
    print('0. 退出系统')
    print('*'*50)

def new_card():
    '''新增名片'''
    print('-'*50)
    print('新增名片')

    # 1. 提示用户输入名片信息
    name_str = input('请输入姓名:')
    phone_str = input('请输入电话:')
    qq_str = input('请输入qq:')
    email_str = input('请输入邮箱:')

    # 2. 使用用户输入信息建立名片字典
    card_dict = {'name': name_str,
                 'phone': phone_str,
                 'qq': qq_str,
                 'email': email_str}
    with open('cards_data.txt','a',encoding='UTF=8') as f:
        f.write(str(card_dict)+'\n')
    # 3. 将名片字典添加到列表中
    card_list = read_file()
    card_list.append(card_dict)

    print(card_list)

    # 4. 提示用户添加成功
    print('添加{}的名片成功'.format(name_str))

def show_all():
    '''显示所有名片'''
    print('-' * 50)
    print('显示所有名片')
    card_list = read_file()

    #判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list)==0:
        print('当前没有任何名片记录，请使用新增功能添加名片！')
        return
    # 打印表头
    for name in ['姓名','电话','QQ','邮箱']:
        print(name,end='\t\t')
    print('')
    #打印分割线
    print('=' * 50)
    #遍历名片列表依次输出字典信息：
    for card_dict in card_list:
        print('{}\t\t{}\t\t{}\t\t{}'.format(card_dict['name'],
                                            card_dict['phone'],
                                            card_dict['qq'],
                                            card_dict['email']))

def search_card():
    '''搜索名片'''
    print('-' * 50)
    print('搜索名片')

    card_list = read_file()

    #1. 提示用户输入要搜索的姓名
    find_name = input('请输入要搜索的姓名：')
    #2. 遍历名片列表查询要搜索的姓名，如果没有找的提示用户
    for num,card_dict in enumerate(card_list):

        if find_name == card_dict['name']:

            print('姓名\t\t电话\t\tQQ\t\t邮箱')
            print('='*50)
            print('{}\t\t{}\t\t{}\t\t{}'.format(card_dict['name'],
                                                    card_dict['phone'],
                                                    card_dict['qq'],
                                                   card_dict['email']))
            # 针对搜索的名片进行删除和修改操作
            card_list = deal_card(num,card_dict,card_list)
            break
        else:
            print('抱歉，没有找到{}'.format(find_name))

    with open('cards_data.txt','w+',encoding='UTF-8') as f:
        f.writelines('\n'.join([str(x) for x in card_list]))


def deal_card(num,find_dict,card_list):
    """处理查找到的名片

    :param find_dict:查找到的名片
    :return:
    """
    print(find_dict)

    action_str = input('请选择要执行的操作 '
                       '[1]修改 [2]删除 [0]返回上级菜单')

    if action_str == '0':
        return
    elif action_str == '1':
        find_dict['name'] = input_card_info(find_dict['name'],'姓名：')
        find_dict['phone'] = input_card_info(find_dict['phone'],'电话：')
        find_dict['qq'] = input_card_info(find_dict['qq'],'qq:')
        find_dict['email'] = input_card_info(find_dict['email'],'邮箱：')

        print('修改名片成功')
    elif action_str =='2':
        card_list.remove(find_dict)
        print('删除名片成功')

    return card_list

def input_card_info(dict_value,tip_message):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
    # 2. 针对用户输入内容进行判断，如果用户输入内容，直接返回结果
    # 3. 如果用户没有输入内容，返回'字典中原有的值'
    pass

def read_file():
    card_list = []
    with open('cards_data.txt','r',encoding='UTF-8') as f:
        while(True):
            str_f = f.readline()
            if str_f == '':
                break
            name = re.search("'name': '(\w*)'",str_f)[1]
            phone = re.search("'phone': '(\w*)'",str_f)[1]
            qq = re.search("'qq': '(\w*)'",str_f)[1]
            email = re.search("'email': '(\w*)'",str_f)[1]
            card_dict = {'name':name,'phone':phone,'qq':qq,'email':email}
            card_list.append(card_dict)
    return card_list