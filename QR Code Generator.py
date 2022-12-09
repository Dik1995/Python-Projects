from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import qrcode
from resizeimage import resizeimage
import mysql.connector


def main():
    main_window = Tk()
    app = Login_System(main_window)
    main_window.mainloop()


####-------Login class----######
    
class Login_System():
    def __init__(self,root):
        self.root=root
        self.root.title("Login_System|Developed By Diksha")
        self.root.geometry("1400x900+0+0")
        self.root.config(bg="Black")
        

####-----------Images----#######
        
        self.phone_image=ImageTk.PhotoImage(file=r"C:\Users\USER\Desktop\image1/2.png")
        self.lb1_phone_image=Label(self.root,image=self.phone_image,bd=0,bg="white",fg="white").place(x=300,y=90)

####------Login Frame-1------###

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=690,y=90,width=360,height=480)

####------variables---------###
        
        self.username=StringVar()
        self.password=StringVar()
        self.cpassword_info=IntVar()


####----Register Window---####
     
##    def register_window(self):
##        self.new_window=Toplevel(self.root)
##        self.app=Register(self.new_window)
        
####---Title Login Page---###
        
        title=Label(login_frame,text="Login_System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

####----Username And Password Login Page----#######
        
        lb1_user=Label(login_frame,text="Username",font=("Andalus",15,"bold"),bg="white",fg="#767171").place(x=50,y=100)
        txt_username=Entry(login_frame,textvariable=self.username,font=("times",15),bg="#ECECEC").place(x=50,y=140,width=270)


        lb1_pass=Label(login_frame,text="Password",font=("Andalus",15,"bold"),bg="white",fg="#767171").place(x=50,y=200)
        txt_passw=Entry(login_frame,show="*",textvariable=self.password,font=("times",15),bg="#ECECEC").place(x=50,y=240,width=270)

        self.cmb_quest_info=StringVar()
        self.answer_info=StringVar()
        self.npass_info=IntVar()
        self.cpassword_info=IntVar()
        
###-----Login Button---#####

        lbtn=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)     
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times",15,"bold")).place(x=150,y=355)

###---Forget Password Button--###

        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_password_window,font=("times",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

  
####--Register Account Frame 2--#####
        
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=690,y=600,width=360,height=60)


        lb1_reg=Label(register_frame,text="Don't have an account ?",fon=("times",13),bg="white").place(x=60,y=17)

###---Sign Up Button----#####

        btn_signup=Button(register_frame,text="Sign Up",command=self.register_window,font=("times",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=220,y=15)
        

#####---Animation Images On Login Page--###        

        self.im1=ImageTk.PhotoImage(file=r"C:\Users\USER\Desktop\image1\im1.png")
        self.web2=ImageTk.PhotoImage(file=r"C:\Users\USER\Desktop\image1\web2.png")

        self.lb1_change_image=Label(self.root,bg="white")
        self.lb1_change_image.place(x=380,y=116,width=155,height=330)
        
        self.animate()
        
#####--Animate Call Function----#####


    def animate(self):
        self.im=self.im1
        self.im1=self.web2
        self.web2=self.im
        
        self.lb1_change_image.config(image=self.im)
        self.lb1_change_image.after(2000,self.animate)

##    def forget_password(self):
##        self.root2=Toplevel()
##        self.root2=root
##        self.root2.title("Forget Password")
##        self.root2.geometry("1400x900+0+0")
        
####-----Register Window-------#####
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
####-----Login Function-------#####
        
    def login(self):
        if self.username.get()=="" or self.password.get()=="":
             messagebox.showerror("Error","All Fields are required")
##        elif self.username.get()=="diksha@gmail.com" or self.password.get()=="123456":
##             messagebox.showinfo("Info",f"Welcome:{self.username.get()}\nYour Password:{self.password.get()}")
        else:
            conn = mysql.connector.connect(host='localhost' , user='root', password='root123',database="Register")
            cur =conn.cursor()
            cur.execute("Select * from Details where Email= %s and Password= %s",(self.username.get(),self.password.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and password")
            else:
                open_main=messagebox.showinfo("Yay","Login Successful")

                self.new_window_1= Toplevel(self.root)
                app =QR_Generator(self.new_window_1)
                      
                 
            conn.commit()
            conn.close()
             

####----Reset Password------#####
             
    def reset_pass(self):
        if self.npass_info.get()!= self.cpassword_info.get():
            messagebox.showerror("ERROR","NEW PASSWORD & CONFIRM NEW PASSWORD SHOULD BE SAME",parent=self.root2)
        elif self.cmb_quest_info=="" and self.answer_info.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE MANDATORY",parent=self.root2)
        elif self.npass_info.get=="" and  self.cpass_info.get=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE MANDATORY",parent=self.root2)
   
##        if self.cmb_quest_info.get()=="Select":
##            messagebox.showerror("Error","Select Security Question",parent=self.root2)
##        elif self.txt_answer_info.get()=="":
##            messagebox.showerror("Error","Please Enter The Answer",parent=self.root2)
##        elif self.txt_npass_info.get()=="":
##            messagebox.showerror("Error","Please Enter New Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host='localhost' , user='root', password='root123',database="Register")
            cur =conn.cursor()
            query=("Select * from Details where Email=%s and question=%s and answer=%s")
            values=(self.username.get(),self.cmb_quest_info.get(),self.answer_info.get())
            cur.execute(query,values)
            row=cur.fetchone()
            if row==None:
                   messagebox.showerror("Error","Please Enter the correct answer",parent=self.root2)
            else:
##                sql= "insert into Details ({}) values (%s)",(self.txt_npass_info.get())
                query = ("update Details set Password=%s where Email = %s")
                values=(self.npass_info.get(),self.username.get())
                cur.execute(query,values)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password Has Been Reset,Please Login with New Password",parent=self.root2)
                
                self.root2.destroy()
                
####-----Forget Password Window----#####
                
    def forget_password_window(self):
        if self.username.get()=="":
            messagebox.showerror("Error","Please Enter Email to Reset Password")
        else:
             conn = mysql.connector.connect(host='localhost' , user='root', password='root123',database="Register")
             cur =conn.cursor()
             query=("Select * from Details where Email=%s")
             values=(self.username.get(),)
             cur.execute(query,values)
             row=cur.fetchone()
             
             if row==None:
                 messagebox.showerror("Error","please Enter valid Username")
             else:
                 conn.close()
                 
                 self.root2=Toplevel()
                 self.root2.title("Forget Password")
                 self.root2.geometry("340x450+610+170")
                 self.root2.configure(background = "beige")
                 
                 
                 l=Label(self.root2,text="Forget Password",font=("times",20,"bold"),fg="red",bg="white")
                 l.place(x=0,y=10,relwidth=1)
                 
####-------------------------#########
                 
                 self.cmb_quest_info=StringVar()
                 self.answer_info=StringVar()
                 self.npass_info=IntVar()
                 self.cpass_info=IntVar()

                 question=Label(self.root2,text="Security Question",font=("times",15,"bold"),bg="white",fg="black").place(x=50,y=80)

                 
                 list1=["Select","your First Pet Name","Your Birth Place","Your Best Friend Name"]
                 self.cmb_quest=ttk.Combobox(self.root2,value=list1,textvariable = self.cmb_quest_info,font=("times",13),state="readonly",justify=CENTER)
                 self.cmb_quest.place(x=50,y=110,width=250)
                 self.cmb_quest.current(0)


                 anwser=Label(self.root2,text="Anwser",font=("times",15,"bold"),bg="white",fg="black").place(x=50,y=150)
                 self.answer=Entry(self.root2,text='',font=("times",15),bg="lightgray",textvariable=self.answer_info)
                 self.answer.place(x=50,y=180,width=250)
                 
####----New And Confirm Password Button-----########
                 
                 npass=Label(self.root2,text="New Password",font=("times",15,"bold"),bg="white",fg="black").place(x=50,y=220)
                 self.npass=Entry(self.root2,text='',font=("times",15),bg="lightgray",textvariable=self.npass_info)
                 self.npass.place(x=50,y=250,width=250)

                 cpass=Label(self.root2,text="Confirm Password",font=("times",15,"bold"),bg="white",fg="black").place(x=50,y=290)
                 self.npass=Entry(self.root2,text='',font=("times",15),bg="lightgray",textvariable=self.cpassword_info)
                 self.npass.place(x=50,y=320,width=250)

                 
#####---------Reset Button-----#####
                 
                 Rebtn=Button(self.root2,text="Reset",font=("times",15,"bold"),bg="green",fg="white",command=self.reset_pass)
                 Rebtn.place(x=100,y=380)

                
############------------#############
                 
##    def register_window(self):
##        self.root.destroy()
####        import register


## login ends


                 
#####----Register class----#####
             
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black")
        self.root.resizable(0,0)
        

#######------Backgroud Image----######
  
##        self.bg=ImageTk.PhotoImage
##        self.bg1_bg=Label(self.root,image=self.bg,bd=0,bg="white",fg="white").place(x=250,y=0,relwidth=1,height=1)
##
  
#####--Left Image-----##########
        
        self.left=ImageTk.PhotoImage(file=r"C:\Users\USER\Desktop\image1\web.png")
        left=Label(self.root,image=self.left).place(x=130,y=100,width=400,height=500)

#####---Register Frame--#############
        
        frame1=Frame(self.root,bg="White")
        frame1.place(x=530,y=100,width=700,height=500)
        
#######---------------######

        self.fname_info=StringVar()
        self.lname_info=StringVar()
        self.contact_info=IntVar()
        self.email_info=StringVar()
        self.cmb_quest_info=StringVar()
        self.answer_info=StringVar()
        self.password_info=IntVar()
        self.cpassword_info=IntVar()
        
#######------Register Title---------##########
        
        title=Label(frame1,text="REGISTER HERE",font=("times",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
#######------First And Last Name---------##########
        
        fname=Label(frame1,text="First Name",font=("times",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.fname=Entry(frame1,font=("times",15),bg="lightgray",textvariable=self.fname_info)
        self.fname.place(x=50,y=130,width=250)
        
        lname=Label(frame1,text="Last Name",font=("times",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.lname=Entry(frame1,font=("times",15),bg="lightgray",textvariable=self.lname_info)
        self.lname.place(x=370,y=130,width=250)
        
#######----Contact And Email-----------##########
        
        contact=Label(frame1,text="Contact No.",font=("times",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.contact=Entry(frame1,font=("times",15),bg="lightgray",textvariable=self.contact_info)
        self.contact.place(x=50,y=200,width=250)
                             
        email=Label(frame1,text="Email ID",font=("times",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.email=Entry(frame1,font=("times",15),bg="lightgray",textvariable=self.email_info)
        self.email.place(x=370,y=200,width=250)
                             
#######-----Security Question And Answer----------##########

        question=Label(frame1,text="Security Question",font=("times",15,"bold"),bg="white",fg="gray").place(x=50,y=240)

        list1=["Select","your First Pet Name","Your Birth Place","Your Best Friend Name"]
        self.cmb_quest=ttk.Combobox(frame1,value=list1,textvariable = self.cmb_quest_info,font=("times",13),state="readonly",justify=CENTER)
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        anwser=Label(frame1,text="Anwser",font=("times",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.answer=Entry(frame1,font=("times",15),bg="lightgray",textvariable=self.answer_info)
        self.answer.place(x=370,y=270,width=250)
                             
###------Password And Confirm Password---------##########

        password=Label(frame1,text="Password",font=("times",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.password=Entry(frame1,font=("times",15),bg="lightgray",textvariable=self.password_info)
        self.password.place(x=50,y=340,width=250)
                             
        cpassword=Label(frame1,text="Confirm Password",font=("times",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.cpassword=Entry(frame1,font=("times",15),bg="lightgray",textvariable=self.cpassword_info)
        self.cpassword.place(x=370,y=340,width=250)
                             
###------Check Button Terms---------##########
        
        self.var_chk=IntVar()                     
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times",12)).place(x=50,y=380)
        
######----Register Button----######
        
        Rbtn=Button(frame1,text="Register Now",command=self.register_data,font=("times",15),bg="green",fg="black",bd=0,cursor="hand2").place(x=50,y=420)                                                                                                

 ######----Sign Up Button----######
         
        btn_login=Button(frame1,text="Sign Up",command = return_login,font=("times",20),bg="green",fg="black",bd=0,cursor="hand2").place(x=100,y=560,width=150)

#####----Clear Function-----#########

    def clear(self):
        self.fname.delete(0,END)
        self.lname.delete(0,END)
        self.contact.delete(0,END)
        self.email.delete(0,END)
        self.answer.delete(0,END)
        self.password.delete(0,END)
        self.cpassword.delete(0,END)
        self.cmb_quest.current(0)
        
#####------------------#######

    def return_login () :
        self.root.destroy()

#####----Register Function Call-----####       
        
    def register_data(self):
        if self.fname_info.get()=="" or self.lname_info.get()=="" or self.contact_info.get()=="" or self.email_info.get()=="" or self.cmb_quest_info.get()=="Select" or self.answer_info.get()=="" or self.password_info.get()=="" or self.cpassword_info.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.password_info.get()!=self.cpassword_info.get():
            messagebox.showerror("Error","Password & Confirm Password Should be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & condition",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost' , user='root', password='root123',database="Register")
            cur =conn.cursor()
##            cur.execute("create database Register")
##            cur.execute("create table Details(Name varchar(50),last varchar(50),contact int,email varchar(50),question varchar(50),answer varchar(50),password varchar(50));")
            query=("Select * from Details where Email=%s")
            values=(self.email_info.get(),)
            cur.execute(query,values)
            row=cur.fetchone()
##            print(row)
            if row!=None:
                messagebox.showerror("Error","User Already Exist,Please try with another email",parent=self.root)
            else:
                cur.execute("insert into Details values('{}','{}','{}','{}','{}','{}','{}');".format
                                            ( self.fname_info.get(),
                                              self.lname_info.get(),
                                              self.contact_info.get(),
                                              self.email_info.get(),
                                              self.password_info.get(),
                                              self.cmb_quest_info.get(),
                                              self.answer_info.get()))

            
                conn.commit()
                conn.close()                       
                messagebox.showinfo("Success","Register Successful",parent=self.root)
                print ('fname : ', self.fname_info.get(), 'lname : ',self.lname_info.get(), 'contact : ',self.contact_info.get(), 'email : ',self.email_info.get(),'password : ',self.password_info.get(), ' question : ',self.cmb_quest_info.get(), 'answer : ',self.answer_info.get())
##                self.clear()
##            except Exception as es:
##                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=se
##
##    def return_login () :
                self.root.destroy()

####-----QR generator----##########

class QR_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("QR Generator | Developed By Diksha")
##        self.root.resizable(0,0)

        title=Label(self.root,text="                             QR Code Generator",font=("times 40"),bg="#053246",fg="white",anchor="w").place(x=0,y=0,relwidth=1)


#####--------------Employee Details Window --------#########
#####---------variables---------------######

        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()

        img4=Image.open(r"C:\Users\USER\Desktop\Employee_QR\QR_Generator\bg.png")
        img4=img4.resize((1350,700),Image.Resampling.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg4=Label(root,image=self.photoimage4,borderwidth=0)
        lblimg4.place(x=0,y=0,width=1350,height=700)
        
#####---Employee Frame--#############
        
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_Frame.place(x=50,y=100,width=500,height=380)

#####---Employee Title--#############
        
        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",20),bg="#053246",fg="white").place(x=0,y=0,relwidth=1)

#####---Employee Label--#############
        
        lb1_emp_code=Label(emp_Frame,text="Employee ID",font=("times ",15,"bold"),bg="white").place(x=20,y=60)
        lb1_emp_name=Label(emp_Frame,text="Name",font=("times ",15,"bold"),bg="white").place(x=20,y=100)
        lb1_department=Label(emp_Frame,text="Department",font=("times ",15,"bold"),bg="white").place(x=20,y=140)
        lb1_designation=Label(emp_Frame,text="Designation",font=("times ",15,"bold"),bg="white").place(x=20,y=180)

#####---Employee Entry--#############

        txt_emp_code=Entry(emp_Frame,text="",font=("times ",15),textvariable=self.var_emp_code,bg="lightyellow").place(x=200,y=60)
        txt_emp_name=Entry(emp_Frame,text="",font=("times ",15),textvariable=self.var_name,bg="lightyellow").place(x=200,y=100)
        txt_department=Entry(emp_Frame,text="",font=("times ",15),textvariable=self.var_department,bg="lightyellow").place(x=200,y=140)
        txt_designation=Entry(emp_Frame,text="",font=("times ",15),textvariable=self.var_designation,bg="lightyellow").place(x=200,y=180)

#####---Employee Button--#############

        btn_generate=Button(emp_Frame,text="QR Generate",command=self.generate,font=("times",18,"bold"),bg="#2196f3",fg="white").place(x=90,y=250,width=180,height=30)
        btn_clear=Button(emp_Frame,text="Clear",command=self.clear,font=("times",18,"bold"),bg="grey",fg="white").place(x=282,y=250,width=120,height=30)


        self.msg=""
        self.lb1_msg=Label(emp_Frame,text=self.msg,font=("times ",20),bg="white",fg="green")
        self.lb1_msg.place(x=0,y=310,relwidth=1)
        
#####Employee QR code window------------#########
        
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_Frame.place(x=600,y=100,width=250,height=380)

        emp_title=Label(qr_Frame,text="Employee QR Code",font=("goudy old style",20),bg="#053246",fg="white",bd=1,relief=RIDGE).place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text="No QR\nAvailable",font=("times",15),bg="#3f51b5",fg="white")
        self.qr_code.place(x=35,y=100,width=180,height=180)
        
        
####----Creating Function Generate ------#########
        
    def clear(self):
        self.var_emp_code.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_designation.set("")
        
        self.msg=""
        self.lb1_msg.config(text=self.msg)
        self.qr_code.config(image="")
        
    def generate(self):
        if self.var_emp_code.get()=="" or self.var_name.get()=="" or self.var_department.get()=="" or self.var_designation.get()=="":
            self.msg="All Fields Are Required"
            self.lb1_msg.config(text=self.msg,fg="red")
        else:
            qr_data=(f"Employee Id:{self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nDesignation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save(r"C:\Users\USER\Desktop\Employee_QR\QR_Generator\Employee_QR"+str(self.var_emp_code.get())+".png")

############----SQL Connectivity-----######
            
            conn = mysql.connector.connect(host='localhost' , user='root', password='root123',database="QR")
            cur =conn.cursor()
            cur.execute("insert into Employee2 values('{}','{}','{}','{}'); ".format(self.var_emp_code.get(),
                                                                                   self.var_name.get(),
                                                                                   self.var_department.get(),
                                                                                   self.var_designation.get()))
            conn.commit()
            conn.close()
            
######----QR code image update----#####
            
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            
####----Updating Notification----#####
            
            self.msg="QR Generated Successfully"
            self.lb1_msg.config(text=self.msg,fg="green")

conn = mysql.connector.connect(host='localhost' , user='root', password='root123',database="QR")
cur =conn.cursor()
##cur.execute("create database QR")
##cur.execute("create table Employee2( ID int, Name varchar(50), Department varchar(50), Designation varchar(50));")
cur.execute("insert into Employee2 values(1,'Diksha','IT','SE'); ")
conn.commit()
conn.close()
            

            
if __name__=="__main__":
    main()







