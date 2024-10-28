import re
def check_password(password):
# defin  regular expression 
    leng_regex = re.compile(r'^.{8,}$')
    upper_regex = re.compile(r'[A-Z]')
    lower_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')
    special_regex = re.compile(r'[\w_]')

    leng_check = leng_regex.search(password)
    upper_check =upper_regex.search(password)
    lower_check = lower_regex.search(password)
    digit_check = digit_regex.search(password)
    special_check =special_regex.search(password)

    if leng_check and   upper_check and lower_check  and digit_check and  special_check:
         return True
    else:
        return False
#main

with open('passwords.txt') as f:
    for password in f:
        password = password.strip()
        if check_password(password):
            print("valid:"+password)
        else:
            print("invalid:"+password)
