# 该程序如果需要确保比较时不区分大小写，需要保证current_users这个列表全部为小写
# 如果不是的话需要替换
current_users = ['admin', 'test', 'lc', 'osyouth', 'ymqc']
new_users = ['ymqc', 'OSYouth', 'a', 'b', 'c']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("请输入别的用户名")
    else:
        print(new_user + "这个用户名未被使用")