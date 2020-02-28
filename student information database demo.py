dict1 ={}
def main():
    print("---------------------")
    print("    星系管理系统")
    print("1.添加名片")
    print("2.修改名片")
    print("3.删除名片")
    print("4.查看名片")
    print("5.列出名片表")
    print("6.退出")
    print("---------------------")
    case()



def case():
    print("---------------------")
    print("---------------------")
    chooles_number = int(input("请输入要选择的功能序号："))
    if chooles_number == 1:
        add()
    elif chooles_number == 2:
        change()
    elif chooles_number == 3:
        delete()
    elif chooles_number == 4:
        select()
    elif chooles_number == 5:
        check()
    elif chooles_number == 6:
        exit()
    else:
        print("输入错误是否退出")
        YN = input("请输入Y/N：")
        if YN == "y" or YN == "Y":
            main()
        else:
            case()

def add():
    print()
    print("---------------------")
    insert_id = input("请输入要输入名片的人名:")
    dict1[insert_id]= input("请输入名片的信息:")
    YN = input("是否继续输入 请输入Y/N:")
    if YN == "y" or YN == "Y":
        add()
    else:
        main()

def change():
    print()
    print("---------------------")
    if len(dict1) != 0:
        cha_ID = input("请输入要修改的名片的人名:")
        dict1[cha_ID] = input("请输入修改信息：")
        print("修改成功")
        YN = input("是否继续输入 请输入Y/N:")
        if YN == "y" or YN == "Y":
            change()
        else:
            main()
    else:
        print("列表为空")
        YN = input("是否继续输入 请输入Y/N:")
        if YN == "y" or YN == "Y":
            change()
        else:
            main()

def select():
    if len(dict1) != 0:
        sel_ID =input("请输入要查找的值：")
        v = dict1[sel_ID]
        if v == '':
            print("未查找到该数据！")
            YN = input("是否继续输入 请输入Y/N:")
            if YN == "y" or YN == "Y":
                select()
            else:
                main()
        else:
            print(dict1[sel_ID])
            YN = input("是否继续输入 请输入Y/N:")
            if YN == "y" or YN == "Y":
                select()
            else:
                main()
    else:
        print("列表为空！")
        YN = input("是否继续输入 请输入Y/N:")
        if YN == "y" or YN == "Y":
            select()
        else:
            main()

def delete():
    print()
    print("---------------------")
    if len(dict1) != 0:
        del_ID = input("请输入要删除的名片的人名:")
        del dict1[del_ID]
        print("删除成功")
        YN = input("是否继续输入 请输入Y/N:")
        if YN == "y" or YN == "Y":
            delete()
        else:
            main()
    else:
        print("列表为空")
        YN = input("是否继续输入 请输入Y/N:")
        if YN == "y" or YN == "Y":
            delete()
        else:
            main()

def check():
    print("ID : %s" %dict1.items())
    YN = input("是否继续输入 请输入Y/N")
    if YN == "y" or YN == "Y":
        add()
    else:
        main()




main()