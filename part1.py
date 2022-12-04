#Part 1

print("Computer Science Registration System")
course_name=input("Enter a course ID (i.e. CS0002, CS0004): ")
# see if the course exists
file_object=open("class_data.txt", "r")
alldata=file_object.read()
file_object.close()
# open up the enrollment file for reading
fp = open("enrollment_data.txt", "r")
enrollment_data=fp.read()
fp.close()
lines=alldata.split("\n")
# visit each line in the list
course_time=0
for line in lines:
    items=line.split(",")
    if items[0]==course_name:
        course_time+=1
        print ("The name of this course is:", items[1])
        student_lines=enrollment_data.split("\n")
        student=0
        name_list=""
        for stline in student_lines:
            items1=stline.split(",")
            if items[0]==course_name:
                student+=1
                name_list+="* "+items1[1]+","+items1[2]+"\n"
        print("The course has",str(student),"students enrolled")
        print(name_list)
        break
if course_time==0:
    print("Cannot find this course")
