dic = {}
count = int(input())

dic = dict(input().split() for x in range(count))

while True:
    try:
        key = input()
        if(key in dic):
            print("{0}={1}".format(key,dic.get(key)))
        else:
            print('Not found')
    except:
        break
    
    """
    n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
    """