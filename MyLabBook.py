#!/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import matplotlib.backends.backend_tkagg as tkagg
import tkinter.ttk as ttk
from PIL import Image
import pandas as pd

# Workspace  ---------------------------------------------------------------------
class Workspace:
    
    # Select file to open -------------------------------------------------------
    def newImage(self):
        self.filename=''
        global file
        global errorValueRead

        file = tk.filedialog.askopenfile(filetypes=[("JPG Files", "*.jpg"),("PNG Files", "*.png")])

        if file != None:
            self.filename = file.name
        else:
            errorValueRead = 1
            

        icon = Image.open(self.filename)
        self.IDlabel = ttk.Label(self.imageFrame,image=icon)
        self.IDlabel.image = icon
        self.IDlabel.grid(row=0,column=0,sticky='NSEW',padx=5, pady=5)
    
    def saveExp(self,title):
        # open a file to write to
        writeFile = open('%s.mlb'%(title),'a');
        print("I am doing it!")
        writeFile.write("\n%s~\n,%s~\n"%(self.methodText.get("1.0",tk.END),self.notesText.get("1.0",tk.END)));
        writeFile.close
    
    def __init__(self,master):
        self.s = ttk.Style()
        self.s.configure('TLabel', foreground='Black', background='white')
        self.s.configure('TButton', foreground='black', background='white')
        self.s.configure('TEntry', foreground='Blue')
        self.s.configure('TCheckbutton', foreground='black', background='white')
        self.s.configure('TMenubutton', background='white', foreground='black', width=25)
        self.s.configure('TLabelframe', foreground='black', background='white')
        self.s.configure('TFrame', background='white')
        
        # Window properties -----------------------------------------------------
        self.master = master
        master.wm_title("MyLabBook")
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # -----------------------------------------------------------------------
        # Frames ----------------------------------------------------------------
        
        self.frame1 = tk.LabelFrame(master, text="Setup", background='white')
        self.imageFrame=tk.Frame(self.frame1,background='white')
        self.frame2 = tk.LabelFrame(master, text="Plan & Method", background='white')
        self.frame3 = tk.LabelFrame(master, text="Notes", background='white')
        self.frame4 = tk.LabelFrame(master, text="Data", background='white')
        self.frame5 = tk.LabelFrame(master,width=40,text="Graphs", background='white')
        # Frame grid positions --------------------------------------------------

        #self.frame0.grid(row=0, columnspan=3, sticky='N')

        self.frame1.grid(row=0, column=0, sticky='NW',padx=5, pady=5)
        self.imageFrame.grid(row=0, column=0, sticky='NSEW',padx=5, pady=5)

        self.frame2.grid(row=1,column=0,sticky='NW',padx=5, pady=5)
        
        self.frame3.grid(row=0, column=1, sticky='NW',padx=5, pady=5)
        self.frame4.grid(row=1, column=1, sticky='NW',padx=5, pady=5)
        self.frame5.grid(row=0, column=2,sticky='NW',padx=5, pady=5)

        # -----------------------------------------------------------------------
        # Frame 1 widgets  ------------------------------------------------------
        self.addImage=ttk.Button(self.frame1, text=" Add Image ",command=self.newImage,width=10)
        # -----------------------------------------------------------------------

        # Frame 1 widgets positions  --------------------------------------------
        self.addImage.grid(row=1, column=5, sticky='E')
        # -----------------------------------------------------------------------
        # Frame 2 widgets  ------------------------------------------------------
        self.methodText = tk.Text(self.frame2, borderwidth=3, relief="sunken",width=40,height=15)
        self.methodText.config(font=("arial", 12), undo=True, wrap='word')
        self.scrollbarMethod = tk.Scrollbar(self.frame2, command=self.methodText.yview)
        self.methodText['yscrollcommand'] = self.scrollbarMethod.set
        
        # -----------------------------------------------------------------------

        # Frame 2 widgets positions  --------------------------------------------
        self.methodText.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.scrollbarMethod.grid(row=0, column=1, sticky='nsew')
        
        # -----------------------------------------------------------------------
        # Frame 3 widgets  ------------------------------------------------------
        self.notesText = tk.Text(self.frame3, borderwidth=3, relief="sunken",width=40,height=23)
        self.notesText.config(font=("arial", 12), undo=True, wrap='word')
        self.scrollbarNotes = tk.Scrollbar(self.frame3, command=self.notesText.yview)
        self.notesText['yscrollcommand'] = self.scrollbarNotes.set
        
        # -----------------------------------------------------------------------

        # Frame 3 widgets positions  --------------------------------------------
        self.notesText.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.scrollbarNotes.grid(row=0, column=1, sticky='nsew')
        # -----------------------------------------------------------------------
        # Frame 4 widgets  ------------------------------------------------------
        dates = pd.date_range('20160101', periods=6)
        df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
        #self.dataText = tk.Text(self.frame4, borderwidth=3, relief="sunken",width=40,height=15)
        #self.dataText.config(font=("arial", 12), undo=True, wrap='word')
        #self.scrollbarData = tk.Scrollbar(self.frame4, command=self.dataText.yview)
        #self.dataText.insert(tk.END,df)
        #self.dataText['yscrollcommand'] = self.scrollbarData.set
        height = 5
        width = 5
        for i in range(height): #Rows
            for j in range(width): #Columns
                b = tk.Entry(self.frame4, text="hi",width=int(40/width))
                b.grid(row=i, column=j,sticky='nsew')
        
        # -----------------------------------------------------------------------

        # Frame 4 widgets positions  --------------------------------------------
        #self.dataText.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        #self.scrollbarData.grid(row=0, column=1, sticky='nsew')
        
        # -----------------------------------------------------------------------
        # Frame 5 widgets  ------------------------------------------------------
        f = plt.Figure(figsize=(5,4))
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.dataPlot = tkagg.FigureCanvasTkAgg(f,master=self.frame5)
        # -----------------------------------------------------------------------

        # Frame 5 widgets positions  --------------------------------------------
        self.dataPlot.show()
        self.dataPlot.get_tk_widget().grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

# Main Menu ---------------------------------------------------------------------
class MainMenu:
    # Select file to open -------------------------------------------------------
    def openfile(self):
        global filename
        global file
        global errorValueRead

        file = tk.filedialog.askopenfile(filetypes=[("MyLabBook Files", "*.mlb")])

        if file != None:
            filename = file.name
            return filename
        else:
            errorValueRead = 1
        self.previousExperimentDirEntry.configure(state='normal')
        self.previousExperimentDirEntry.insert(0,filename)


    # Select file to open -------------------------------------------------------
    def saveExperiment(self):
        # open a file to write to
        global expTitle
        expTitle=self.expTitleEntry.get()
        writeFile = open('%s.mlb'%(self.expTitleEntry.get()),'w');
        writeFile.write("%s,%s,%s"%(self.expTitleEntry.get(),self.labDaysLengthEntry.get(),self.collaboratorsEntry.get()));
        writeFile.close
    
    def resetMainMenu(self):
        self.expTitleEntry.delete(0,len(self.expTitleEntry.get()))
        self.labDaysLengthEntry.delete(0,len(self.labDaysLengthEntry.get()))
        self.collaboratorsEntry.delete(0,len(self.collaboratorsEntry.get()))
        
    # Close the application -----------------------------------------------------
    def destroy(self):
        self.master.quit()
        self.master.destroy()

    # Close the application -----------------------------------------------------
    def switchToWorkspace(self):
        self.destroy()
        workspace=tk.Tk()
        secondaryApp=Workspace(workspace)
        secondaryApp.master.configure(background='white')
        menubar = tk.Menu(workspace)
        
        filemenu = tk.Menu(menubar,tearoff=0)
        
        # add commands to menu
        filemenu.add_command(label="New File")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save",command=lambda: secondaryApp.saveExp(expTitle))
        menubar.add_cascade(label="File", menu=filemenu)
        workspace.config(menu=menubar)  
        workspace.mainloop()



    def __init__(self,master):

        # Graphical User Interface ----------------------------------------------
        
        # Graphical User Interface ----------------------------------------------

        self.s = ttk.Style()
        self.s.configure('TLabel', foreground='Black', background='white')
        self.s.configure('TButton', foreground='black', background='white')
        self.s.configure('TEntry', foreground='Blue')
        self.s.configure('TCheckbutton', foreground='black', background='white')
        self.s.configure('TMenubutton', background='white', foreground='black', width=25)
        self.s.configure('TLabelframe', foreground='black', background='white')
        self.s.configure('TFrame', background='white')

        # Window properties -----------------------------------------------------
        self.master = master
        master.wm_title("MyLabBook")
        master.resizable(0,0)
        # -----------------------------------------------------------------------
        # Frames ----------------------------------------------------------------

        #self.frame0 = tk.Frame(master,bg='white')
        
        self.frame1 = tk.LabelFrame(master, text="New Experiment", background='white')
        self.buttonFrame1= tk.Frame(self.frame1, background='white')
        
        self.frame2 = tk.LabelFrame(master, text="Load Experiment", background='white')
        
        # Frame grid positions ---------------------------------        

        #self.frame0.grid(row=0, columnspan=3, sticky='N')

        self.frame1.grid(row=0, columnspan=1, sticky='E',padx=5, pady=5)

        self.buttonFrame1.grid(row=0, rowspan=3, column=3,ipadx=5, ipady=5)

        self.frame2.grid(row=1,columnspan=2,  sticky='EW',
                         padx=5, pady=5,ipadx=5,ipady=5)
        
        # -----------------------------------------------------------------------

        # Frame 0 widgets  ------------------------------------------------------

        #self.about = ttk.Label(self.frame0, text="MyLabBook")
        #self.about.grid(row=0, column=2,sticky='N')

        # -----------------------------------------------------------------------
        # Frame 1 widgets  ------------------------------------------------------
        self.expTitleLabel = ttk.Label(self.frame1, text="Name : ")
        self.labDaysLengthLabel = ttk.Label(self.frame1, text="Length(Days) : ")
        self.collaboratorsLabel = ttk.Label(self.frame1, text="Collaborators : ")
        
        self.expTitleEntry = ttk.Entry(self.frame1)
        self.labDaysLengthEntry = ttk.Entry(self.frame1)
        self.collaboratorsEntry = ttk.Entry(self.frame1)

        self.expTitleEntry.insert(0, string='Experiment 1')
        self.labDaysLengthEntry.insert(0, string='3')
        self.collaboratorsEntry.insert(0, string='A.B and C.D')

        # -----------------------------------------------------------------------

        # Frame 1 widgets positions  --------------------------------------------

        self.expTitleLabel.grid(row=0, column=0, sticky='E')
        self.expTitleEntry.grid(row=0, column=1, sticky='W')

        self.labDaysLengthLabel.grid(row=1, column=0, sticky='E')
        self.labDaysLengthEntry.grid(row=1, column=1, sticky='W')

        self.collaboratorsLabel.grid(row=2, column=0, sticky='E')
        self.collaboratorsEntry.grid(row=2, column=1, sticky='W')

        # -----------------------------------------------------------------------

        #ButtonFrame1 widgets  ------------------------------------------------------
        self.exit = ttk.Button(self.buttonFrame1, text=" Exit ", command=self.destroy,width=4)
        self.reset = ttk.Button(self.buttonFrame1, text=" Reset ",command=self.resetMainMenu,width=4)
        self.save = ttk.Button(self.buttonFrame1, text=" Save ",command=self.saveExperiment,width=4)
        
        #ButtonFrame1 widgets positions  --------------------------------------------

        self.exit.grid(row=0, column=0, sticky='EW',
                       padx=30, pady=5, ipadx=5, ipady=5)

        self.reset.grid(row=1, column=0, sticky='EW',
                       padx=30, pady=5, ipadx=5, ipady=5)

        self.save.grid(row=2, column=0, sticky='EW',
                       padx=30, pady=5, ipadx=5, ipady=5)
        # -----------------------------------------------------------------------

        #Frame2 widgets  ------------------------------------------------------
        
        self.previousExperimentDirLabel= ttk.Label(self.frame2, text="Directory of Experiment: ")
        self.previousExperimentDirEntry= ttk.Entry(self.frame2,state='disabled')
        self.opendir = ttk.Button(self.frame2, text="Open",command=self.openfile,width=4)
        self.sendToWorkspace=ttk.Button(self.frame2, text="To Workspace...",command=self.switchToWorkspace,width=12)
        
        #Frame2 widgets positions  --------------------------------------------
        self.previousExperimentDirLabel.grid(row=0, column=0, sticky='E')
        self.previousExperimentDirEntry.grid(row=0, column=1, sticky='W')
        self.opendir.grid(row=0, column=2, sticky='EW',padx=7)
        self.sendToWorkspace.grid(row=0, column=3, sticky='EW',padx=7)
        

mainM = tk.Tk()
"""
# Code to add widgets will go here...
for i in range(len(figures)):
    frame = tk.Frame(top)
    frame.grid(row=0, column=i, sticky="ns")
    #frame.pack()
    canvas = tkagg.FigureCanvasTkAgg(figures[i], frame)
    canvas.show()
    canvas.get_tk_widget().pack(fill='both', expand=True)
    toolbar = tkagg.NavigationToolbar2TkAgg(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(fill='both', expand=True)
"""
app=MainMenu(mainM)
app.master.configure(background='white')


mainM.mainloop()





        