def check_password(s):
    f = True
    cn = "!@#$%*"
    ccnt = cnt = 0
    if len(s) < 10:
        f = False
    if s == s.lower():
        f = False
    for i in s:
        if i in cn:
            ccnt += 1
        if i.isdigit():
            cnt += 1
    else:
        if cnt < 3 or ccnt == 0:
            f = False

    print("Perfect password" if f else "Easy peasy")


check_password("Qwerty1357!")
