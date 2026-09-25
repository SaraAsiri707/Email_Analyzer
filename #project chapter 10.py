#project chapter 10
file=input("Enter a file name:")
try:
    fhandle=open(file)
except:
    print('File cannot found')
    exit()
sender_counts=dict()
day_counts=dict()
hour_counts=dict()
count=0
for line in fhandle:
    if line.startswith('From '): 
        count+=1
        words=line.split()
        email=words[1]
        day=words[2]
        time=words[5]
        hour=time.find(':')
        hour1=time[:hour]

        if email not in sender_counts:
            sender_counts[email]=1
        else:
            sender_counts[email]+=1

        if day not in day_counts:
            day_counts[day]=1
        else:
            day_counts[day]+=1

        if hour1 not in hour_counts:
            hour_counts[hour1]=1
        else:
            hour_counts[hour1]+=1
       
hour_list=list()
for hour,num in hour_counts.items():
    hour_list.append((hour,num))
hour_list.sort()

top_senders=list()
for sender,number in sender_counts.items():
    top_senders.append((number,sender))
top_senders.sort(reverse=True)

print('========== EMAIL ANALYZER ==========')
print('\nTotal messages:', count)
print('\nMessages from each email:',top_senders)   
print('\nTop sender:',top_senders[0])
print('\nMessages by day:',day_counts)
print('\nMessages by hour:',hour_list)
print('\nTop 10 senders:',top_senders[:10])



    