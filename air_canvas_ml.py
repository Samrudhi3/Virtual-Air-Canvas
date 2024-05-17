import cv2
import numpy as np
import mediapipe as mp
from collections import deque
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os
import credentials as cr
import pymysql
import os

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")
        
        self.bg_img = ImageTk.PhotoImage(file="Images/sample.jpeg")
        background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.window, bg="white")
        frame.place(x=350,y=100,width=500,height=550)

        title1 = Label(frame, text=" @ VIRTUAL AIR CANVAS", font=("times new roman",25,"bold"),bg="white").place(x=40, y=20)
        title2 = Label(frame, text="Sign up to activate account!", font=("times new roman",13),bg="white", fg="blue").place(x=40, y=75)

        f_name = Label(frame, text="First name", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Last name", font=("helvetica",15,"bold"),bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("helvetica",15,"bold"),bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        sec_question = Label(frame, text="Security questions", font=("helvetica",15,"bold"),bg="white").place(x=20, y=260)
        answer = Label(frame, text="Answer", font=("helvetica",15,"bold"),bg="white").place(x=240, y=260)

        self.questions = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
        self.questions.place(x=20,y=290,width=200)
        self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        password =  Label(frame, text="New password", font=("helvetica",15,"bold"),bg="white").place(x=20, y=340)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=370, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=20,y=420)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=470,width=250)

    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="Select" or self.answer_txt.get()=="" or self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                connection = pymysql.connect(host="localhost", user="user1", password="samu", database="student_database")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s",self.email_txt.get())
                row=cur.fetchone()

               
                if row!=None:
                    messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
                else:
                    cur.execute("insert into student_register (f_name,l_name,email,question,answer,password) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.fname_txt.get(),
                                        self.lname_txt.get(),
                                        self.email_txt.get(),
                                        self.questions.get(),
                                        self.answer_txt.get(),
                                        self.password_txt.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)

    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()



class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("Log In Canavs")
       
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

       

        self.frame1 = Frame(self.window, bg="yellow")
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        label1 = Label(self.frame1, text= "CA", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(x=80,y=300)
        label2 = Label(self.frame1, text= "NVAS", font=("times new roman", 40, "bold"), bg="yellow", fg="RoyalBlue1").place(x=162,y=300)
        label3 = Label(self.frame1, text= "All about Virtuality!", font=("times new roman", 13, "bold"), bg="yellow", fg="brown4").place(x=100,y=360)

        

        self.frame2 = Frame(self.window, bg = "gray95")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140,y=150,width=500,height=450)

        self.email_label = Label(self.frame3,text="Email Address", font=("helvetica",20,"bold"),bg="white", fg="black").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="black")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3,text="Password", font=("helvetica",20,"bold"),bg="white", fg="black").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="black",show="*")
        self.password_entry.place(x=50, y=160, width=300)

        
        self.login_button = Button(self.frame3,text="Log In",command=self.login_func,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=50,y=200,width=300)

        self.forgotten_pass = Button(self.frame3,text="Forgotten password?",command=self.forgot_func,font=("times new roman",10, "bold"),bd=0,cursor="hand2",bg="white",fg="blue").place(x=125,y=260,width=150)

        self.create_button = Button(self.frame3,text="Create New Account",command=self.redirect_window,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=80,y=320,width=250)


    def login_func(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host="localhost", user="user1", password="samu", database="student_database")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid USERNAME & PASSWORD",parent=self.window)
                else:
                    messagebox.showinfo("Success","Welcome to the Virtual Air Canvas family",parent=self.window)
                    # Clear all the entries
                    self.reset_fields()
                    
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def forgot_func(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Error!", "Please enter your Email Id",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host="localhost", user="user1", password="samu", database="student_database")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s", self.email_entry.get())
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Email Id doesn't exists")
                else:
                    connection.close()
                    
                    

                    self.root=Toplevel()
                    self.root.title("Forget Password?")
                    self.root.geometry("400x440+450+200")
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root,text="Change your password",font=("times new roman",20,"bold"),bg="white").place(x=10,y=10)

                    title4 = Label(self.root,text="It's quick and easy",font=("times new roman",12),bg="white").place(x=10,y=45)

                    title5 = Label(self.root, text="Select your question", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=85)

                    self.sec_ques = ttk.Combobox(self.root,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.sec_ques['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
                    self.sec_ques.place(x=10,y=120, width=270)
                    self.sec_ques.current(0)
                    
                    title6 = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=160)

                    self.ans = Entry(self.root,font=("arial"))
                    self.ans.place(x=10,y=195,width=270)

                    title7 = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=235)

                    self.new_pass = Entry(self.root,font=("arial"))
                    self.new_pass.place(x=10,y=270,width=270)

                    self.create_button = Button(self.root,text="Submit",command=self.change_pass,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=95,y=340,width=200)
                  

            except Exception as e:
                messagebox.showerror("Error", f"{e}")
                
      
    def change_pass(self):
        if self.email_entry.get() == "" or self.sec_ques.get() == "Select" or self.new_pass.get() == "":
            messagebox.showerror("Error!", "Please fill the all entry field correctly")
        else:
            try:
                connection = pymysql.connect(host="localhost", user="user1", password="samu", database="student_database")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s and question=%s and answer=%s", (self.email_entry.get(),self.sec_ques.get(),self.ans.get()))
                row=cur.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Please fill the all entry field correctly")
                else:
                    try:
                        cur.execute("update student_register set password=%s where email=%s", (self.new_pass.get(),self.email_entry.get()))
                        connection.commit()

                        messagebox.showinfo("Successful", "Password has changed successfully")
                        connection.close()
                        self.reset_fields()
                        self.root.destroy()

                    except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
                        
            except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
            

    def redirect_window(self):
        self.window.destroy()
        
       
        root = Tk()
        obj = SignUp(root)
        root.mainloop()

    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)

if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()

 
def setValues(x):
 print("")


bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]



blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

 
kernel = np.ones((5,5),np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0


paintWindow = np.zeros((471,636,3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40,1), (140,65), (0,0,0), 2)
paintWindow = cv2.rectangle(paintWindow, (160,1), (255,65), (255,0,0), 2)
paintWindow = cv2.rectangle(paintWindow, (275,1), (370,65), (0,255,0), 2)
paintWindow = cv2.rectangle(paintWindow, (390,1), (485,65), (0,0,255), 2)
paintWindow = cv2.rectangle(paintWindow, (505,1), (600,65), (0,255,255), 2)

cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
ret = True
while ret:
    
    ret, frame = cap.read()

    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame = cv2.rectangle(frame, (40,1), (140,65), (0,0,0), 2)
    frame = cv2.rectangle(frame, (160,1), (255,65), (255,0,0), 2)
    frame = cv2.rectangle(frame, (275,1), (370,65), (0,255,0), 2)
    frame = cv2.rectangle(frame, (390,1), (485,65), (0,0,255), 2)
    frame = cv2.rectangle(frame, (505,1), (600,65), (0,255,255), 2)
    cv2.putText(frame, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    

    
    result = hands.process(framergb)

    
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # # print(id, lm)
                # print(lm.x)
                # print(lm.y)
                lmx = int(lm.x * 640)
                lmy = int(lm.y * 480)

                landmarks.append([lmx, lmy])


            
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
        fore_finger = (landmarks[8][0],landmarks[8][1])
        center = fore_finger
        thumb = (landmarks[4][0],landmarks[4][1])
        cv2.circle(frame, center, 3, (0,255,0),-1)
        print(center[1]-thumb[1])
        if (thumb[1]-center[1]<30):
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1

        elif center[1] <= 65:
            if 40 <= center[0] <= 140: 
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0

                paintWindow[67:,:,:] = 255
            elif 160 <= center[0] <= 255:
                    colorIndex = 0 # Blue
            elif 275 <= center[0] <= 370:
                    colorIndex = 1 # Green
            elif 390 <= center[0] <= 485:
                    colorIndex = 2 # Red
            elif 505 <= center[0] <= 600:
                    colorIndex = 3 # Yellow
        else :
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(center)
    
    else:
        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1

    
    points = [bpoints, gpoints, rpoints, ypoints]
    # for j in range(len(points[0])):
    #         for k in range(1, len(points[0][j])):
    #             if points[0][j][k - 1] is None or points[0][j][k] is None:
    #                 continue
    #             cv2.line(paintWindow, points[0][j][k - 1], points[0][j][k], colors[0], 2)
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

    cv2.imshow("Output", frame) 
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
