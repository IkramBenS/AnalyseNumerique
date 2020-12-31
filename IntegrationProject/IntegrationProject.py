#**********************************************IMPORTATION***************************************************
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter import*
import sys
from tkinter import *
import tkinter.font as font
from tkinter import messagebox as msg
import tkinter as tk
from tkinter import ttk
from scipy.integrate import quad 

#**********************************************M. RECTANGLE***************************************************
class Rectangle(object):
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f=f
        self.n=n
    def integrate(self,f):
        x=self.x# contiens les xi
        y=f(x)#les yi
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        return h*s
    def Graph(self,f,resolution=1001):
        #fig = plt.figure(figsize=(7, 5.5))
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0 ,yl[i], yl[i] ,0 ,0 ]# ordonnees des sommets
            plt.plot(x_rect, y_rect,"r")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)
        plt.plot(xl, yl,"bo")
        plt.title('Methode des rectangles')
        #plt.set_xlabel('x')
        #plt.set_ylabel('F(x)')
        #plt.text(0.5*(self.a+self.b), f(self.b), '$I_{%s}$ =%12.4f' % (self.n,self.integrate(f)), fontsize=15) 
#**********************************************M. TRAPEZE***************************************************
class Trapezoidal(object):
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
            plt.plot(x_rect, y_rect,"r")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)#plot de f(x)
        plt.plot(xl, yl,"cs")#point support
        plt.ylabel ( ' f ( x ) ' )
        plt.title('Methode des Trapézes, N = {}'.format(self.n))

#**********************************************M. Simpson***************************************************
class Simpson ( object ) :
    def __init__ (self , a , b , n , f ) :
        self.a = a
        self.b = b
        self.x = np.linspace( a , b , n+1 )
        self.f = f
        self.n = n   
    def integrate ( self , f ) :
        x = self.x
        y=f(x)
        h=float(x[1]-x[0])
        n=len(x)-1
        if n%2==1:
            n-=1
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        return h*s/3.0
    def Graph ( self , f , resolution=1001 ) :
        fig = plt.figure(figsize=(7, 5.5))
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace( self.a , self.b , resolution )
        for i in range ( self.n ) :
            xx=np.linspace(xl[i],xl[i+1],resolution)
            m=(xl[i]+xl[i+1])/2
            aa=xl[i]
            bb=xl[i+1]
            l0=(xx-m)/(aa-m)*(xx-bb)/(aa-bb)
            l1=(xx-aa)/(m-aa)*(xx-bb)/(m-bb)
            l2=(xx-aa)/(bb-aa)*(xx-m)/(bb-m)
            P=f(aa)*l0+f(m)*l1+f(bb)*l2
            fig.plot(xx,P,'b')
            fig.plot(m,f(m),"r*")
    
        yflist_fine = f(xlist_fine)
        fig.plot(xlist_fine, yflist_fine,'g')
        fig.plot(xl, yl, "bo")
        fig.set_xlabel('x')
        fig.set_ylabel('f(x)')
        fig.set_title ( ' Méthode de Simpson' )
        fig.text( 0.5*( self.a+ self.b ) , f(self.b ) , '$I_{%s}$ =%4.4f'.format(self.n,self.integrate( f ) ) , fontsize =15 )
#**********************************************M. POIT MILIEU***************************************************
class Milieu(object):
    def __init_(self, a, b, n, f):
        self.a = a
        self.b = b
        self.n=n
        self.x = np.linspace(a, b, self.n+1)
        self.f=f
    def integrate(self,f):
        x=self.x
        h = float(x[1] - x[0])
        yml=[]
        for i in range(self.n):
            lm=(x[i]+x[i+1])*0.5
            lym=f(lm)
            yml.append(lym)
        s = sum(yml)
        return h*s
    def Graph(self,f, resolution=1001):
        fig = plt.figure(figsize=(7, 5.5))
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace( self.a , self.b , resolution )
        for i in range ( self.n ) :
            mi=(xl[i]+xl[i+1])/2
            x_rect = [xl[ i ] , xl[ i ] , xl[ i + 1 ] , xl[i+1] , xl[ i ] ] # abscisses des sommets
            y_rect = [0 , f(mi) , f(mi) , 0 , 0 ] # ordonnees des sommets
            fig.plot ( x_rect , y_rect , 'r' )
            fig.plot(mi,f(mi),'b*')
        yflist_fine=f(xlist_fine)
        fig.plot (xlist_fine,yflist_fine )
        fig.set_xlabel ( 'x' )
        fig.set_ylabel ( 'f(x)' )
        fig.set_title ( ' Méthode des points milieux' )
        fig.text( 0.5*( self.a+ self.b ) , f(self.b ) , '$I_{%s}$ =%12.4f' % (self.n,self.integrate(f)),fontsize =15 )
#**********************************************mclass*****************************************************************

class mclass:
    #Méthode d'initialisation
    def __init__(self,  window):
        
        #Définition des frame
        self.window = window
        self.window.title("Itegration Numérique - Ikram & Eya")
        self.window.geometry("1320x640")
        self.fr1 = Frame(window,highlightbackground="Purple", highlightthickness=2, width=100, height=100, bd= 5)
               
        self.fr2 = Frame(window,highlightbackground="Purple", highlightthickness=2, width=100, height=100, bd= 5)

        self.fr3 = Frame(window,highlightbackground="Purple", highlightthickness=2, width=100, height=300, bd= 5)
        
        #ComboBox
        self.a_txt=StringVar()
        self.a_txt.set("Choisir la méth:")
        self.label_a=Label(self.fr1,textvariable=self.a_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))    
        self.label_a.grid(sticky = E,row=1,column=0)

        self.num = tk.StringVar()
        self.c = ttk.Combobox(self.fr1,state="readonly", width=15,justify="center", textvariable=self.num)
        self.c['values'] = ('Rectangles','Point Milieux','Simpson','Trapèzes')
        self.c.current(0)
              
        #La fonction f
        self.func_txt=StringVar()
        self.func_txt.set("Fonction f à integrer:")
        self.label_func=Label(self.fr1,textvariable=self.func_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_func.grid(sticky = E, row=2, column=0)
        self.box = Entry(self.fr1,borderwidth=3,width=10,bg="Bisque", font=("Arial", 12))
        self.box.grid(row=2,column=1)
        

        #la borne inferieur a
        self.a_txt=StringVar()
        self.a_txt.set("Borne inferieur a:")
        self.label_a=Label(self.fr1,textvariable=self.a_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))    
        self.label_a.grid(sticky = E,row=3,column=0)
        self.boxa = Entry(self.fr1,width=10,borderwidth=3,bg="Bisque",font=("Arial", 12))
        self.boxa.grid(sticky = W,row=3,column=1)
      

        #la borne supérieur b
        self.b_txt=StringVar()
        self.b_txt.set("Borne inferieur b:")
        self.label_b=Label(self.fr1,textvariable=self.b_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_b.grid(sticky = E,row=4,column=0)
        self.boxb = Entry(self.fr1,width=10,borderwidth=3,bg="Bisque",font=("Arial", 12))
        self.boxb.grid(sticky = W,row=4,column=1)
        
        
        #Nombre des points n
        self.n_txt=StringVar()
        self.n_txt.set("Nombre des points n :")
        self.label_n=Label(self.fr1, textvariable=self.n_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_n.grid(sticky = E,row=5,column=0)
        self.boxn = Entry(self.fr1,width=10,borderwidth=3,bg="Bisque",font=("Arial", 12))
        self.boxn.grid(sticky = W,row=5,column=1)
        
        

        #FRAME
        self.c.grid(row=1,column=1)
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)
        self.fr3.grid(row=1,column=2,padx=10,pady=10)
        
        #self.fr4.grid(row=1,column=4,padx=10,pady=10)

        self.fig = Figure(figsize=(6,6))
        self.a = self.fig.add_subplot(111)
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.set_facecolor("white")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
         # Label Frame3
        self.integ_txt=StringVar()
        self.integ_txt.set("valeurs approché & Erreur ")
        self.label_integ = Label(self.fr3, textvariable=self.integ_txt,justify=RIGHT, anchor="w", height=4,font=("none 18 italic underline") )
        self.label_integ.grid(row=0,column=0,columnspan=3)

        # Label Frame1
        self.integ_txt=StringVar()
        self.integ_txt.set("Saisie des données ")
        self.label_integ = Label(self.fr1, textvariable=self.integ_txt,justify=RIGHT, anchor="w", height=4,font=("none 18 italic underline") )
        self.label_integ.grid(row=0,column=0,columnspan=3)
        
        # Labels des reusltats
                # Valeur Approché de la méthode des rectangles
        self.vaRect_txt=StringVar()
        self.vaRect_txt.set("Valeur approché m.Rectangle: ")
        self.label_vaRect = Label(self.fr3, textvariable=self.vaRect_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_vaRect.grid(sticky = E, row=1, column=0)
        
        self.res_Rect_txt=StringVar()
        self.res_Rect = Label(self.fr3,textvariable=self.res_Rect_txt,justify=RIGHT, anchor="w",bg="Bisque", width=15,borderwidth=3,font=("Arial", 9))
        self.res_Rect.grid(sticky = W, row=1, column=1)

                # Valeur Approché de la méthode des point milieux
        self.vaMilieu_txt=StringVar()
        self.vaMilieu_txt.set("valeur approché m.Milieu: ")
        self.label_vaMilieu = Label(self.fr3, textvariable=self.vaMilieu_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_vaMilieu.grid(sticky = E, row=3, column=0)
        
        self.res_Milieu_txt=StringVar()
        self.res_Milieu = Label(self.fr3,textvariable=self.res_Milieu_txt,justify=RIGHT, anchor="w",bg="Bisque", width=15,borderwidth=3,font=("Arial", 9))
        self.res_Milieu.grid(sticky = W, row=3, column=1)

                # Valeur Approché de la méthode des trapézes
        
        self.vaTrap_txt=StringVar()
        self.vaTrap_txt.set("Valeur Approché m.Trapézes: ")
        self.label_vaTrap = Label(self.fr3, textvariable=self.vaTrap_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_vaTrap.grid(sticky = E, row=5, column=0)
        
        self.res_Tra_txt=StringVar()
        self.res_Tra = Label(self.fr3,textvariable=self.res_Tra_txt,justify=RIGHT, anchor="w",bg="Bisque", width=15,borderwidth=3,font=("Arial", 9))
        self.res_Tra.grid(sticky = W, row=5, column=1)
      
                # Valeur Approché de la méthode de Simpson
        self.vaSim_txt=StringVar()
        self.vaSim_txt.set("Valeur Approché m.Simpson: ")
        self.label_vaSim = Label(self.fr3, textvariable=self.vaSim_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_vaSim.grid(sticky = E, row=7, column=0)
        
        self.res_va_txt=StringVar()
        self.res_va = Label(self.fr3,textvariable=self.res_va_txt,justify=RIGHT, anchor="w",bg="Bisque", width=15,borderwidth=3,font=("Arial", 9))
        self.res_va.grid(sticky = W, row=7, column=1)


                # Erreur Rectangle
        self.erect_txt=StringVar()
        self.erect_txt.set("Erreur m. Rectangle: ")
        self.label_er = Label(self.fr3, textvariable=self.erect_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_er.grid(sticky = E, row=2, column=0)
        
        self.res_erect_txt=StringVar()
        self.res_erect = Label(self.fr3,textvariable=self.res_erect_txt,justify=RIGHT, anchor="w",bg="Bisque", width=15,borderwidth=3,font=("Arial", 9))
        self.res_erect.grid(sticky = W, row=2, column=1)


                 # Erreur des point milieux
        self.erm_txt=StringVar()
        self.erm_txt.set("Erreur m. Milieu: ")
        self.label_er = Label(self.fr3, textvariable=self.erm_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_er.grid(sticky = E, row=4, column=0)
        
        self.res_em_txt=StringVar()
        self.res_em = Label(self.fr3,textvariable=self.res_em_txt,justify=RIGHT, anchor="w",bg="Bisque", width=15,borderwidth=3,font=("Arial", 9))
        self.res_em.grid(sticky = W, row=4, column=1)

                # Erreur de la méthode des trapézes
        self.etrap_txt=StringVar()
        self.etrap_txt.set("Erreur m. Trapézes: ")
        self.label_etrap = Label(self.fr3, textvariable=self.etrap_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_etrap.grid(sticky = E, row=6, column=0)
        
        self.res_etrap_txt=StringVar()
        self.res_etrap = Label(self.fr3,textvariable=self.res_etrap_txt,justify=RIGHT, anchor="w",bg="Bisque", width=15,borderwidth=3,font=("Arial", 9))
        self.res_etrap.grid(sticky = W, row=6, column=1)


                # Erreur de la méthode de Simpson
        self.ers_txt=StringVar()
        self.ers_txt.set("Erreur m. Simpson: ")
        self.label_ers = Label(self.fr3, textvariable=self.ers_txt,justify=RIGHT, anchor="w", height=3, font=("Arial", 12))
        self.label_ers.grid(sticky = E, row=8, column=0)
        
        self.res_es_txt=StringVar()
        self.res_es = Label(self.fr3,textvariable=self.res_es_txt,justify=RIGHT, anchor="w",bg="Bisque", width=15,borderwidth=3,font=("Arial", 9))
        self.res_es.grid(sticky = W, row=8, column=1)

        #Le Bouton "PLOT"
        self.button = Button (self.fr1, width =30,text="PLOT",bg="Moccasin",fg="#000000", font="Helvetica 11 italic bold", command=self.plot)
        self.button.grid(row=8,column=0,columnspan=3,pady=8)

        #Bouton PLOT ALL
        self.button1 = Button (self.fr1, width =30,text="PLOT All",bg="PeachPuff",fg="#000000", font="Helvetica 11 italic bold",command=self.plotall)
        self.button1.grid(row=9,column=0,columnspan=3,pady=8)

        #Bouton QUITTER
        self.button = Button(self.fr1, width =30,text="QUITTER",bg="DarkKhaki", fg="#000000", font="Helvetica 11 italic", command=self.choice_box)
        self.button.grid(row=11,column=0,columnspan=3,pady=8)

        #bouton reset
        self.buttonr = Button (self.fr1, width =30,text="RESET",bg="PaleGoldenrod",fg="#000000", font="Helvetica 12 italic",command=self.clear)
        self.buttonr.grid(row=10,column=0,columnspan=3,pady=8)       
    
    #action refresh
    def clear(self):
        self.fig.clf()
        self.a = self.fig.add_subplot(111)
        self.a.cla()
        self.a.grid(True)
        self.fig.canvas.draw()
        self.box.delete(0, END)
        self.boxa.delete(0, END)
        self.boxb.delete(0, END)
        self.boxn.delete(0, END)


        self.res_etrap_txt.set(" ")
        self.res_Rect_txt.set(" ")
        self.res_Milieu_txt.set(" ")
        self.res_Tra_txt.set(" ")

        self.res_va_txt.set(" ")
        self.res_erect_txt.set(" ")
        self.res_em_txt.set(" ")
        self.res_es_txt.set(" ")
        #self.a.clear()
        #self.canvas.get_tk_widget().pack_forget()
        #self.FigureCanvasTkAgg.clear() 
        #FigureCanvasTkAgg

        #self.box.set(" ")
        #self.boxa.delete(0, 'end')
    
    #L'action du boutton QUITTER
    def choice_box(self):
          answer = msg.askyesnocancel("Multi Choice Box Title", "Do You Want To Quite!")
 
          if answer == True:
             self.window.quit()
    
    #Méthode plot
    def plot (self):
        self.f= lambda x: eval(self.box.get())
       # x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
        #pp=f(x)
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.a.grid(True)
        test = self.c.get()
        if test == ('Trapèzes'):
            #plot valeur approché m. trapézes
            self.GraphTrap(self.f)
            self.I=self.IntegrateTrap(self.f)
            self.res_Tra_txt.set(self.I)

            #plot erreur trapéze
            result,e = quad(self.f, int(self.boxa.get()), int(self.boxb.get()))
            Erreur=result-self.IntegrateTrap(self.f)
            self.res_etrap_txt.set (Erreur)

            self.canvas.draw() 

        elif test ==('Rectangles'):
            #plot valeur approché m. rectangle
            self.GraphRect(self.f)
            self.I=self.IntegrateRect(self.f)
            self.res_Rect_txt.set(self.I)

            #plot erreur rectangle
            result,e = quad(self.f, int(self.boxa.get()), int(self.boxb.get()))
            Erreur=result-self.IntegrateRect(self.f)
            self.res_erect_txt.set (Erreur)

            self.canvas.draw()      
        elif test ==('Point Milieux'):
            #plot valeur approché m. pt milieu
            self.GraphPMilieu(self.f)
            self.I=self.IntegrateMilieu(self.f)
            self.res_Milieu_txt.set(self.I)

            #plot erreur pt milieu
            result,e = quad(self.f, int(self.boxa.get()), int(self.boxb.get()))
            Erreur=result-self.IntegrateMilieu(self.f)
            self.res_em_txt.set (Erreur)

            self.canvas.draw()          
        else:
            #plot valeur approché m. simpson
            self.GraphSim(self.f)
            self.I=self.IntegrateSim(self.f)
            self.res_va_txt.set(self.I)

            #plot erreur pt simpson
            result,e = quad(self.f, int(self.boxa.get()), int(self.boxb.get()))
            Erreur=result-self.IntegrateSim(self.f)
            self.res_es_txt.set (Erreur)

            self.canvas.draw() 
    #plot all
    def plotall (self):
        self.fig.clf()
        self.a = self.fig.add_subplot(111)
        self.a.cla()

        self.f= lambda x: eval(self.box.get())
        self.a = self.fig.add_subplot(221)  
        
        self.GraphTrap(self.f)
        #plot valeur approché m. trapézes
        self.I=self.IntegrateTrap(self.f)
        self.res_Tra_txt.set(self.I)
        
        self.a = self.fig.add_subplot(222)
        self.GraphRect(self.f)
        #plot valeur approché m. rectangles
        self.IR=self.IntegrateRect(self.f)
        self.res_Rect_txt.set(self.IR)

        self.a = self.fig.add_subplot(223)
        self.GraphPMilieu(self.f)
        #plot valeur approché m. pt milieu
        self.IM=self.IntegrateMilieu(self.f)
        self.res_Milieu_txt.set(self.IM)

        self.a = self.fig.add_subplot(224)
        self.GraphSim(self.f)
        #plot valeur approché m. simpson
        self.IS=self.IntegrateSim(self.f)
        self.res_va_txt.set(self.IS) 

        #plot erreur trapéze
        result,e = quad(self.f, int(self.boxa.get()), int(self.boxb.get()))
        Erreur=result-self.IntegrateTrap(self.f)
        self.res_etrap_txt.set (Erreur)

        #plot erreur rectangle
        result,e = quad(self.f, int(self.boxa.get()), int(self.boxb.get()))
        Erreur=result-self.IntegrateRect(self.f)
        self.res_erect_txt.set (Erreur)

        #plot erreur pt milieu
        result,e = quad(self.f, int(self.boxa.get()), int(self.boxb.get()))
        Erreur=result-self.IntegrateMilieu(self.f)
        self.res_em_txt.set (Erreur)

        #plot erreur pt simpson
        result,e = quad(self.f, int(self.boxa.get()), int(self.boxb.get()))
        Erreur=result-self.IntegrateSim(self.f)
        self.res_es_txt.set (Erreur)

        self.canvas.draw()
    
    #méthode GraphTrap
    def GraphTrap(self,f,resolution=1001):

        self.a.cla()
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.x = np.linspace(self.a_, self.b, self.n+1)
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a_, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
            self.a.plot(x_rect, y_rect,"m")
        yflist_fine = f(xlist_fine)
        self.a.plot(xlist_fine, yflist_fine)#plot de f(x)
        self.a.plot(xl, yl,"cs")#point support
        self.a.set_title('Methode des trapézes')
        self.a.set_ylabel ( ' f ( x ) ' )
        self.canvas.draw()
    def IntegrateTrap(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
    #méthode GraphRect
    def GraphRect(self,f,resolution=1001):
        
        self.a.cla()
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.x = np.linspace(self.a_, self.b, self.n+1)
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a_, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0 ,yl[i], yl[i] ,0 ,0 ]# ordonnees des sommets
            self.a.plot(x_rect, y_rect,"r")
        yflist_fine = f(xlist_fine)
        self.a.plot(xlist_fine, yflist_fine)#plot de f(x)
        self.a.plot(xl, yl,"cs")#point support
        self.a.set_title('Methode des rectangles')
        self.a.set_ylabel ( ' f ( x ) ' )

        self.canvas.draw()
    def IntegrateRect(self,f):
        x=self.x# contiens les xi
        y=f(x)#les yi
        h = float(x[1] - x[0])
        s = sum(y[0:-1])
        return h*s
    #Méthode GraphPMilieu
    def GraphPMilieu(self,f, resolution=1001):
        #fig = plt.figure(figsize=(7, 5.5)
        self.a.cla()
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.x = np.linspace(self.a_, self.b, self.n+1)
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace( self.a_, self.b , resolution )
        for i in range ( self.n ) :
            mi=(xl[i]+xl[i+1])/2
            x_rect = [xl[ i ] , xl[ i ] , xl[ i + 1 ] , xl[i+1] , xl[ i ] ] # abscisses des sommets
            y_rect = [0 , f(mi) , f(mi) , 0 , 0 ] # ordonnees des sommets
            self.a.plot ( x_rect , y_rect , 'r' )
            self.a.plot(mi,f(mi),'b*')
        yflist_fine=f(xlist_fine)
        self.a.plot (xlist_fine,yflist_fine )
        self.a.plot(xl, yl,"cs")#point support
        self.a.set_title(' Méthode des points milieux')
        #self.fig( 0.5*( self.a+ self.b ) , f(self.b ) , '$I_{%s}$ =%12.4f' % (self.n,self.integrate(f)),fontsize =15 )
        self.canvas.draw()
    def IntegrateMilieu(self,f):
        x=self.x
        h = float(x[1] - x[0])
        yml=[]
        for i in range(self.n):
            lm=(x[i]+x[i+1])*0.5
            lym=f(lm)
            yml.append(lym)
        s = sum(yml)
        return h*s
    #Méthode GraphSim
    def GraphSim(self,f, resolution=1001):
        self.a.cla()
        self.a_ = int(self.boxa.get())
        self.b = int(self.boxb.get())
        self.n = int(self.boxn.get())
        self.x = np.linspace(self.a_, self.b, self.n+1)
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace( self.a_, self.b , resolution )
        for i in range ( self.n ) :
            xx=np.linspace(xl[i],xl[i+1],resolution)
            m=(xl[i]+xl[i+1])/2
            aa=xl[i]
            bb=xl[i+1]
            l0=(xx-m)/(aa-m)*(xx-bb)/(aa-bb)
            l1=(xx-aa)/(m-aa)*(xx-bb)/(m-bb)
            l2=(xx-aa)/(bb-aa)*(xx-m)/(bb-m)
            P=f(aa)*l0+f(m)*l1+f(bb)*l2
            self.a.plot(xx,P,'b')
            self.a.plot(m,f(m),"r*")
    
        yflist_fine = f(xlist_fine)
        self.a.plot(xlist_fine, yflist_fine,'g')
        self.a.plot(xl, yl, "bo")
        #fig.set_xlabel('x')
        self.a.set_title(' Méthode de Simpson')
        #fig.text( 0.5*( self.a+ self.b ) , f(self.b ) , '$I_{%s}$ =%4.4f'.format(self.n,self.integrate( f ) ) , fontsize =15 )
        self.canvas.draw()

    def IntegrateSim ( self , f ) :
        x = self.x
        y=f(x)
        h=float(x[1]-x[0])
        n=len(x)-1
        if n%2==1:
            n-=1
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        return h*s/3.0
if __name__ == '__main__':
    window= Tk()

    start= mclass(window)

    window.mainloop()

