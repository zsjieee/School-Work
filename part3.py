#Part 3

def valid_username(a):
    size=len(a)
    if size<5:
       alength= False
    else:
        alength=True
        all_alnum = a.isalnum()
        if a[0].isdigit():
            adigit= False
        else:
            adigit=True
    if alength and adigit and all_alnum:
        return True
    else:
        return False

def valid_password(a):
    #valid its length
    size=len(a)
    if size<5:
        alength=False
    else:
        alength=True
        all_alnum = a.isalnum()
        if a[0].isdigit():
            adigit=False
        else:
            adigit=True
            lowers=0
            uppers=0
            digits=0
            for i in a:
                if i.islower():
                    lowers+=1
                elif i.isdigit():
                    digits+=1
                elif i.isupper():
                    uppers+=1
                if lowers==0:
                    alower=False
                else:
                    alower=True
                if uppers==0:
                    aupper=False
                else:
                    aupper=True
                if digits==0:
                    adigit=False
                else:
                    adigit=True
    if alength and adigit and all_alnum and alower and aupper and adigit:
        return True
    else:
        return False

def username_exists(a):
    if len(a)==0:
        return False
    file_name=open("user_info.txt","r")
    allname=file_name.read()
    file_name.close()
    username=allname.split('\n')
    name_time=0
    for i in username:
        name=i.split(',')
        if name[0]==a:
            name_time+=1
    if name_time==0:
        return False
    else:
        return True

def check_password(a,b):
    c=a+","+b
    file_name=open("user_info.txt","r")
    allname=file_name.read()
    file_name.close()
    username=allname.split('\n')
    match=0
    for i in username:
        if c==i:
            match+=1
    if match==0:
        return False
    else:
        return True
    
def add_user(a,b):
    if valid_username(a):
        if not username_exists(a) and valid_password(b):
            file_user=open("user_info.txt","a")
            file_user.write(a)
            file_user.write(",")
            file_user.write(b)
            file_user.write("\n")
            file_user.close()
        
def send_message(a,b,c):
    import datetime
    d=datetime.datetime.now()
    month=d.month
    day=d.day
    year=d.year
    hour=d.hour
    minute=d.minute
    second=d.second
    file_name="messages/"+b+".txt"
    file_r=open(file_name,'a')
    file_r.write(a+"|"+str(month)+"/"+str(day)+"/"+str(year)+" "+str(hour)+":"+str(minute)+":"+str(second)+"|"+c+"\n")
    file_r.close()

def print_messages(a):
    open_file="messages/"+a+".txt"
    messages_received=open(open_file,'r')
    all_message=messages_received.read()
    message=all_message.split("\n")
    if len(all_message)==0:
        print()
        print("No message in your inbox")
        print()
    else:
        number=1
        for i in message:
            if len(i)==0:
                pass
            else:
                seperate_message=i.split("|")
                print()
                print("Message #"+str(number)+" received from "+seperate_message[0])
                print("Time:",seperate_message[1])
                print(seperate_message[2]+"\n")
                number+=1
                messages_received.close()
                
def delete_messages(a):
    open_file="messages/"+a+".txt"
    messages_received=open(open_file,'w')
    all_message=messages_received.write("")

while True:
    order=input("(l)ogin, (r)egister or (q)uit: ")
    if order=="r":
        print()
        print("Register for an account")
        username=input("Username (case sensitive): ")
        password=input("Password (case sensitive): ")
        while True:
            if username_exists(username):
                print("Duplicate username, registration cancelled\n")
                break
            else:
                if valid_username(username) and valid_password(password):
                    add_user(username,password)
                    print("Registration successful!")
                    print()
                    send_message("admin",username,"Welcome to your account!")
                    break
                else:
                    print("Password is invalid, registration cancelled\n")
                    break
    elif order=="l":
        print()
        print("Log In")
        username=input("Username (case sensitive): ")
        password=input("Password (case sensitive): ")
        while True:
            print("You have been logged in successfully as",username)
            messages=input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ")
            if messages=="r":
                print_messages(username)
            elif messages=="s":
                recipient=input("Username of recipient: ")
                if username_exists(recipient):
                    message=input("Type your message: ")
                    send_message(username,recipient,message)
                    print("Message sent!")
                    print()
                else:
                    print("Unknown recipient")
                    print()
                    continue
            elif messages=="d":
                delete_messages(username)
                print("Your messages have been deleted")
                print()
            elif messages=="l":
                print("Logging out as username snorlax")
                print()
                break
    elif order=="q":
        print()
        print("Goodbye!")
        break
                
        
        
                
        
