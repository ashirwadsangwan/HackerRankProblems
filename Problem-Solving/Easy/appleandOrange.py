def countApplesAndOranges(s, t, a, b, apples, oranges):

    app = 0
    org = 0

    app_list = []
    org_list = []

    for i in apples:
        app_list.append(a+i)
    for j in oranges:
        org_list.append(b+j)

    for k in app_list:
        if k>=s and k<=t:
            app+=1
    for m in org_list:
        if m>=s and m<=t:
            org+=1

    print(app)
    print(org)             



if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
`
