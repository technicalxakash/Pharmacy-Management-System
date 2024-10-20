from datetime import datetime
from tkinter import *
from tkinter import ttk
import random
import time
import tkinter.messagebox

def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("PHARMACY")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="white")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, font=("arial", 50, "bold"), text="PHARMACY", bd=20)
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.login1 = Frame(self.frame, width=1010, height=300, relief="ridge", bd=20)
        self.login1.grid(row=1, column=0)

        self.login2 = Frame(self.frame, width=1000, height=100, relief="ridge", bd=20)
        self.login2.grid(row=2, column=0)

        self.login3 = Frame(self.frame, width=1000, height=200, relief="ridge", bd=20)
        self.login3.grid(row=3, column=0)

        # Labels and Entry Boxes
        labels = ["Username", "Password"]
        for i in range(len(labels)):
            cur_label = Label(self.login1, font=("arial", 30, "bold"), text=labels[i], bd=22)
            cur_label.grid(row=i, column=0)

        entry_box = {"Username": self.Username, "Password": self.Password}
        counter = 0
        for i in entry_box:
            cur_entrybox = Entry(self.login1, font=("arial", 30, "bold"), bd=22, textvariable=entry_box[i])
            cur_entrybox.grid(row=counter, column=1, padx=85)
            if counter == 1:
                cur_entrybox.config(show="*")
            counter += 1

        # Buttons
        self.btnlogin = Button(self.login2, text="Login", width=17, font=("arial", 20, "bold"), command=self.LoginSystem)
        self.btnlogin.grid(row=0, column=0)

        self.btnReset = Button(self.login2, text="Reset", width=17, font=("arial", 20, "bold"), command=self.Reset)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.login2, text="Exit", width=17, font=("arial", 20, "bold"), command=self.iExit)
        self.btnExit.grid(row=0, column=2)

        self.btnReg = Button(self.login3, text="Patients Registrations", font=("arial", 20, "bold"), state=DISABLED, command=self.Registeration_window)
        self.btnReg.grid(row=0, column=0, pady=8, padx=57)

        self.btnPhar = Button(self.login3, text="Pharmacy Management", font=("arial", 20, "bold"), state=DISABLED, command=self.Pharmacy_window)
        self.btnPhar.grid(row=0, column=1, pady=8, padx=57)

    def LoginSystem(self):
        user = self.Username.get()
        password = self.Password.get()

        if (user in ["ADMIN", "admin", "Admin"]) and (password == "111"):
            self.btnReg.config(state=NORMAL)
            self.btnPhar.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Hospital Management", "Invalid username or password, please try again.")
            self.btnReg.config(state=DISABLED)
            self.btnPhar.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")

    def Reset(self):
        self.btnReg.config(state=DISABLED)
        self.btnPhar.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Hospital Management", "Please confirm to exit!")
        if self.iExit > 0:
            self.master.destroy()
        return

    def Registeration_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Window2(self.newwindow)

    def Pharmacy_window(self):
        self.newwindow = Toplevel(self.master)
        self.app = Window3(self.newwindow)

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registrations")
        self.master.geometry("1350x750+0+0")
        self.master.configure(background="grey")
        self.frame = Frame(self.master)
        self.frame.pack()

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = IntVar()

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Telephone = StringVar()
        Ref = StringVar()
        Date = StringVar()

        Membership = StringVar()
        Membership.set("0")

        # Functions
        def iExit():
            iExit = tkinter.messagebox.askyesno("Patient Registrations", "Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Date.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)

        def iDelete():
            Reset()
            self.txtRecipt.delete("1.0", END)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Patient Registrations", "Confirm if you want to Add a new record")
            if iResetRecord > 0:
                Reset()
            elif iResetRecord <= 0:
                Reset()
                self.txtRecipt.delete("1.0", END)
                return

        def Ref_No():
            x = random.randint(1000, 60000)
            randomRef = str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtRecipt.insert(END, "\t" + Ref.get() + "\t\t" + Firstname.get() + "\t\t" + Surname.get() + "\t\t" + Address.get() + "\t\t" + DateofOrder.get() + "\t\t" + Telephone.get() + "\t\t" + Membership.get() + "\n")

        def Fees():
            if var4.get() == 1:
                self.txtMembership.configure(state=NORMAL)
                Item1 = float(500)
                Membership.set("Rs" + str(Item1))
            elif var4.get() == 0:
                self.txtMembership.configure(state=DISABLED)
                Membership.set("0")

        # Frames
        Mainframe = Frame(self.frame)
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, bd=20, width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 59, 'bold'), text="Patient Registrations", padx=2)
        self.lblTitle.grid()

        MemberDetailFrame = LabelFrame(Mainframe, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
        MemberDetailFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailFrame, bd=10, width=880, height=400, relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, width=350, height=400, font=('arial', 12, 'bold'), text="Patient Name", relief=RIDGE)
        MembersName_F.grid(row=0, column=0)

        Recipt_ButtonFrame = LabelFrame(MemberDetailFrame, bd=10, width=1000, height=400, relief=RIDGE)
        Recipt_ButtonFrame.pack(side=RIGHT)

        # Labels and Entry Boxes
        self.lblReferenceNo = Label(MembersName_F, font=('arial', 14, 'bold'), text="Reference no.", bd=7)
        self.lblReferenceNo.grid(row=0, column=0, sticky=W)
        self.txtReferenceNo = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=Ref, state=DISABLED, insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblDate = Label(MembersName_F, font=('arial', 14, 'bold'), text="Date", bd=7)
        self.lblDate.grid(row=6, column=0, sticky=W)
        self.txtDate = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=DateofOrder, insertwidth=2)
        self.txtDate.grid(row=6, column=1)

        labels = ["Firstname", "Surname", "Address", "Postcode", "Telephone"]
        row_number = 1
        entry_boxes = [Firstname, Surname, Address, Postcode, Telephone]
        counter = 0
        for i in labels:
            cur_label = Label(MembersName_F, font=("arial", 14, "bold"), text=i, bd=7)
            cur_label.grid(row=row_number, column=0, sticky=W)
            row_number += 1

        row_number = 1
        for i in entry_boxes:
            cur_entrybox = Entry(MembersName_F, font=("arial", 14, "bold"), bd=7, textvariable=i, insertwidth=2)
            cur_entrybox.grid(row=row_number, column=1)
            row_number += 1

        self.lblProof = Label(MembersName_F, font=("arial", 14, "bold"), text="Proof of ID", bd=7)
        self.lblProof.grid(row=7, column=0, sticky=W)
        self.cboProve_of_ID = ttk.Combobox(MembersName_F, font=("arial", 14, "bold"), width=19, state="readonly", textvariable=var1)
        self.cboProve_of_ID['value'] = ("", "Aadhar Card", "Driving License", "Passport", "Voter Card")
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7, column=1)

        self.lblType_of_Member = Label(MembersName_F, font=("arial", 14, "bold"), text="Type of Member", bd=7)
        self.lblType_of_Member.grid(row=8, column=0, sticky=W)
        self.cboType_of_Member = ttk.Combobox(MembersName_F, font=("arial", 14, "bold"), width=19, state="readonly", textvariable=var2)
        self.cboType_of_Member['value'] = ("", "Full Member", "Annual Member", "Pay As You Go", "Honorary Member")
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8, column=1)

        self.lblMethod_of_Payment = Label(MembersName_F, font=("arial", 14, "bold"), text="Method of Payment", bd=7)
        self.lblMethod_of_Payment.grid(row=9, column=0, sticky=W)
        self.cboMethod_of_Payment = ttk.Combobox(MembersName_F, font=("arial", 14, "bold"), width=19, state="readonly", textvariable=var3)
        self.cboMethod_of_Payment['value'] = ("", "Cash", "Debit Card", "Master Card", "Visa Card", "Paytm", "Google Pay")
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9, column=1)

        self.chkMembership = Checkbutton(MembersName_F, text="Membership Fees", variable=var4, onvalue=1, offvalue=0, font=("arial", 14, "bold"), command=Fees).grid(row=10, column=0, sticky=W)

        self.txtMembership = Entry(MembersName_F, font=("arial", 14, "bold"), bd=7, insertwidth=2, state=DISABLED, textvariable=Membership)
        self.txtMembership.grid(row=10, column=1)

        # Receipt
        self.lblLabel = Label(Recipt_ButtonFrame, font=("arial", 10, "bold"), pady=10, text="Reference no.\t Firstname \t Surname \t Address \t Date \t Telephone \t Membership Fee", bd=7)
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtRecipt = Text(Recipt_ButtonFrame, width=112, height=22, font=("arial", 10, "bold"))
        self.txtRecipt.grid(row=1, column=0, columnspan=4)

        # Buttons
        self.btnTotalandAddData = Button(Recipt_ButtonFrame, padx=18, bd=7, font=("arial", 16, "bold"), width=13, height=2, text="Add Data", command=Receipt)
        self.btnTotalandAddData.grid(row=2, column=0)

        self.btnAddData = Button(Recipt_ButtonFrame, padx=18, bd=7, font=("arial", 16, "bold"), width=13, height=2, text="Reset", command=iResetRecord)
        self.btnAddData.grid(row=2, column=1)

        self.btnRecipt = Button(Recipt_ButtonFrame, padx=18, bd=7, font=("arial", 16, "bold"), width=13, height=2, text="Delete", command=iDelete)
        self.btnRecipt.grid(row=2, column=2)

        self.btnExit = Button(Recipt_ButtonFrame, padx=18, bd=7, font=("arial", 16, "bold"), width=13, height=2, text="Exit", command=iExit)
        self.btnExit.grid(row=2, column=3)

class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.master.configure(background="white")
        self.frame = Frame(self.master)
        self.frame.pack()

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = DoubleVar()
        var6 = DoubleVar()
        var7 = DoubleVar()
        var8 = DoubleVar()
        var9 = DoubleVar()
        var10 = DoubleVar()
        var11 = DoubleVar()
        var12 = DoubleVar()
        var13 = DoubleVar()
        var14 = DoubleVar()
        var15 = DoubleVar()

        # Frames
        Mainframe = Frame(self.frame)
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, bd=20, width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=("arial", 59, "bold"), text="Pharmacy Management System", padx=2)
        self.lblTitle.grid()

        DataFrame = Frame(Mainframe, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=("arial", 12, "bold"), text="Prescription")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE, font=("arial", 12, "bold"), text="Prescription")
        DataFrameRIGHT.pack(side=RIGHT)

        ButtonFrame = Frame(Mainframe, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        # Functions
        def iExit():
            iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return

        def iReset():
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            self.txtReceipt.delete("1.0", END)

        def iReceipt():
            self.txtReceipt.insert(END, "\t" + var1.get() + "\t" + var2.get() + "\t" + var3.get() + "\t" + var4.get() + "\t" + str(var5.get()) + "\t" + str(var6.get()) + "\t" + str(var7.get()) + "\t" + str(var8.get()) + "\t" + str(var9.get()) + "\t" + str(var10.get()) + "\t" + str(var11.get()) + "\t" + str(var12.get()) + "\t" + str(var13.get()) + "\t" + str(var14.get()) + "\t" + str(var15.get()) + "\n")

        def iTotal():
            Item1 = float(var5.get())
            Item2 = float(var6.get())
            Item3 = float(var7.get())
            Item4 = float(var8.get())
            Item5 = float(var9.get())
            Item6 = float(var10.get())
            Item7 = float(var11.get())
            Item8 = float(var12.get())

            Price = (Item1 + Item2 + Item3 + Item4 + Item5 + Item6 + Item7 + Item8)
            Tax = (Price * 0.05)
            SubTotal = (Price)
            Total = (Price + Tax)
            var13.set(Tax)
            var14.set(SubTotal)
            var15.set(Total)

        # Labels and Entry Boxes
        self.lblNameTablet = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Name of Tablet", padx=2, pady=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(DataFrameLEFT, font=("arial", 12, "bold"), width=23, textvariable=var1, state="readonly")
        self.cboNameTablet['value'] = ("", "Ibuprofen", "Paracetamol", "Aspirin", "Amoxicillin", "Ciprofloxacin")
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        self.lblFurtherInformation = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Further Information", padx=2, pady=2)
        self.lblFurtherInformation.grid(row=1, column=0, sticky=W)
        self.txtFurtherInformation = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var2, width=25)
        self.txtFurtherInformation.grid(row=1, column=1)

        self.lblStorageAdvice = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Storage Advice", padx=2, pady=2)
        self.lblStorageAdvice.grid(row=2, column=0, sticky=W)
        self.txtStorageAdvice = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var3, width=25)
        self.txtStorageAdvice.grid(row=2, column=1)

        self.lblDose = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Dose(mg)", padx=2, pady=2)
        self.lblDose.grid(row=3, column=0, sticky=W)
        self.txtDose = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var4, width=25)
        self.txtDose.grid(row=3, column=1)

        self.lblNumberTablets = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="No. of Tablets", padx=2, pady=2)
        self.lblNumberTablets.grid(row=4, column=0, sticky=W)
        self.txtNumberTablets = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var5, width=25)
        self.txtNumberTablets.grid(row=4, column=1)

        self.lblLOT = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="LOT", padx=2, pady=2)
        self.lblLOT.grid(row=5, column=0, sticky=W)
        self.txtLOT = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var6, width=25)
        self.txtLOT.grid(row=5, column=1)

        self.lblIssuedDate = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Issued Date", padx=2, pady=2)
        self.lblIssuedDate.grid(row=6, column=0, sticky=W)
        self.txtIssuedDate = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var7, width=25)
        self.txtIssuedDate.grid(row=6, column=1)

        self.lblExpDate = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Exp Date", padx=2, pady=2)
        self.lblExpDate.grid(row=7, column=0, sticky=W)
        self.txtExpDate = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var8, width=25)
        self.txtExpDate.grid(row=7, column=1)

        self.lblDailyDose = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Daily Dose", padx=2, pady=2)
        self.lblDailyDose.grid(row=8, column=0, sticky=W)
        self.txtDailyDose = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var9, width=25)
        self.txtDailyDose.grid(row=8, column=1)

        self.lblPossibleSideEffects = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Possible Side Effects", padx=2, pady=2)
        self.lblPossibleSideEffects.grid(row=9, column=0, sticky=W)
        self.txtPossibleSideEffects = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var10, width=25)
        self.txtPossibleSideEffects.grid(row=9, column=1)

        self.lblMoreInformation = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="More Information", padx=2, pady=2)
        self.lblMoreInformation.grid(row=10, column=0, sticky=W)
        self.txtMoreInformation = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var11, width=25)
        self.txtMoreInformation.grid(row=10, column=1)

        self.lblBloodPressure = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Blood Pressure", padx=2, pady=2)
        self.lblBloodPressure.grid(row=11, column=0, sticky=W)
        self.txtBloodPressure = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var12, width=25)
        self.txtBloodPressure.grid(row=11, column=1)

        self.lblStorageCondition = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Storage Condition", padx=2, pady=2)
        self.lblStorageCondition.grid(row=12, column=0, sticky=W)
        self.txtStorageCondition = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var13, width=25)
        self.txtStorageCondition.grid(row=12, column=1)

        self.lblPrice = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Price", padx=2, pady=2)
        self.lblPrice.grid(row=13, column=0, sticky=W)
        self.txtPrice = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var14, width=25)
        self.txtPrice.grid(row=13, column=1)

        self.lblExpDate = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Exp Date", padx=2, pady=2)
        self.lblExpDate.grid(row=14, column=0, sticky=W)
        self.txtExpDate = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable=var15, width=25)
        self.txtExpDate.grid(row=14, column=1)

        # Prescription
        self.txtReceipt = Text(DataFrameRIGHT, font=("arial", 12, "bold"), width=56, height=22, padx=2, pady=2)
        self.txtReceipt.grid(row=0, column=0)

        # Buttons
        self.btnTotal = Button(ButtonFrame, text="Total", font=("arial", 12, "bold"), height=2, width=24, bd=4, command=iTotal)
        self.btnTotal.grid(row=0, column=0)

        self.btnReceipt = Button(ButtonFrame, text="Receipt", font=("arial", 12, "bold"), height=2, width=24, bd=4, command=iReceipt)
        self.btnReceipt.grid(row=0, column=1)

        self.btnReset = Button(ButtonFrame, text="Reset", font=("arial", 12, "bold"), height=2, width=24, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=2)

        self.btnExit = Button(ButtonFrame, text="Exit", font=("arial", 12, "bold"), height=2, width=24, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=3)

if __name__ == '__main__':
    root = Tk()
    application = Window1(root)
    root.mainloop()
