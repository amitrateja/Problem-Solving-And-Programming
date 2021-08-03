import turtle
#student_marks={"Charan":9.5,"Mitra":5.4,"Teja":5.3, "Rahul":7.5, "Nithin":8.8, "Shreeya":7.8, "Sai":6.3,"Sai ch":6.2, "Adithya":7.2, "Kaushik":9.1}
#sorted_marks = sorted(student_marks.items(), key = lambda x: x[1],reverse = True)
#s=dict(sorted_marks)

#names=list(s.keys())
#marks=list(s.values())

import pandas as pd
s=pd.read_excel(r'studentmarks.xlsx')

import turtle


names=list(s['student'])
marks=list(s['marks'])


d_students={}
cls1_students={}
cls2_students={}
pass_students={}

for i in range(0,len(names)):
    if s['marks'][i]>=8.0:
        d_students[s['student'][i]]=marks[i]



for i in range(0,len(names)):
    if s['marks'][i]>=6.5 and s['marks'][i]<8.0:
        cls1_students[s['student'][i]]=marks[i]

for i in range(0,len(names)):
    if s['marks'][i]>=5.5 and s['marks'][i]<6.5:
        cls2_students[s['student'][i]]=marks[i]

for i in range(0,len(names)):
    if s['marks'][i]>=5.0 and s['marks'][i]<5.5:
        pass_students[s['student'][i]]=marks[i]
        
print(d_students)
print(cls1_students)
print(cls2_students)
print(pass_students)

maxmarks = max(marks)
num_stu = len(marks)    
border = 10

wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 40*num_stu+border, maxmarks+border)
wn.bgcolor("blue")

st = turtle.Turtle()
st.color("white")
st.fillcolor("navy")
st.pensize(3)
st.speed(0)



def drawbar(student, marks):
    student.begin_fill()
    student.left(90)               
    student.forward(marks)
    student.right(90)
    student.forward(15)
    student.write(str(marks),font=('Arial',13))
    student.forward(25)            
    student.right(90)
    student.forward(marks)        
    student.left(90)
    student.end_fill()

def names(s,name):
    s.forward(5)
    s.write(name,font=('Times New Roman',13))
    s.forward(35)

def draw_distinction():
    student=list(d_students.keys())
    marks=list(d_students.values())

    
    for i in marks:
        drawbar(st, i)
    
    st.goto(0,0)

    for j in student:
        names(st,j)

    st.penup()
    st.goto(0,-4)
    st.pendown()
    st.write('Distinction',font=('Times New Roman',20))
    st.penup()
    st.goto((len(student)*40)+3,0)
    st.pendown()

def draw_1stclass():
    student=list(cls1_students.keys())
    marks=list(cls1_students.values())

    
    
    for i in marks:
        drawbar(st, i)
    
    st.goto(len(student)*40,0)

    for j in student:
        names(st,j)

    st.penup()
    st.goto(len(student)*40,-4)
    st.pendown()
    st.write('1st Class',font=('Times New Roman',20))
    st.penup()
    st.goto(((len(student)*40)*2)+6,0)
    st.pendown()

def draw_2ndclass():
    student=list(cls2_students.keys())
    marks=list(cls2_students.values())

    
    
    for i in marks:
        drawbar(st, i)
    
    st.goto(((len(student)*40)*3)+6,0)

    for j in student:
        names(st,j)

    st.penup()
    st.goto(((len(student)*40)*3)+6,-4)
    st.pendown()
    st.write('2nd Class',font=('Times New Roman',20))
    st.penup()
    st.goto(((len(student)*40)*4)+9,0)
    st.pendown()

def draw_pass():
    student=list(pass_students.keys())
    marks=list(pass_students.values())

    
    
    for i in marks:
        drawbar(st, i)
    
    st.goto(((len(student)*40)*4)+9,0)

    for j in student:
        names(st,j)

    st.penup()
    st.goto(((len(student)*40)*4)+9,-4)
    st.pendown()
    st.write('Pass',font=('Times New Roman',20))
 
draw_distinction()

draw_1stclass()

draw_2ndclass()

draw_pass()

wn.exitonclick()