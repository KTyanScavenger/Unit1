#Kyla Ryan
#9/17

def test_average(total):
    my_list=[]
    total_score=int(total)
    count=0
    while count != total_score:
        score = float(input("enter a score:"))
        my_list.append(score)
        count=count+1
                            
    b=sum(my_list)
    avg=b/total_score
    print("your avg is",avg)


t=input("enter total tests")
test_average(t)




def my_average():
    t1=int(input("test 1:"))
    t2=int(input("test 2:"))
    t3=int(input("test 3:"))
    t4=int(input("test 4:"))
    t5=int(input("test 5:"))
    t6=int(input("test 6:"))
    t7=int(input("test 7:"))
    t8=int(input("test 8:"))
    t9=int(input("test 9:"))
    t10=int(input("test 10:"))

    average_sum=(t1+t2+t3+t4+t5+t6+t7+t8+t9+t10)
    average_total=average_sum/10
    print(average_total)
my_average()
