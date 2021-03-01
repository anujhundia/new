from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import db.db


class DashboardWindow:

    def __init__(self,root):
        self.root = root
        self.root.title=("Local Train Ticketing System")
        self.root.geometry("1550x900+0+0")
        self.root.configure(background='gainsboro')

        MainFrame= Frame(self.root, bd=10, width= 1350, height=700, bg='gainsboro', relief= RIDGE)
        MainFrame.grid()

        TopFrame1= Frame(MainFrame, bd=10, width= 1340, height=100, bg='gainsboro', relief= RIDGE)
        TopFrame1.grid()

        TopFrame2= Frame(MainFrame, bd=10, width= 1300, height=500, bg='gainsboro', relief= RIDGE)
        TopFrame2.grid()

        f1= Frame(TopFrame2, width=890, height=500 ,bd=5,  relief=RIDGE)
        f1.grid(row=1, column=0)

        f2= Frame(TopFrame2, width=400, height=500 ,pady=2,bd=5 , relief=RIDGE)
        f2.grid(row=1, column=1)

        frametopRight=Frame(f2,width=404,height=420,bd=5,relief=RIDGE)
        frametopRight.pack(side=TOP)
        frameBottomRight=Frame(f2,width=408,height=100,bd=5,pady=15,relief=RIDGE)
        frameBottomRight.pack(side=BOTTOM)

        f1a=Frame(f1,width=900,height=330,bd=5,relief=RIDGE)
        f1a.pack(side=TOP)
        f2a=Frame(f1,width=900,height=320,bd=5,relief=RIDGE)
        f2a.pack(side=BOTTOM)

        topLeft1=Frame(f1a,width=300,height=200,bd=5,padx=20,pady=1,relief=RIDGE)
        topLeft1.pack(side=LEFT)
        topLeft2=Frame(f1a,width=300,height=200,bd=5,relief=RIDGE)
        topLeft2.pack(side=RIGHT)
        topLeft3=Frame(f1a,width=300,height=200,bd=5,pady=5,relief=RIDGE)
        topLeft3.pack(side=RIGHT)

        bottomLeft1=Frame(f2a,width=450, height=300, bd=5, pady=12,relief=RIDGE)
        bottomLeft1.pack(side=LEFT)

        bottomLeft2=Frame(f2a, width=450, height=300, bd=5, relief=RIDGE)
        bottomLeft2.pack(side=RIGHT)

        lblTitle=Label(TopFrame1, font=('arial',40, 'bold'), text="TRAIN TICKETING SYSTEM",bd=5,width=41,padx=4,justify='center')
        lblTitle.grid(row=0,column=0)

        Date1 = StringVar()
        time1 = StringVar()
        Ticketclass = StringVar()
        TicketPrice = StringVar()
        
        Adult_Ticket = StringVar()
        source = StringVar()
        destination = StringVar()
        Fee_Price = StringVar()
        Route = StringVar()
        refid = StringVar()

        Ticketclass.set("")
        TicketPrice.set("")
        
        Adult_Ticket.set("")
        source.set("")
        destination.set("")
        Fee_Price.set("")
        Route.set("")
        refid.set("")

        var1=IntVar()
        var2=IntVar()
        var4=IntVar()
        var6=IntVar()
        var7=StringVar()
        var9=StringVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()

        Tax=StringVar()
        SubTotal=StringVar()
        Total=StringVar()

        var1.set("0")
        var2.set("0")
        var4.set("0")
        var6.set("0")
        var7.set("0")
        var9.set("0")
        var10.set("0")
        var11.set("0")
        var12.set("0")
        

        def iExit():
            iExit=tkinter.messagebox.askyesno("Train Ticketing Systme","Confirm if you want to quit")
            if iExit > 0:
                root.destroy()
                return
                

        def Reset():
            var1.set("0")
            var2.set("0")
            var4.set("0")
            var6.set("0")
            var7.set("0")
            var9.set("0")
            var10.set("0")
            var11.set("0")
            var12.set("0")
            Tax.set("0")
            SubTotal.set("0")
            Total.set("0")
            Ticketclass.set("")
            TicketPrice.set("")
            
            Adult_Ticket.set("")
            source.set("")
            destination.set("")
            Fee_Price.set("")
            Route.set("")
            refid.set("")

        def Travel_Cost():
            if((var9.get() =="DADAR" or var9.get()=="KURLA")  and var1.get() == 1 and var4.get()==1):
                Tcost=5
                Single =var12.get()
                Return_cost=var6.get()
                Adult_Tax=(Tcost * Single)*0.18
                Adult_Fees=(Tcost * Single)
                totalcost=(Tcost * Single)+((Tcost*Single)*0.18)
                if (Return_cost>0):
                    Tcost=10
                    Adult_Fees=(Tcost * Return_cost)
                    Adult_Tax=(Tcost * Return_cost)*0.18
                    totalcost=(Tcost * Return_cost)+((Tcost*Return_cost)*0.18)
                Tax.set(Adult_Tax)
                SubTotal.set(Adult_Fees)
                Ticketclass.set("II CLASS")
                TicketPrice.set(Adult_Fees)
                
                Adult_Ticket.set("Yes")
                source.set("CSTM")
                destination.set(var9.get())
                Fee_Price.set(totalcost)
                Total.set(totalcost)
                Route.set("Direct")
                x=random.randint(109,5876)
                randomRef=str(x)
                refid.set("TFL"+randomRef) 
                db.db.addtraindata(source.get(),destination.get(),totalcost,refid.get())

            elif((var9.get() =="MULUND" or var9.get()=="THANE")  and var1.get() == 1 and var4.get()==1):
                Tcost=10
                Single =var12.get()
                Return_cost=var6.get()
                Adult_Tax=(Tcost * Single)*0.18
                Adult_Fees=(Tcost * Single)
                totalcost=(Tcost * Single)+((Tcost*Single)*0.18)
                if (Return_cost>0):
                    Tcost=15
                    Adult_Fees=(Tcost * Return_cost)
                    Adult_Tax=(Tcost * Return_cost)*0.18
                    totalcost=(Tcost * Return_cost)+((Tcost*Return_cost)*0.18)
                Tax.set(Adult_Tax)
                SubTotal.set(Adult_Fees)
                Ticketclass.set("II CLASS")
                TicketPrice.set(Adult_Fees)
                
                Adult_Ticket.set("Yes")
                source.set("CSTM")
                destination.set(var9.get())
                Fee_Price.set(totalcost)
                Total.set(totalcost)
                Route.set("Direct")
                x=random.randint(109,5876)
                randomRef=str(x)
                refid.set("TFL"+randomRef)
                db.db.addtraindata(source.get(),destination.get(),totalcost,refid.get())

            elif(var9.get() =="KALYAN" and var1.get() == 1 and var4.get()==1):
                Tcost=15
                Single =var12.get()
                Return_cost=var6.get()
                Adult_Tax=(Tcost * Single)*0.18
                Adult_Fees=(Tcost * Single)
                totalcost=(Tcost * Single)+((Tcost*Single)*0.18)
                if (Return_cost>0):
                    Tcost=20
                    Adult_Fees=(Tcost * Return_cost)
                    Adult_Tax=(Tcost * Return_cost)*0.18
                    totalcost=(Tcost * Return_cost)+((Tcost*Return_cost)*0.18)
                Tax.set(Adult_Tax)
                SubTotal.set(Adult_Fees)
                Ticketclass.set("II CLASS")
                TicketPrice.set(Adult_Fees)
                
                Adult_Ticket.set("Yes")
                source.set("CSTM")
                destination.set("KALYAN")
                Fee_Price.set(totalcost)
                Total.set(totalcost)
                Route.set("Direct")
                x=random.randint(109,5876)
                randomRef=str(x)
                refid.set("TFL"+randomRef)
                db.db.addtraindata(source.get(),destination.get(),totalcost,refid.get())            
            elif((var9.get() =="DADAR" or var9.get()=="KURLA")  and var2.get() == 1 and var4.get()==1):
                Tcost=50
                Single =var12.get()
                Return_cost=var6.get()
                Adult_Tax=(Tcost * Single)*0.18
                Adult_Fees=(Tcost * Single)
                totalcost=(Tcost * Single)+((Tcost*Single)*0.18)
                if (Return_cost>0):
                    Tcost=100
                    Adult_Fees=(Tcost * Return_cost)
                    Adult_Tax=(Tcost * Return_cost)*0.18
                    totalcost=(Tcost * Return_cost)+((Tcost*Return_cost)*0.18)
                Tax.set(Adult_Tax)
                SubTotal.set(Adult_Fees)
                Ticketclass.set("I CLASS")
                TicketPrice.set(Adult_Fees)
                
                Adult_Ticket.set("Yes")
                source.set("CSTM")
                destination.set(var9.get())
                Fee_Price.set(totalcost)
                Total.set(totalcost)
                Route.set("Direct")
                x=random.randint(109,5876)
                randomRef=str(x)
                refid.set("TFL"+randomRef) 
                db.db.addtraindata(source.get(),destination.get(),totalcost,refid.get())
            elif((var9.get() =="MULUND" or var9.get()=="THANE")  and var2.get() == 1 and var4.get()==1):
                Tcost=140
                Single =var12.get()
                Return_cost=var6.get()
                Adult_Tax=(Tcost * Single)*0.18
                Adult_Fees=(Tcost * Single)
                totalcost=(Tcost * Single)+((Tcost*Single)*0.18)
                if (Return_cost>0):
                    Tcost=280
                    Adult_Fees=(Tcost * Return_cost)
                    Adult_Tax=(Tcost * Return_cost)*0.18
                    totalcost=(Tcost * Return_cost)+((Tcost*Return_cost)*0.18)
                Tax.set(Adult_Tax)
                SubTotal.set(Adult_Fees)
                Ticketclass.set("I CLASS")
                TicketPrice.set(Adult_Fees)
                
                Adult_Ticket.set("Yes")
                source.set("CSTM")
                destination.set(var9.get())
                Fee_Price.set(totalcost)
                Total.set(totalcost)
                Route.set("Direct")
                x=random.randint(109,5876)
                randomRef=str(x)
                refid.set("TFL"+randomRef)
                db.db.addtraindata(source.get(),destination.get(),totalcost,refid.get())
            elif(var9.get() =="KALYAN" and var2.get() == 1 and var4.get()==1):
                Tcost=165
                Single =var12.get()
                Return_cost=var6.get()
                Adult_Tax=(Tcost * Single)*0.18
                Adult_Fees=(Tcost * Single)
                totalcost=(Tcost * Single)+((Tcost*Single)*0.18)
                if (Return_cost>0):
                    Tcost=330
                    Adult_Fees=(Tcost * Return_cost)
                    Adult_Tax=(Tcost * Return_cost)*0.18
                    totalcost=(Tcost * Return_cost)+((Tcost*Return_cost)*0.18)
                Tax.set(Adult_Tax)
                SubTotal.set(Adult_Fees)
                Ticketclass.set("I CLASS")
                TicketPrice.set(Adult_Fees)
                
                Adult_Ticket.set("Yes")
                source.set("CSTM")
                destination.set("KALYAN")
                Fee_Price.set(totalcost)
                Total.set(totalcost)
                Route.set("Direct")
                x=random.randint(109,5876)
                randomRef=str(x)
                refid.set("TFL"+randomRef)
                db.db.addtraindata(source.get(),destination.get(),totalcost,refid.get())
        

        lblReceipt=Label(frametopRight, font=('arial',18, 'bold'), text="TRAVELLING TICKETING SYSTEM",bd=5,pady=10,padx=4,width=28,justify='center')
        lblReceipt.grid(row=0,column=0)

        lblClass1=Label(frameBottomRight, font=('arial',14, 'bold'), text="Class",width=8,relief='sunken',justify='center')
        lblClass1.grid(row=0,column=0)

        lblClass2=Label(frameBottomRight, font=('arial',14, 'bold'),width=8,relief='sunken',textvariable=Ticketclass,justify='center')
        lblClass2.grid(row=1,column=0)

        lblTicket1=Label(frameBottomRight, font=('arial',14, 'bold'), text="Ticket",width=8,relief='sunken',justify='center')
        lblTicket1.grid(row=0,column=1)

        lblTicket2=Label(frameBottomRight, font=('arial',14, 'bold'),width=8,relief='sunken',textvariable=TicketPrice,justify='center')
        lblTicket2.grid(row=1,column=1)

        lblAdult1=Label(frameBottomRight, font=('arial',14, 'bold'), text="Adult",width=8,relief='sunken',justify='center')
        lblAdult1.grid(row=0,column=2)

        lblAdult2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief='sunken',textvariable=Adult_Ticket,justify='center')
        lblAdult2.grid(row=1,column=2)

        

        lblsp=Label(frameBottomRight, font=('arial',14, 'bold'),width=36,height=2,relief='sunken',bg='lightgray')
        lblsp.grid(row=2,column=0,columnspan=4)

        lblFrom1=Label(frameBottomRight, font=('arial',14, 'bold'), text="From",width=8,relief='sunken',justify='center')
        lblFrom1.grid(row=3,column=1)
        
        lblFrom2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief='sunken',textvariable=source,justify='center')
        lblFrom2.grid(row=3,column=2)

        lblTo1=Label(frameBottomRight, font=('arial',14, 'bold'), text="To",width=8,relief='sunken',justify='center')
        lblTo1.grid(row=4,column=1)
        
        lblTo2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief='sunken',textvariable=destination,justify='center')
        lblTo2.grid(row=4,column=2)

        lblPrice1=Label(frameBottomRight, font=('arial',14, 'bold'), text="Price",width=8,relief='sunken',justify='center')
        lblPrice1.grid(row=5,column=1)
        
        lblPrice2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief='sunken',textvariable=Fee_Price,justify='center')
        lblPrice2.grid(row=5,column=2)

        lblsp=Label(frameBottomRight, font=('arial',14, 'bold'), width=36,height=2,relief='sunken',bg='lightgray')
        lblsp.grid(row=6,column=0,columnspan=4)
        
        lblRefNo1=Label(frameBottomRight, font=('arial',14, 'bold'), text="Ref No",width=8,relief='sunken',justify='center')
        lblRefNo1.grid(row=7,column=0)
        
        lblRefNo2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief='sunken',textvariable=refid,justify='center')
        lblRefNo2.grid(row=8,column=0)
        
        lblTime1=Label(frameBottomRight, font=('arial',14, 'bold'), text="Time",width=8,relief='sunken',justify='center')
        lblTime1.grid(row=7,column=1)
        
        lblTime2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief='sunken',textvariable=time1,justify='center')
        lblTime2.grid(row=8,column=1)

        lblDate1=Label(frameBottomRight, font=('arial',14, 'bold'), text="Date",width=8,relief='sunken',justify='center')
        lblDate1.grid(row=7,column=2)
        
        lblDate2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief='sunken',textvariable=Date1,justify='center')
        lblDate2.grid(row=8,column=2)

        lblRoute1=Label(frameBottomRight, font=('arial',14, 'bold'), text="Route",width=8,relief='sunken',justify='center')
        lblRoute1.grid(row=7,column=3)
        
        lblRoute2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief='sunken',textvariable=Route,justify='center')
        lblRoute2.grid(row=8,column=3) 
        
        Date1.set(time.strftime("%d/%m/%Y"))
        time1.set(time.strftime("%H:%M:%S"))

        lblClass =Label(topLeft1, font=('arial',20,'bold'),text="Class",bd=8)
        lblClass.grid(row=0,column=0,sticky=W)

        chkSecondClass=Checkbutton(topLeft1,font=('arial',20,'bold'),text="Second Class",variable=var1,onvalue=1,offvalue=0)
        chkSecondClass.grid(row=1,column=0,sticky=W)
        chkFirstClass=Checkbutton(topLeft1,font=('arial',20,'bold'),text="First Class",variable=var2,onvalue=1,offvalue=0)
        chkFirstClass.grid(row=2,column=0,sticky=W)

        lblSelect =Label(topLeft3, font=('arial',20,'bold'),text="Select Destination",bd=8)
        lblSelect.grid(row=0,column=0,sticky=W,columnspan=2)
        lblDestination=Label(topLeft3,font=('arial',20,'bold'),text="Destination",bd=8)
        lblDestination.grid(row=1,column=0,sticky=W)
        cboDesitnation=ttk.Combobox(topLeft3,textvariable=var9,font=('arial',20,'bold'),state='readonly',width=8)
        cboDesitnation['value']=('','DADAR','KURLA','MULUND','THANE','KALYAN')
        cboDesitnation.current(0)
        cboDesitnation.grid(row=1,column=1)

        chkAdult=Checkbutton(topLeft3,font=('arial',20,'bold'),text="Adult",variable=var4,onvalue=1,offvalue=0)
        chkAdult.grid(row=2,column=0,sticky=W)
        
        
        lblTicketType=Label(topLeft2,font=('arial',20,'bold'),text="Ticket Type", bd=8)
        lblTicketType.grid(row=0,column=0,sticky=W)
        chkSingle=Checkbutton(topLeft2,font=('arial',20,'bold'),text="Single",variable=var10,onvalue=1,offvalue=0)
        chkSingle.grid(row=1,column=0,sticky=W)
        entSingle=Entry(topLeft2,font=('arial',20,'bold'),textvariable=var12, bd=2,width=8)
        entSingle.grid(row=1,column=1,sticky=W)
        chkReturn=Checkbutton(topLeft2,font=('arial',20,'bold'),text="Return",variable=var11 ,onvalue=1,offvalue=0)
        chkReturn.grid(row=2,column=0,sticky=W)
        entReturn=Entry(topLeft2,font=('arial',20,'bold'),textvariable=var6, bd=2,width=8)
        entReturn.grid(row=2,column=1,sticky=W)
        lblComment=Label(topLeft2,font=('arial',20,'bold'),text="Comment", bd=8)
        lblComment.grid(row=3,column=0,sticky=W)
        entComment=Entry(topLeft2,font=('arial',20,'bold'),textvariable=var7, bd=8,width=8)
        entComment.grid(row=3,column=1,sticky=W)

        lblTax=Label(bottomLeft1,font=('arial',20,'bold'),text="GST", bd=8)
        lblTax.grid(row=0,column=0,sticky=W)
        entTax=Entry(bottomLeft1,font=('arial',20,'bold'),textvariable=Tax, bd=5,width=28)
        entTax.grid(row=0,column=1,sticky=W)

        lblSubTotal=Label(bottomLeft1,font=('arial',20,'bold'),text="Subtotal", bd=8)
        lblSubTotal.grid(row=1,column=0,sticky=W)
        entSubTotal=Entry(bottomLeft1,font=('arial',20,'bold'),textvariable=SubTotal, bd=5,width=28)
        entSubTotal.grid(row=1,column=1,sticky=W)

        lblTotal=Label(bottomLeft1,font=('arial',20,'bold'),text="Total", bd=8)
        lblTotal.grid(row=2,column=0,sticky=W)
        entTotal=Entry(bottomLeft1,font=('arial',20,'bold'),textvariable=Total, bd=5,width=28)
        entTotal.grid(row=2,column=1,sticky=W)



        btnTotal=Button(frameBottomRight,font=('arial',14,'bold'), text="Total",width=8,height=1,padx=2,pady=16,bd=2,command=Travel_Cost)
        btnTotal.grid(row=10,column=0)
        btnClear=Button(frameBottomRight,font=('arial',14,'bold'), text="Clear",width=8,height=1,padx=2,pady=16,bd=2,command=Reset)
        btnClear.grid(row=10,column=1)
        btnReset=Button(frameBottomRight,font=('arial',14,'bold'), text="Reset",width=8,height=1,padx=2,pady=16,bd=2,command=Reset)
        btnReset.grid(row=10,column=2)
        btnExit=Button(frameBottomRight,font=('arial',14,'bold'), text="Exit",width=8,height=1,padx=2,pady=16,bd=2,command=iExit)
        btnExit.grid(row=10,column=3)
        
        
        

if __name__=='__main__':
    root=Tk()
    application= DashboardWindow(root)
    root.mainloop()
