#Part 2

openquiz=open("quizzes.txt","r")
quizzes=openquiz.read()
while True:
    print()
    print("NYU Quizzing System - Main Menu")
    order=str.lower(input("(q)uiz info, (s)core or (e)xit: "))
    if order=="s":
        filename=input("Enter a filename to score: ")
        try:
            fileconnect = open(filename,"r")
        except:
            print("File not found.")
        else:
            total=0
            answer=""
            summary=[]
            fileopen=fileconnect.read()
            filelist=fileopen.split("\n")
            number_question=len(filelist)-2
            print("This file contains",number_question,"student entries for the test"+' "'+filelist[0]+'"')
            quizspilt=quizzes.split("\n")
            for i in quizspilt:
                quizsplit1=i.split(",")
                if filelist[0] == quizsplit1[0]:
                    answer+=quizsplit1[1] 
                    print("The answer key for this test is:",answer)
            del filelist[0]
            del filelist[-1]
            for j in filelist:
                filelist1=j.split(",")
                for k in range(0, len(answer)):
                    if filelist1[1][k]==answer[k]:
                        total+=1
                percentage=(total/len(answer))*100 
                print(filelist1[0]," earned ",total," out of ",len(answer)," (",format(percentage,".2f"),"%)",sep="")
                summary+=[total]
                total=0
                percentage=0
            summ=sorted(summary)
            a=0
            occurrence =[]
            mode=[]
            while a<len(summ):
                occurrence.append(summ.count(summ[a]))
                a+=1
            highest=max(occurrence)
            b=0
            c=len(occurrence)
            while b<c:
                if occurrence[b]==highest:
                    if not summ[b] in mode:
                        mode+=[summ[b]]
                b+=1
            modestring=""
            for z in mode:
                modestring+=str(z)+" "
            print()
            print("*** Class Report ***")
            print("Average score:",format(sum(summary)/number_question,".2f"))
            print("Highest score:",max(summary))
            print("Lowest score:",min(summary))
            print("Range of scores:",max(summary)-min(summary))
            print("Mode(s):",modestring)
            times=0
            for m in range(0,len(answer)+1):
                for n in summ:
                    if n==m:
                        times+=1
                print(format(m,">2d"),times*"*")
                times = 0
    elif order=="e":
        print("Goodbye!")
        break
    elif order=="q":
        quizspilt=quizzes.split("\n")
        number_quiz=len(quizspilt)
        print("There are",number_quiz,"quizzes available")
        for q in quizspilt:
            quizsplit1=q.split(",")
            numquestion=len(quizsplit1[1])
            print(quizsplit1[0],"has",numquestion,"questions")
    else:
        print("Unknown command, please try again")
