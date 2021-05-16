
import re
msg_count={}
with open('_chat.txt',encoding="utf8") as f:
    for line in f:
        search=re.search(r"] ([\w\' ]*):", line.strip())
        if search!=None:
            if search[1] not in msg_count.keys():
                msg_count[search[1]]=0
            msg_count[search[1]]+=1
for i in msg_count.keys():
    if msg_count[i]>1:
        print(f'Total message(s) sent by {i} is: {msg_count[i]}')
        if msg_count[i]<msg_count['Sandeep']:
            diff=msg_count['Sandeep']-msg_count[i]
            print(f'Hey sweetie {i} you owe Sandy {diff} more messages.')
            break
