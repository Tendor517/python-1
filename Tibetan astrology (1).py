def fun():
    r=0
    r=input("1.Enter your name in(english/tibetan etc.)=")
    return r
while 1==1:
    you=fun()
    name=['Mouse','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep','Monkey','Bird','Dog','Pig']
    kham=['iron','iron','water','water','wind','wind','fire','fire','earth','earth']
    a=int(input("2.enter the your year of birth:"))
    tib={'Mouse':'བྱི་བ།','Ox':'གླང་།','Tiger':'སྟག།','Rabbit':'ཡོས།','Dragon':'འབྲུག།','Snake':'སྦྲུལ།','Horse':'རྟ།','Sheep':'ལུག།','Monkey':'སྤྲེལ།','Bird':'བྱ།','Dog':'ཁྱི།','Pig':'ཕག།'}
    tibk={'iron':'ལྕགས།','water':'ཆུ།','wind':'རླུང་།','fire':'མེ།','earth':'ས།'}
    luck={'Mouse':{'best day':'Wednesday','Good day':'Tuesday','Bad day':'Saturday'},'Ox':{'best day':'Saturday','Good day':'Wednesday','Bad day':'Friday'},
          'Tiger':{'best day':'Thursday','Good day':'Saturday','Bad day':'Friday'},'Rabbit':{'best day':'Thursday','Good day':'Saturday','Bad day':'Friday'},
          'Dragon':{'best day':'Sunday','Good day':'Wednesday','Bad day':'Thursday'},'Snake':{'best day':'Tuesday','Good day':'Friday','Bad day':'Wednesday'},
         'Horse':{'best day':'Tuesday','Good day':'Friday','Bad day':'Wednesday'},'Sheep':{'best day':'Friday','Good day':'Monday','Bad day':'Thursday'},
          'Sheep':{'best day':'Friday','Good day':'Monday','Bad day':'Thursday'},'Bird':{'best day':'Friday','Good day':'Thursday','Bad day':'Tuesday'},
          'Monkey':{'best day':'Friday','Good day':'Thursday','Bad day':'Tuesday'},'Dog':{'best day':'Monday','Good day':'Wednesday','Bad day':'Thursday'},
          'Pig':{'best day':'Wednesday','Good day':'Tuesday','Bad day':'Saturday'}}
    luckt={'Mouse':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},'Ox':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},
          'Tiger':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},'Rabbit':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},
          'Dragon':{'best day':'གཟའ་ཉི་མ།','Good day':'གཟའ་ལྷག་པ།','Bad day':'ཕུར་པོ།'},'Snake':{'best day':'མིག་དམར།','Good day':'པ་སངས།','Bad day':'ལྷག་པ།'},
         'Horse':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},'Sheep':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},
          'Sheep':{'best day':'པ་སངས།','Good day':'གཟའ་ཟླ་བ།','Bad day':'ཕུར་པོ།་'},'Bird':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},
          'Monkey':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},'Dog':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'},
          'Pig':{'best day':'བླ་གཟའ།','Good day':'སྲོག་གཟའ།','Bad day':'གཤེད་གཟའ།'}}
    count=0
    lortak=[]
    k=0
    for i in range(1900,a+1):
        if i==a:
            lortak=name[count]
            Kham=kham[k]
            break
        else:
            if count==11:
                count=0
            else:
                count+=1
        if 1==1:
            if k==9:
                k=0
            else:
                k+=1
        
    print("3.",you,"your lortak is=",lortak,'    རང་གི་ལོ་རྟགས་ནི་=',tib[lortak])
    print("4.Your kham is=",Kham,"  རང་གི་ཁམས་ནི་=",tibk[Kham])
    print("5.your best day is",luck[lortak]['best day'],"__your good day is=",luck[lortak]['Good day'],"__your Bad day is on=",luck[lortak]['Bad day'], "  རང་གི་བླ་གཟའ་ནི་=",luckt[lortak]['best day'],"__རང་གི་སྲོག་གཟའ་ནི་=་",luckt[lortak]['Good day'],"__རང་གི་གཤེད་གཟའ་ནི་=",luckt[lortak]['Bad day'])
    e=input("6.Want to try this again?; yes or no =")
    if e=="yes" or e=="Yes" or e=="YES":
        continue
    else:
        print("See you again, bye")
        break
   
        



    
    

