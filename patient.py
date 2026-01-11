
class patient_manager():    
    def patient_saving_module(self):
        import os
        self.name = str(input("Please Input your full name\n-"))
        self.age = int(input("Please Mention your age\n-"))
        self.weight= int(input("Please describe your weight in Kgs\n-"))
        self.condition = input("Please describe your condition\n-")
        self.insur_status= str(input("Do you have insurance?(yes/no)-\t"))
        self.insur_type = str(input("What Type Insurace you have? (Government/Private)-\t"))
        self.previous_doc= str(input("Name of the previous doctor you treated (type none if not treated)\n-")) 
        #file_exists=os.path.exist("patient.csv")
        #if not file_exists:
            #self.create_db(self)     
        #else:
            #self.write_db(self) 
        self.write_db()     

    def write_db(self):
        import sqlite3
        conn= sqlite3.connect("Input Database name here")
        cursor= conn.cursor
        cursor.execute("Insert Sql query here",(self.name,self.age,self.weight,self.condition,self.insur_status,self.insur_type,self.previous_doc))
        conn.commit()
        conn.close()
    
    def create_db(self):
        import sqlite3
        conn=sqlite3.connect
    
    
    
    
    
    
    
    
    #def write_new_file(self):
        #import csv
        #with open("patient.csv",mode="w",newline="") as file:
                #writer = csv.writer(file)
               #writer.writerow(["Name","Age","Weight(kg)","Condition","Insurance Status","Insurance type","Previous Doc"])          
                #writer.writerow([self.name,self.age,self.weight,self.condition,self.insur_status,self.insur_type,self.previous_doc])
    
    #def append_file(self):
        #import csv
        #with open("patient.csv",mode="a",newline="") as file:
                #writer = csv.writer(file)          
                #writer.writerow([self.name,self.age,self.weight,self.condition,self.insur_status,self.insur_type,self.previous_doc])
         
