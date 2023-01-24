from tkinter import *
from batsman.pbl4_batsman import *
from PIL import Image,ImageTk,ImageSequence
from tkinter import ttk
import threading
import random
import pyttsx3


class cricket:
    def __init__(self):
        self.score=0
        self.overs=0.0
        self.wickets=0

    def tscore(self,input):
        self.score+=input
        cric2.bowler_runs(input)

    def over(self):
        self.overs+=0.1
        self.overs = round(self.overs, 1)
        print(self.overs)
        self.overs=str(self.overs)
        cric2.bowler_overs()
        #print(self.overs[0:3])
        if self.overs[2]=='6':
            #self.overs = float(self.overs)
            self.overs = round(float(self.overs)) + 0.0
            #print(self.overs)
        else:
            self.overs = float(self.overs)
       # if((self.overs*10) % 10 == 6):
            #self.overs=round(self.overs)+0.0
            #print(self.overs)
    def wicket(self):
       self.wickets+=1
       cric2.bowler_wicket()
       #print(str(self.score) + ' - '+str(self.wickets))

    def setForSecondInnings(self):
        self.score = 0
        self.overs = 0.0
        self.wickets = 0



engine = pyttsx3.init()
lock=threading.Lock()

t5=''
t2=''
t9=''

options=['INDIA','AUSTRALIA','NEW ZEALAND','SOUTH AFRICA','ENGLAND']
options1=options.copy()
INDIA=['ROHIT','KL RAHUL','VIRAT','KARTHIK','PANT','HARDIK','BUVI','BUMRAH','JADEJA','CHAHAL','SHAMI']
AUSTRALIA=['WARNER','FINCH','SMITH','MARSH','GREEN','MAXWEL','CUMMINS','STARC','HAZELWOOD','ZAMPA','RICHARDSAON']
NEWZ=['CONWAY','GUPTIL','WILLIAMSON','PHILLIPS','FINN ALLEN','MITCHELL','GRANDHOME','SOUTHEE','BOULT','TIM SODHI','SANTNER']
ENGLAND=['BUTTLER','ALEX HALES','MALAN','STOKES','BAIRSTOW','MOOEN ALI','WOAKES','ARCHER','RASHID','WOOD','ANDERSON']
options=['INDIA','AUSTRALIA','NEW ZEALAND','ENGLAND']

teams={options[0]:INDIA,options[1]:AUSTRALIA,options[2]:NEWZ,options[3]:ENGLAND}
options1=options.copy()

def main():
    global t1,t2
    lock.acquire()
    newroot2=Tk()
    newroot2.geometry("600x200")
    Grid.columnconfigure(newroot2, 0, weight=1)
    Grid.rowconfigure(newroot2, 0, weight=1)
    Grid.columnconfigure(newroot2, 1, weight=1)
    Grid.rowconfigure(newroot2, 1, weight=1)
    Grid.columnconfigure(newroot2,3,weight=1)
    Grid.rowconfigure(newroot2,3,weight=1)
    def getBatsman(x,y):
        global t1,t9
        t1= x.get()
        t9=y.get()
        buttonp = Button(newroot2, text="GO...", width=20, font=('calibri', 20, 'bold'), bg="cyan",command=newroot2.destroy)
        buttonp.grid(row=3, column=0, columnspan=2, sticky="nsew")



    label=Label(newroot2,text='BATTING TEAM',font=('calibri',20,'bold'),fg='red')
    label.grid(row=0,column=0)

    a=ttk.Combobox(newroot2,values=options,foreground='blue')
    a.grid(row=0,column=1,pady=10,padx=10,ipady=5,sticky="nsew")
    a.set("INDIA")

    options1.remove(a.get())
    label=Label(newroot2,text='BOWLING TEAM',font=('calibri',20,'bold'),fg='red')
    label.grid(row=1,column=0,sticky="nsew")
    b=ttk.Combobox(newroot2,values=options1,foreground='blue')
    b.grid(row=1,column=1,pady=10,padx=10,ipady=5,sticky="nsew")
    b.set('AUSTRALIA')
    buttonp=Button(newroot2,text="GO...",width=20,font=('calibri',20,'bold'),bg="cyan",command=lambda :getBatsman(a,b))
    buttonp.grid(row=3,column=0,columnspan=2,sticky="nsew")

    newroot2.mainloop()
    lock.release()

t3 = threading.Thread(target=main())
t3.start()
t3.join()

team_name_bowl=''


newroot=Tk()
newroot.geometry("500x300")
def check():
    global Overs_entry,forOvers,forStriker,forNonStriker,buttonx,striker_entry,nonStriker_entry,team_name
    forOvers=Overs_entry.get()
    forStriker=striker_entry.get()
    forNonStriker=nonStriker_entry.get()
    team_name=team_name_Entry.get()


    if forOvers!='' and forStriker!='' and forNonStriker!='' and team_name!='' :
        buttonx = Button(newroot, text="LET'S PLAY",width=20,font=('calibri',20,'bold'),bg="cyan", command=newroot.destroy)
        buttonx.grid(row=4, column=0,columnspan=2,pady=5,sticky='NSEW')
    else:
        buttonx = Button(newroot, text="LET'S PLAY",width=20,font=('calibri',20,'bold'),bg="cyan", command=check)
        buttonx.grid(row=4, column=0,columnspan=2,pady=5,sticky='NSEW')

oversSet=[2,3,5,10,20,50,90]
Overs=Label(newroot,text="OVERS :",font=('calibri',20,"bold"),fg="blue",relief='ridge',border=5).grid(row=0,column=0,pady=5)
# Overs_entry=Entry(newroot,font=('calibri',20,'bold'),relief='solid',border=2.5)
Overs_entry = Spinbox(newroot, values=oversSet,font=('calibri',20,'bold'),relief='solid',border=2.5,width=19)
Overs_entry.grid(row=0,column=1,pady=5,sticky="nsew")


striker = Label(newroot,text="STRIKER ",font=('calibri',20,'bold'),fg="blue",relief='sunken',border=5).grid(row=1,column=0,pady=5)
striker_entry=Entry(newroot,font=('calibri',20,'bold'),relief="solid",border=2.5)
striker_entry.grid(row=1,column=1,pady=5,sticky="nsew")

nonStriker =Label(newroot,text="NON STRIKER ",font=('calibri',20,'bold'),fg="blue",relief="sunken",border=5)
nonStriker.grid(row=2,column=0,pady=5,sticky="nsew")
nonStriker_entry=Entry(newroot,font=('calibri',20,'bold'),relief="solid",border=2.5)
nonStriker_entry.grid(row=2,column=1,pady=5,sticky="nsew")
team_name_Label=Label(newroot,text="team",font=('calibri',20,'bold'),fg="blue",relief="sunken",border=5)
team_name_Label.grid(row=3,column=0,pady=5,sticky="nsew")
# team_name_Entry=Entry(newroot,font=('calibri',20,'bold'),relief="solid",border=2.5)
# team_name_Entry.grid(row=3,column=1,pady=5)


team_name_Entry=ttk.Combobox(newroot,values=options,width=50,foreground='blue')
team_name_Entry.grid(row=3,column=1,pady=5,ipady=5,sticky="nsew")
team_name_Entry.set(t1)


forOvers=''
team_name=''
forStriker=''
forNonStriker=''

'''FIRST APPROACH'''
if t1 == options[0]:

    striker_entry.insert(0,teams[options[0]][0])
    nonStriker_entry.insert(0,teams[options[0]][1])
elif t1 == options[1]:
    striker_entry.insert(0, teams[options[1]][0])
    nonStriker_entry.insert(0, teams[options[1]][1])
elif  t1==options[2]:
    striker_entry.insert(0, teams[options[2]][0])
    nonStriker_entry.insert(0, teams[options[2]][1])
elif t1==options[3]:
    striker_entry.insert(0, teams[options[3]][0])
    nonStriker_entry.insert(0, teams[options[3]][1])
elif t1==options[4]:
    striker_entry.insert(0, teams[options[4]][0])
    nonStriker_entry.insert(0, teams[options[4]][1])
striker_entry['state']=DISABLED
nonStriker_entry['state']=DISABLED

'''SECOND APPROACH '''
# striker_entry.insert(0,teams[t1[0]][0])
# nonStriker_entry.insert(0,teams[options[0]][1])

buttonx=Button(newroot,text="LET'S PLAY",width=20,font=('calibri',20,'bold'),bg="cyan",command=check)
buttonx.grid(row=4,column=0,columnspan=2,sticky='NSEW')
newroot.mainloop()


print(forOvers,forStriker,forNonStriker,team_name)
cric1=batsman(forStriker,forNonStriker)   #here setting of striker and non striker intially from newroot widget
cric1.striker()  #this is for setting the srike to the striker
cric1.teams(team_name)

team_name_bowl=t9
cric2=Bowler(teams[team_name_bowl][7])
cric2.teams(team_name_bowl)

root=Tk()
root.title("cricbuzz")
root.geometry()
root.resizable(True,True)

def commands():
    pass

#adding menu's
mymenu=Menu(root)
root.config(menu=mymenu)


file_menu=Menu(mymenu)

mymenu.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label='NEW',command=commands)
file_menu.add_command(label='edit',command=commands)
file_menu.add_separator()

file_menu.add_command(label='view',command=commands)
file_menu.add_command(label='new project',command=commands)
file_menu.add_command(label='view',command=commands)
file_menu.add_separator()

file_menu=Menu(mymenu)

mymenu.add_cascade(label="SCORECARD",menu=file_menu)
file_menu.add_command(label='back',command=commands)
file_menu.add_command(label='search everywhere',command=commands)
file_menu.add_separator()
file_menu.add_command(label='<- previous',command=commands)
file_menu.add_command(label='select ...',command=commands)
file_menu.add_command(label='jump ....',command=commands)
file_menu.add_separator()

file_menu=Menu(mymenu)

mymenu.add_cascade(label="COMMENTRY",menu=file_menu)
file_menu.add_command(label='run ....',command=commands)
file_menu.add_command(label='debug ...',command=commands)
file_menu.add_separator()
file_menu.add_command(label='Attach to process',command=commands)
file_menu.add_command(label='select',command=commands)
file_menu.add_command(label='jump',command=commands)
file_menu.add_separator()


file_menu=Menu(mymenu)

mymenu.add_cascade(label="VIEW",menu=file_menu)
file_menu.add_command(label='details ....',command=commands)
file_menu.add_command(label='show ....',command=commands)

cric=cricket()


list1=[0,1,2,3,4,6]
x=float(forOvers)


y=''
inp_wide=0

# img=ImageTk.PhotoImage(Image.open(r"C:\Users\HOME\Desktop\1.jpg"))
img1=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\1.jpg").resize((65,65))
new_img=ImageTk.PhotoImage(img1)
img2=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\2.png").resize((65,65))
new_img2=ImageTk.PhotoImage(img2)
img3=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\3.png").resize((65,65))
new_img3=ImageTk.PhotoImage(img3)
img4=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\4.png").resize((65,65))
new_img4=ImageTk.PhotoImage(img4)
img6=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\6.png").resize((65,65))
new_img6=ImageTk.PhotoImage(img6)
imgw=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\w.png").resize((65,65))
new_imgw=ImageTk.PhotoImage(imgw)
img0=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\0.png").resize((70,70))
new_img0=ImageTk.PhotoImage(img0)
imgnb=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\nb.png").resize((65,65))
new_imgnb=ImageTk.PhotoImage(imgnb)
imgwd=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\wd.png").resize((65,65))
new_imgwd=ImageTk.PhotoImage(imgwd)


img_rohit=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\ROHIT.png").resize((75,75))
new_img_rohit=ImageTk.PhotoImage(img_rohit)
img_rahul=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\KL RAHUL.png").resize((75,75))
new_img_rahul=ImageTk.PhotoImage(img_rahul)
img2_virat=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\VIRAT.png").resize((75,75))
new_img2_virat=ImageTk.PhotoImage(img2_virat)
img_karthik=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\KARTHIK.png").resize((75,75))
new_img3_karthik=ImageTk.PhotoImage(img_karthik)
img_pant=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\PANT.png").resize((75,75))
new_img_pant=ImageTk.PhotoImage(img_pant)
img_hardik=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\HARDIK.png").resize((75,75))
new_img_hardik=ImageTk.PhotoImage(img_hardik)
img_jadeja=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\JADEJA.png").resize((75,75))
new_img_jadeja=ImageTk.PhotoImage(img_jadeja)
img6_bhuvi=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\BHUVI.png").resize((75,75))
new_img_bhuvi=ImageTk.PhotoImage(img6_bhuvi)
imgn_bumrah=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\BUMRAH.png").resize((75,75))
new_imgn_bumrah=ImageTk.PhotoImage(imgn_bumrah)
img_chahal=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\CHAHAL.png").resize((75,75))
new_imgw_chahal=ImageTk.PhotoImage(img_chahal)
imgw_shami=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\SHAMI.png").resize((75,75))
new_imgw_shami=ImageTk.PhotoImage(imgw_shami)
INDIA_IMAGES=[new_img_rohit,new_img_rahul,new_img2_virat,new_img3_karthik,new_img_pant,new_img_hardik,new_img_bhuvi,new_imgn_bumrah,new_img_jadeja,new_imgw_chahal,new_imgw_shami]
INDIA_IMAGES1=[new_img_hardik,new_img_bhuvi,new_imgn_bumrah,new_img_jadeja,new_imgw_chahal,new_imgw_shami]

img_conway=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\CONWAY.png").resize((75,75))
new_img_conway=ImageTk.PhotoImage(img_conway)
img_guptil=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\GUPTIL.png").resize((75,75))
new_img_guptil=ImageTk.PhotoImage(img_guptil)
img2_williamson=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\WILLIAMSON.png").resize((75,75))
new_img2_williamson=ImageTk.PhotoImage(img2_williamson)
img_phillips=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\PHILLIPS.png").resize((75,75))
new_img3_phillips=ImageTk.PhotoImage(img_phillips)
img_finn_allen=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\FINN ALLEN.png").resize((75,75))
new_img_finn_allen=ImageTk.PhotoImage(img_finn_allen)
img_mitchell=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\MITCHELL.png").resize((75,75))
new_img_mitchell=ImageTk.PhotoImage(img_mitchell)
img6_grandhome=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\GRANDHOME.png").resize((75,75))
new_img_grandhome=ImageTk.PhotoImage(img6_grandhome)
imgn_southee=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\SOUTHEE.png").resize((75,75))
new_imgn_southee=ImageTk.PhotoImage(imgn_southee)
img_boult=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\BOULT.png").resize((75,75))
new_imgw_boult=ImageTk.PhotoImage(img_boult)
imgw_tim_sodhi=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\TIM SODHI.png").resize((75,75))
new_imgw_tim_sodhi=ImageTk.PhotoImage(imgw_tim_sodhi)
imgw_santner=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\SANTNER.png").resize((75,75))
new_imgw_santner=ImageTk.PhotoImage(imgw_santner)
NEWZ_IMAGES=[new_img_conway,new_img_guptil,new_img2_williamson,new_img3_phillips,new_img_finn_allen,new_img_mitchell,new_img_grandhome,new_imgn_southee,new_imgw_boult,new_imgw_tim_sodhi,new_imgw_santner]
NEWZ_IMAGES1=[new_img_mitchell,new_img_grandhome,new_imgn_southee,new_imgw_boult,new_imgw_tim_sodhi,new_imgw_santner]

img_buttler=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\Buttler.png").resize((75,75))
new_img_buttler=ImageTk.PhotoImage(img_buttler)
img_hales=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\ALEX HALES.png").resize((75,75))
new_img_hales=ImageTk.PhotoImage(img_hales)
img2_malan=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\MALAN.png").resize((75,75))
new_img2_malan=ImageTk.PhotoImage(img2_malan)
img_stokes=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\STOKES.png").resize((75,75))
new_img3_stokes=ImageTk.PhotoImage(img_stokes)
img_mooean=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\MOOEAN ALI.png").resize((75,75))
img_bairstow=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\BAIRSTOW.png").resize((75,75))
new_img_bairstow=ImageTk.PhotoImage(img_bairstow)
new_img_mooean=ImageTk.PhotoImage(img_mooean)
img_woakes=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\WOAKES.png").resize((75,75))
new_img_woakes=ImageTk.PhotoImage(img_woakes)
img6_archer=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\ARCHER.png").resize((75,75))
new_img_archer=ImageTk.PhotoImage(img6_archer)
imgn_rashid=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\RASHID.png").resize((75,75))
new_imgn_rashid=ImageTk.PhotoImage(imgn_rashid)
img_wood=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\WOOD.png").resize((75,75))
new_imgw_wood=ImageTk.PhotoImage(img_wood)
imgw_anderson=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\ANDERSON.png").resize((75,75))
new_imgw_anderson=ImageTk.PhotoImage(imgw_anderson)
ENGLAND_IMAGES=[new_img_buttler,new_img_hales,new_img2_malan,new_img3_stokes,new_img_bairstow,new_img_mooean,new_img_woakes,new_img_archer,new_imgn_rashid,new_imgw_wood,new_imgw_anderson]
ENGLAND_IMAGES1=[new_img_mooean,new_img_woakes,new_img_archer,new_imgn_rashid,new_imgw_wood,new_imgw_anderson]

img_warner=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\WARNER.png").resize((75,75))
new_img_warner=ImageTk.PhotoImage(img_warner)
img_finch=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\FINCH.png").resize((75,75))
new_img_finch=ImageTk.PhotoImage(img_finch)
img2_smith=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\SMITH.png").resize((75,75))
new_img2_smith=ImageTk.PhotoImage(img2_smith)
img_marsh=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\MARSH.png").resize((75,75))
new_img3_marsh=ImageTk.PhotoImage(img_marsh)
img_green=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\GREEN.png").resize((75,75))
new_img3_green=ImageTk.PhotoImage(img_green)
img2_maxwel=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\MAXWEL.png").resize((75,75))
new_img2_maxwel=ImageTk.PhotoImage(img2_maxwel)
img_cummins=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\CUMMINS.png").resize((75,75))
new_img_cummins=ImageTk.PhotoImage(img_cummins)
img_starc=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\STARC.png").resize((75,75))
new_img_starc=ImageTk.PhotoImage(img_starc)

img_hazelwood=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\HAZELWOOD.png").resize((75,75))
new_img3_hazelwood=ImageTk.PhotoImage(img_hazelwood)
img_zampa=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\ZAMPA.png").resize((75,75))
new_img_zampa=ImageTk.PhotoImage(img_zampa)
img_richardson=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\RICHARDSAON.png").resize((75,75))
new_img_richardson=ImageTk.PhotoImage(img_richardson)

AUSTRALIA_IMAGES=[new_img2_maxwel,new_img_cummins,new_img_starc,new_img3_hazelwood,new_img_zampa,new_img_richardson]
AUSTRALIA_IMAGES1=[new_img_warner,new_img_finch,new_img2_smith,new_img3_marsh,new_img3_green,new_img2_maxwel,new_img_cummins,new_img_starc,new_img3_hazelwood,new_img_zampa,new_img_richardson]

def forWides():

    newroot1=Tk()
    newroot1.geometry("500x500")
    newroot1['bg']='red'

    def set_wide(inp):
        global button0, button3, button4, button6, button2, button1, new_img0, new_img6, new_img4, new_img3, new_img2, new_img
        global inp_wide
        lock.acquire()
        inp_wide=inp
        button1 = Button(newroot1, text='1', padx=10, pady=10,width=5, fg="blue", command=newroot1.quit).grid(row=1,column=0,pady=2,ipadx=10,sticky="nsew")
        button2 = Button(newroot1, text='2', padx=10, pady=10,width=5,  fg="blue", command=newroot1.quit).grid(row=1,column=1,pady=2,ipadx=10,sticky="nsew")
        button3 = Button(newroot1, text='3', padx=10, pady=10,width=5,  fg="blue", command=newroot1.quit).grid(row=1,column=2,pady=2,ipadx=10,sticky="nsew")
        button4 = Button(newroot1, text='4', padx=10, pady=10,width=5,  fg="blue", command=newroot1.quit).grid(row=2,column=0,pady=1,ipadx=10,sticky="nsew")
        button6 = Button(newroot1, text='6', padx=10, pady=10,width=5,  fg="blue", command=newroot1.quit).grid(row=2,column=1,pady=1,ipadx=10,sticky="nsew")
        button0 = Button(newroot1, text='0', padx=10, pady=10,width=5,  fg="blue", command=newroot1.quit).grid(row=2,column=2,pady=1,ipadx=10,sticky="nsew")
        lock.release()


    button1 = Button(newroot1, text='1', padx=10, pady=10,width=5,  fg="blue", command=lambda: set_wide(1)).grid(row=1, column=0, pady=2, ipadx=10,sticky="nsew")
    button2 = Button(newroot1, text='2', padx=10, pady=10,width=5,  fg="blue",command=lambda: set_wide(2)).grid(row=1, column=1, pady=2, ipadx=10,sticky="nsew")
    button3 = Button(newroot1, text='3', padx=10, pady=10,width=5,  fg="blue",command=lambda: set_wide(3)).grid(row=1, column=2, pady=2, ipadx=10,sticky="nsew")
    button4 = Button(newroot1, text='4', padx=10, pady=10,width=5,  fg="blue",command=lambda: set_wide(4)).grid(row=2, column=0, pady=1, ipadx=10,sticky="nsew")
    button6 = Button(newroot1, text='6', padx=10, pady=10,width=5,  fg="blue", command=lambda: set_wide(6)).grid(row=2, column=1, pady=1, ipadx=10,sticky="nsew")
    button0 = Button(newroot1, text='0', padx=10, pady=10,width=5,  fg="blue",command=lambda: set_wide(0)).grid(row=2, column=2, pady=1, ipadx=10,sticky="nsew")

    row_number=0
    col_number=0
    buttons=[button0,button3,button4,button6,button2,button1]
    for i in buttons:
        Grid.rowconfigure(newroot1,row_number,weight=1)
        Grid.rowconfigure(newroot1, row_number, weight=1)
        Grid.rowconfigure(newroot1, row_number, weight=1)
        Grid.columnconfigure(newroot1,0, weight=1)
        Grid.columnconfigure(newroot1,1, weight=1)
        Grid.columnconfigure(newroot1,2, weight=1)
        row_number+=1


    newroot1.mainloop()

    # return bowler_name

def bowler_names(*bowlersSet):
    global bowler_name
    newroot1=Tk()
    newroot1.geometry("300x300")
    def getBowler():
        global bowler_name,indexForBowler,bowlersSet
        lock.acquire()


        namess=entry1.get()
        indexForBowler=bowlersSet.index(namess)

        bowler_name=namess
        if namess != '':
            button_bowler1 = Button(newroot1, text="saveBowler",font=('calibri',10,'bold'),fg="blue",relief='sunken',border=5, command=newroot1.quit)
            button_bowler1.grid(row=2, column=0,sticky="nsew")

            lock.release()
        else:
            button_bowler1 = Button(newroot1, text="saveBowler", font=('calibri', 10, 'bold'), fg="blue",relief='sunken', border=5, command=getBowler)
            button_bowler1.grid(row=2, column=0,sticky="nsew")



    # bowlersSet=[teams[t9][5],teams[t9][6],teams[t9][7],teams[t9][8],teams[t9][9],teams[t9][10]]
    label=Label(newroot1,text="ENTER NEXT BOWLER",font=('calibri',20,'bold'),relief="sunken",border=5,fg='red')
    label.grid(row=0,column=0,sticky="nsew")
    entry1=Spinbox(newroot1,values=bowlersSet,font=('calibri',20,'bold'),relief="solid",border=2.5)
    entry1.grid(row=1,column=0,sticky="nsew")
    button_bowler=Button(newroot1,text="saveBowler",font=('calibri',10,'bold'),fg="blue",relief='sunken',border=5,command=getBowler)
    button_bowler.grid(row=2,column=0,sticky="nsew")

    namess=''
    newroot1.mainloop()
    return bowler_name

bowlersSet=[teams[t9][5],teams[t9][6],teams[t9][7],teams[t9][8],teams[t9][9],teams[t9][10]]

def switchInnings():
    global team_name,t9,team_name_set,entries,ball_count,i,entry,label2,label,label100,bowlersSet,firstInningsScore,firstInningsWickets,chasingLabel,innings
    team_name_set.configure(text=t9)
    firstInningsScore=cric.score
    firstInningsWickets=cric.wickets
    
    cric.setForSecondInnings()

    '''CREATE LABEL FOR CHASING SCORE '''


    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',200)
    engine.say("first innings completed ")

    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    engine.say(f"{cric.score} for {cric.wickets}")
    engine.runAndWait()

    for i in range(0, len(entries)):
        entries[i]['bg'] = 'white'
        entries[i].after(50, entries[i].delete(0, END))
    i = -1
    ball_count = 1


    '''CREATE LABEL FOR CHASING SCORE '''
    innings=2
    chasingLabel.configure(text=""+str(firstInningsScore)+" needed in "+str(int(x*6)),fg='red',font=('calibri',15,'italic'))

    batsman1.delete(0, END)
    batsman2.delete(0, END)
    bowler.delete(0,END)

    cric1.teams(team_name_bowl)
    cric2.teams(team_name)
    cric2.bowling(teams[team_name][7])

    bowlersSet = [teams[team_name][5], teams[team_name][6], teams[team_name][7], teams[team_name][8], teams[team_name][9], teams[team_name][10]]

    if team_name == options[0]:
        label2.configure(image=INDIA_IMAGES1[2])
        bowler.insert(0,teams[team_name][7])

    elif team_name == options[1]:
        label2.configure(image=AUSTRALIA_IMAGES[2])
        bowler.insert(0,teams[team_name][7])


    elif team_name == options[2]:
        label2.configure(image=NEWZ_IMAGES1[2])
        bowler.insert(0,teams[team_name][7])

    elif team_name == options[3]:
        label2.configure(image=ENGLAND_IMAGES1[2])
        bowler.insert(0,teams[team_name][7])


    if team_name_bowl == options[0]:
        label.configure(image=INDIA_IMAGES[0])
        label100.configure(image=INDIA_IMAGES[1])

    elif team_name_bowl == options[1]:
        label.configure(image=AUSTRALIA_IMAGES1[0])
        label100.configure(image=AUSTRALIA_IMAGES1[1])

    elif team_name_bowl == options[2]:
        label.configure(image=NEWZ_IMAGES[0])
        label100.configure(image=NEWZ_IMAGES[1])

    elif team_name_bowl == options[3]:
        label.configure(image=ENGLAND_IMAGES[0])
        label100.configure(image=ENGLAND_IMAGES[1])


    entry.delete(0,END)
    entry.insert(0, "0 - 0" + '  (0.0/' + str(x) + ')')

    cric1.setBatsman(teams[team_name_bowl][0],teams[team_name_bowl][1])



    if team_name_bowl == options[0]:
        batsman1.insert(0, INDIA[0] + "            0(0)")
        batsman2.insert(0, INDIA[1] + "            0(0)")
        # cric1.setBatsman(INDIA[0],INDIA[1])
    elif team_name_bowl == options[1]:
        batsman1.insert(0, AUSTRALIA[0] + "            0(0)")
        batsman2.insert(0, AUSTRALIA[1] + "            0(0)")
        # cric1.setBatsman(AUSTRALIA[0], AUSTRALIA[1] )
    elif team_name_bowl == options[2]:
        batsman1.insert(0, NEWZ[0] + "            0(0)")
        batsman2.insert(0, NEWZ[1] + "            0(0)")
        # cric1.setBatsman( NEWZ[0],  NEWZ[1])
    elif team_name_bowl == options[3]:
        batsman1.insert(0, ENGLAND[0] + "            0(0)")
        batsman2.insert(0, ENGLAND[1]  + "            0(0)")

        # cric1.setBatsman(ENGLAND[0],  ENGLAND[1] )



firstInningsScore=cric.score
firstInningsWickets=cric.wickets
chasingLabel=Label(root,text="First Innings",fg="red",font=('calibri',20,"bold"))
chasingLabel.grid(row=0,column=3,columnspan=12)
innings=1
totalballscount=int(x*6)

def scoring(inp):
    
    global i,ball_count,label100,label,label2,totalballscount
    global entries,names
    i+=1
    if innings==2 and cric.score <= firstInningsScore and cric.wickets!=10:
        buttonChangeInnings['state']=DISABLED
    # elif innings==2 and cric.wickets and cric.score >= firstInningsScore or innings==2 and  cric.wickets==10:


    if ball_count <=6 :

        if inp != 'wicket' and cric.wickets <10:
            cric1.batting(inp)

        else:
            # cric1.batting(inp)
            '''IMPORTANT LINE'''

            if cric.wickets <9 :
                t2=threading.Thread(target=cric1.change_batsman(teams[cric1.team][cric.wickets+2]))
                t2.start()
                t2.join()
            else:
                # cric.over()
                cric.wicket()
                batsman1.delete(0,END)
                label.grid_forget()
                # else:
                batsman2.delete(0,END)
                label100.grid_forget()


        '''TO CHANGE STRING TO VARAIABLE'''

        batsman1.delete(0, END)
        batsman2.delete(0, END)
        batsman1.insert(0, cric1.b1+"            "+str(cric1.b1_runs)+"("+str(cric1.b1_count)+")")
        batsman2.insert(0, cric1.b2+"            "+str(cric1.b2_runs)+"("+str(cric1.b2_count)+")")
        if ball_count == 6 and cric.wickets <10:
            if inp==2 or inp==4 or inp==6 or inp == 0 or inp=='wicket':
                cric1.batting("last ball"+str(inp))
                batsman1.delete(0, END)
                batsman2.delete(0, END)
                batsman1.insert(0, cric1.b1 + "            " + str(cric1.b1_runs) + "(" + str(cric1.b1_count) + ")")
                batsman2.insert(0, cric1.b2 + "            " + str(cric1.b2_runs) + "(" + str(cric1.b2_count) + ")")
            elif inp==1 or inp==3 :
                cric1.batting("last ball"+str(inp))
                batsman1.delete(0, END)
                batsman2.delete(0, END)
                batsman1.insert(0, cric1.b1 + "            " + str(cric1.b1_runs) + "(" + str(cric1.b1_count) + ")")
                batsman2.insert(0, cric1.b2 + "            " + str(cric1.b2_runs) + "(" + str(cric1.b2_count) + ")")

    if cric.overs !=x and cric.wickets <= 10:
        if inp=='wide':
            
            
            
            if i <= 5 or ball_count <= 6:


                t6=threading.Thread(target=forWides)
                t6.start()
                t6.join()
                inp1=inp_wide
                cric.tscore(inp1+1)

                entries[i].insert(0, str(inp1)+"WD")
                if innings==2 :
                    chasingLabel.configure(text=""+str(firstInningsScore - cric.score)+" in "+str(totalballscount),fg='red',font=('calibri',15,'italic'))

            else:
                for i in range(0,len(entries)):
                    entries[i]['bg']='white'
                    entries[i].after(50,entries[i].delete(0,END))
                i=-1
                ball_count=1
                
                if innings==2 :
                    chasingLabel.configure(text=""+str(firstInningsScore - cric.score)+" in "+str(totalballscount),fg='red',font=('calibri',15,'italic'))

                t8 = threading.Thread(target=bowler_names)
                t8.start()
                t8.join()
                cric2.bowling(bowler_name)

                # label2.configure(image=AUSTRALIA_IMAGES[indexForBowler])
                if cric2.team == options[0]:
                    label2.configure(image=INDIA_IMAGES1[indexForBowler])
                elif cric2.team == options[1]:
                    label2.configure(image=AUSTRALIA_IMAGES[indexForBowler])
                elif cric2.team == options[2]:
                    label2.configure(image=NEWZ_IMAGES1[indexForBowler])

                elif cric2.team == options[3]:
                    label2.configure(image=ENGLAND_IMAGES1[indexForBowler])

                bowler.delete(0, END)
                bowler.insert(0,cric2.name.upper() + " " + str(cric2.b_wicket) + " - " + str(cric2.b_runs) + " (" + str(cric2.b_overs) + ")")

            engine=pyttsx3.init()
            rate=engine.getProperty('rate')
            engine.setProperty('rate',200)
            engine.say("wide ball wide")
            engine.runAndWait()

        elif inp=='noball' and cric.wickets <10 :

            if i <= 5 or ball_count <= 6:
                t6 = threading.Thread(target=forWides)
                t6.start()
                t6.join()
                inp1 = inp_wide


                cric.tscore(inp1+1)
                entries[i].insert(0, str(inp1) + "NB")

                # if inp1 == 1 or inp1 == 3 :
                #     print("striker changes")
                cric1.NoBall_batting(inp1)
                batsman1.delete(0, END)
                batsman2.delete(0, END)
                batsman1.insert(0, cric1.b1 + "            " + str(cric1.b1_runs) + "(" + str(cric1.b1_count) + ")")
                batsman2.insert(0, cric1.b2 + "            " + str(cric1.b2_runs) + "(" + str(cric1.b2_count) + ")")

                if innings==2:
                    chasingLabel.configure(text=""+str(firstInningsScore - cric.score)+" in "+str(totalballscount),fg='red',font=('calibri',15,'italic'))
            else:
                for i in range(0,len(entries)):
                    entries[i]['bg']='white'
                    entries[i].after(50,entries[i].delete(0,END))
                i=-1
                ball_count=1

                t8 = threading.Thread(target=bowler_names)
                t8.start()
                t8.join()
                cric2.bowling(bowler_name)

                # label2.configure(image=AUSTRALIA_IMAGES[indexForBowler])
                if cric2.team == options[0]:
                    label2.configure(image=INDIA_IMAGES1[indexForBowler])
                elif cric2.team == options[1]:
                    label2.configure(image=AUSTRALIA_IMAGES[indexForBowler])
                elif cric2.team == options[2]:
                    label2.configure(image=NEWZ_IMAGES1[indexForBowler])

                elif cric2.team == options[3]:
                    label2.configure(image=ENGLAND_IMAGES1[indexForBowler])

                bowler.delete(0, END)
                bowler.insert(0,cric2.name.upper() + " " + str(cric2.b_wicket) + " - " + str(cric2.b_runs) + " (" + str(cric2.b_overs) + ")")

            engine=pyttsx3.init()
            rate=engine.getProperty('rate')
            engine.setProperty('rate',135)
            engine.say("bowler goes over the line umpires calls noball ")
            engine.runAndWait()    

        elif inp=='wicket':
            if innings==2:
                totalballscount-=1
                chasingLabel.configure(text=""+str(firstInningsScore - cric.score)+" in "+str(totalballscount),fg='red',font=('calibri',15,'italic'))

            if i <= 5 or ball_count <= 6:
                cric.over()
                ball_count+=1
                #i =i+1
                entries[i].insert(0, "w")
                entries[i]['bg']="red"
                if cric1.team==options[0] and cric.wickets <9:
                    if cric1.check==0:
                        label.configure(image=INDIA_IMAGES[cric.wickets+2])
                    else:
                        label100.configure(image=INDIA_IMAGES[cric.wickets+2])
                elif cric1.team==options[1] and cric.wickets <9:
                    if cric1.check == 0:
                        label.configure(image=AUSTRALIA_IMAGES1[cric.wickets + 2])
                    else:
                        label100.configure(image=AUSTRALIA_IMAGES1[cric.wickets + 2])
                elif cric1.team==options[2] and cric.wickets <9:
                    if cric1.check == 0 and cric.wickets <9:
                        label.configure(image=NEWZ_IMAGES[cric.wickets + 2])
                    else:
                        label100.configure(image=NEWZ_IMAGES[cric.wickets + 2])
                elif cric1.team ==options[3] and cric.wickets <9:
                    if cric1.check == 0:
                        label.configure(image=ENGLAND_IMAGES[cric.wickets + 2])
                    else:
                        label100.configure(image=ENGLAND_IMAGES[cric.wickets + 2])

                if cric.wickets !=10 :
                    cric.wicket()
                    

            else:
                for i in range(0,len(entries)):
                    entries[i]['bg']='white'
                    entries[i].after(50,entries[i].delete(0,END))
                i=-1
                ball_count=1
                t8 = threading.Thread(target=bowler_names)
                t8.start()
                t8.join()
                cric2.bowling(bowler_name)

                # label2.configure(image=AUSTRALIA_IMAGES[indexForBowler])
                if cric2.team == options[0]:
                    label2.configure(image=INDIA_IMAGES1[indexForBowler])
                elif cric2.team == options[1]:
                    label2.configure(image=AUSTRALIA_IMAGES[indexForBowler])
                elif cric2.team == options[2]:
                    label2.configure(image=NEWZ_IMAGES1[indexForBowler])

                elif cric2.team == options[3]:
                    label2.configure(image=ENGLAND_IMAGES1[indexForBowler])

                bowler.delete(0, END)
                bowler.insert(0,cric2.name.upper() + " " + str(cric2.b_wicket) + " - " + str(cric2.b_runs) + " (" + str(cric2.b_overs) + ")")
            engine=pyttsx3.init()
            rate=engine.getProperty('rate')
            engine.setProperty('rate',125)
            engine.say("wickets flies over that's out  ")
            engine.runAndWait()    

        elif inp in list1:
            if innings==2:
                totalballscount-=1
                chasingLabel.configure(text=""+str(firstInningsScore - (cric.score+inp))+" needed in "+str(totalballscount),fg='red',font=('calibri',15,'italic'))
                
            if i <= 5 or ball_count <=6:
                cric.tscore(int(inp))
                #entries[i]['state'] = "normal"
                cric.over()
                entries[i].insert(0,inp)
                if inp==6:
                    entries[i]['bg']='green'

                if inp==4:
                    entries[i]['bg']='blue'
                ball_count+=1

                if inp !=0:
                    engine=pyttsx3.init()
                    rate=engine.getProperty('rate')
                    engine.setProperty('rate',200)
                    engine.say(f"goes for {inp}")
                    engine.runAndWait()
                else:
                    engine=pyttsx3.init()
                    rate=engine.getProperty('rate')
                    engine.setProperty('rate',200)
                    engine.say("dot ball dot")
                    engine.runAndWait()
            else:
                engine=pyttsx3.init()
                rate=engine.getProperty('rate')
                engine.setProperty('rate',200)
                engine.say("over completed ")
                engine.setProperty('rate',100)
                voices=engine.getProperty("voices")
                engine.setProperty("voice",voices[1].id)
                engine.say(f"{cric.score} for {cric.wickets}")
                engine.runAndWait()


                for i in range(0,len(entries)):
                    entries[i]['bg']='white'
                    entries[i].after(50,entries[i].delete(0,END))
                i=-1
                ball_count=1

                
                #here need to change the bowler
                '''TRYING TO THE BOWLERR NAME'''

                '''END OF TAKING NAME'''
                t8=threading.Thread(target=bowler_names,args=bowlersSet)
                t8.start()
                t8.join()
                engine=pyttsx3.init()
                rate=engine.getProperty('rate')
                engine.setProperty('rate',150)
                

                voices=engine.getProperty("voices")
                engine.setProperty("voice",voices[1].id)
                engine.say(f"{bowler_name} comes into attack now")
                engine.runAndWait()
                cric2.bowling(bowler_name)

                # label2.configure(image=AUSTRALIA_IMAGES[indexForBowler])
                if cric2.team== options[0]:
                    label2.configure(image=INDIA_IMAGES1[indexForBowler])
                elif cric2.team == options[1]:
                    label2.configure(image=AUSTRALIA_IMAGES[indexForBowler])
                elif cric2.team == options[2]:
                    label2.configure(image=NEWZ_IMAGES1[indexForBowler])

                elif cric2.team == options[3]:
                    label2.configure(image=ENGLAND_IMAGES1[indexForBowler])


                bowler.delete(0,END)
                bowler.insert(0,cric2.name.upper()+" "+str(cric2.b_wicket)+" - "+str(cric2.b_runs)+" ("+str(cric2.b_overs)+")")

        bowler.delete(0, END)
        bowler.insert(0, cric2.name.upper() + "      " + str(cric2.b_wicket) + " - " + str(cric2.b_runs) + " (" + str(cric2.b_overs) + ")")

        #label=Label(root,text=str(cric.score) + ' - ' + str(cric.wickets)).grid(row=3,column=0)
        entry.delete(0,END)
        y=str(cric.overs)
        entry.insert(0,str(cric.score) + ' - ' + str(cric.wickets) +'   ('+y[0:3]+'/'+str(int(x))+')')

    else:
        buttonChangeInnings['state']=ACTIVE





'''FOR ENTERING THE BATSMAN NAME'''

bowler_name = ''
indexForBowler=1
buttonb=''

'''TEAM NAME  SETTING'''

team_name_set=Label(root,text=team_name,font=('calibri',25,'bold'),fg="blue",relief="sunken",border=5)
team_name_set.grid(row=0,column=0,sticky="nsew")
entry=Entry(root,width=12,borderwidth=5,fg="red",font=('calibri',30,'bold'),relief='solid')
#entry=Entry(root,width=30,borderwidth=10,fg="red",show="*")
entry.insert(0,"0 - 0"+'  (0.0/'+str(x)+')')
entry.grid(row=0,column=1,columnspan=3,padx=0,sticky="nsew")

'''CREATING BATSMAN FRAME'''

batsman_Frame=LabelFrame(root,text='batsman')
batsman_Frame.grid(row=4,column=0,columnspan=4,pady=15,sticky="nsew")
batsman1=Entry(batsman_Frame,width=30,font=('calibri',25,'bold'))
batsman1.grid(row=0,column=1,pady=10)
batsman2=Entry(batsman_Frame,width=30,font=('calibri',25,'bold'))
batsman2.grid(row=1,column=1,pady=10)
batsman1.insert(0,cric1.b1 + "            0(0)")
batsman2.insert(0,cric1.b2 + "            0(0)")

'''IMAGES OF BATSMAN'''
if team_name == options[0]:
    label = Label(batsman_Frame, image=INDIA_IMAGES[0])
    label.grid(row=0, column=0)
    label100 = Label(batsman_Frame, image=INDIA_IMAGES[1])
    label100.grid(row=1, column=0)
elif team_name == options[1]:
    label = Label(batsman_Frame, image=AUSTRALIA_IMAGES1[0])
    label.grid(row=0, column=0)
    label100 = Label(batsman_Frame, image=AUSTRALIA_IMAGES1[1])
    label100.grid(row=1, column=0)
elif team_name == options[2]:
    label = Label(batsman_Frame, image=NEWZ_IMAGES[0])
    label.grid(row=0, column=0)
    label100 = Label(batsman_Frame, image=NEWZ_IMAGES[1])
    label100.grid(row=1, column=0)
elif team_name == options[3]:
    label = Label(batsman_Frame, image=ENGLAND_IMAGES[0])
    label.grid(row=0, column=0)
    label100 = Label(batsman_Frame, image=ENGLAND_IMAGES[1])
    label100.grid(row=1, column=0)



#creating a frame for bowler
bowler_Frame=LabelFrame(root,text='bowler')
bowler_Frame.grid(row=5,column=0,columnspan=4,sticky="nsew")
# label2=Label(bowler_Frame,image=new_img_starc)
# label2.grid(row=0,column=0)
if t9==options[0]:
    label2 = Label(bowler_Frame, image=INDIA_IMAGES1[2])
    label2.grid(row=0, column=0)
elif t9==options[1]:
    label2=Label(bowler_Frame,image=AUSTRALIA_IMAGES[2])
    label2.grid(row=0,column=0)
elif t9==options[2]:
    label2=Label(bowler_Frame,image=NEWZ_IMAGES1[2])
    label2.grid(row=0,column=0)
elif t9==options[3]:
    label2=Label(bowler_Frame,image=ENGLAND_IMAGES1[2])
    label2.grid(row=0,column=0)

bowler=Entry(bowler_Frame,width=30,font=('calibri',25,'bold'))
bowler.grid(row=0,column=1)
bowler.insert(0,cric2.b_list[0])


innings_Frame=LabelFrame(root,text="second innings")
innings_Frame.grid(row=5,column=4,columnspan=12)
buttonChangeInnings =Button(innings_Frame,text="change innings",padx=10,pady=10,fg="red",font=('calibri',15,'bold'),state=DISABLED,command=switchInnings)
buttonChangeInnings.grid(row=0,column=0,pady=1,padx=10,ipadx=0,sticky="nsew")
'''active these button when the allout or total overs completed '''

#entries for tracking the every ball score
e1=Entry(root, width=5,font=('calibri',15,'italic'))
e1.grid(row=1, column=4)
e2=Entry(root, width=5,font=('calibri',15,'italic'))
e2.grid(row=1, column=5)
e3=Entry(root, width=5,font=('calibri',15,'italic'))
e3.grid(row=1, column=6)
e4=Entry(root, width=5,font=('calibri',15,'italic'))
e4.grid(row=1, column=7)
e5=Entry(root, width=5,font=('calibri',15,'italic'))
e5.grid(row=1, column=8)
e6=Entry(root, width=5,font=('calibri',15,'italic'))
e6.grid(row=1, column=9)
e7=Entry(root, width=5,font=('calibri',15,'italic'))
e7.grid(row=1, column=10)
e8=Entry(root, width=5,font=('calibri',15,'italic'))
e8.grid(row=1, column=11)
e9=Entry(root, width=5,font=('calibri',15,'italic'))
e9.grid(row=1, column=12)
e10=Entry(root, width=5,font=('calibri',15,'italic'))
e10.grid(row=1, column=13)
e11=Entry(root, width=5,state='disabled',font=('calibri',15,'italic'))
e11.grid(row=1, column=14)
e12=Entry(root, width=5,state=DISABLED,font=('calibri',15,'italic'))
e12.grid(row=1, column=15)


entries=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
i=-1
ball_count=1

# img=ImageTk.PhotoImage(Image.open(r"C:\Users\HOME\Desktop\1.jpg"))



button1=Button(root,image=new_img,padx=10,pady=10,fg="blue",border="0",command=lambda :scoring(1)).grid(row=1,column=0,pady=2,ipadx=10,sticky="nsew")
button2=Button(root,image=new_img2,padx=10,pady=10,fg="blue",border="0",command=lambda :scoring(2)).grid(row=1,column=1,pady=2,ipadx=10,sticky="nsew")
button3=Button(root,image=new_img3,padx=10,pady=10,fg="blue",border="0",command=lambda :scoring(3)).grid(row=1,column=2,pady=2,ipadx=10,sticky="nsew")
button4=Button(root,image=new_img4,padx=10,pady=10,fg="blue",border="0",command=lambda :scoring(4)).grid(row=2,column=0,pady=1,ipadx=10,sticky="nsew")
button6=Button(root,image=new_img6,padx=10,pady=10,fg="blue",border="0",command=lambda :scoring(6)).grid(row=2,column=1,pady=1,ipadx=10,sticky="nsew")
button0=Button(root,image=new_img0,padx=10,pady=10,fg="blue",border="0",command=lambda :scoring(0)).grid(row=2,column=2,pady=1,ipadx=10,sticky="nsew")
buttonWide=Button(root,image=new_imgwd,border="0",padx=5,pady=10,fg="blue",command=lambda :scoring("wide")).grid(row=3,column=0,pady=1,ipadx=10,sticky="nsew")
buttonNb=Button(root,image=new_imgnb,padx=10,pady=10,fg="blue",border="0",command=lambda :scoring("noball")).grid(row=3,column=1,pady=1,ipadx=5,sticky="nsew")
buttonW=Button(root,image=new_imgw,padx=10,pady=10,fg="blue",border="0",command=lambda :scoring("wicket")).grid(row=3,column=2,pady=1,ipadx=0,sticky="nsew")





print(cric1.b1)
print(cric1.b2)

'''TEAM IMAGE SETTINGS'''
img_bcci=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\bcci.png").resize((200,200))
new_img_bcci=ImageTk.PhotoImage(img_bcci)
img_aus=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\australia.png").resize((200,200))
new_img_aus=ImageTk.PhotoImage(img_aus)
img_kiwi=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\kiwis.png").resize((200,200))
new_img_kiwi=ImageTk.PhotoImage(img_kiwi)
img_eng=Image.open(r"C:\Users\HOME\Desktop\cric\IMAGES\england.png").resize((200,200))
new_img_eng=ImageTk.PhotoImage(img_eng)

teamFrame=LabelFrame(root,text="new match")
teamFrame.grid(row=4,column=4,padx=7,columnspan=12)

if team_name == options[0] :
    labelt1=Label(teamFrame,image=new_img_bcci)
    labelt1.grid(row=0,column=0)
elif team_name ==options[1]:
    labelt1 = Label(teamFrame, image=new_img_aus)
    labelt1.grid(row=0, column=0)
elif team_name==options[2]:
    labelt1 = Label(teamFrame, image=new_img_kiwi)
    labelt1.grid(row=0, column=0)
elif team_name==options[3]:
    labelt1 = Label(teamFrame, image=new_img_eng)
    labelt1.grid(row=0, column=0)

if team_name_bowl == options[0] :
    labelt2=Label(teamFrame,image=new_img_bcci)
    labelt2.grid(row=0,column=2)
elif team_name_bowl ==options[1]:
    labelt2 = Label(teamFrame, image=new_img_aus)
    labelt2.grid(row=0,column=2)
elif team_name_bowl==options[2]:
    labelt2 = Label(teamFrame, image=new_img_kiwi)
    labelt2.grid(row=0,column=2)
elif team_name_bowl==options[3]:
    labelt2 = Label(teamFrame, image=new_img_eng)
    labelt2.grid(row=0,column=2)

label_vs=Label(teamFrame,text="vs",font=('calibri',70,'italic'))
label_vs.grid(row=0,column=1)

rate=engine.getProperty('rate')
engine.setProperty('rate',200)
engine.say(f"{team_name} versus {team_name_bowl}")
engine.runAndWait()


root.mainloop()