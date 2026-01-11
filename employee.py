class employeeterminal():
    def info_patient_main(self):
        import csv
        import os
        choice=int(input("***EMPLOYEE TERMINAL***\n1) View the most recent Patient\n2) View a specific Patient's Record\n Specify your choice Number(1/2):- "))
        match choice:
                     
        

    
    
    

    
    def fetch_all():
        import sqlite3
        conn= sqlite3.connect("db name")
        cursor=conn.sqlite3
        cursor.execute("SQL Query to get whole table")
        rows= cursor.fetchall()
        for row in rows :
             print(rows)
        conn.close
             
    def fetch_sorted_ascending():
        import sqlite3
        conn=sqlite3.connect()
        cursor=conn.sqlite3("db")
        #variable_selected=variable selected by the employee for displaying 
        query="SQL Query to sort the following variable (Ascending) {variable_selected}"
        cursor.execute()     
        rows=cursor.fetchall()
        for row in rows:
          print(rows)
        conn.close

    def fetch_sorted_descending():
        import sqlite3
        conn=sqlite3.connect()
        cursor=conn.sqlite3("db")
        #variable_selected=variable selected by the employee for displaying 
        query="SQL Query to sort the following variable (Descending) {variable_selected}"
        cursor.execute(query)     
        rows=cursor.fetchall()
        for row in rows:
          print(rows)
        conn.close
    
    def fetch_single_col():
        import sqlite3
        conn=sqlite3.connect()
        cursor=conn.sqlite3("db")
        #variable_selected=variable selected by the employee for displaying
        query="SQL Query to fetch the following variable column {variable_selected}"
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
          print(rows)
        conn.close

    def var_under_limit():
        import sqlite3
        conn=sqlite3.connect()
        cursor=conn.sqlite3("db")
        #variable_selected=variable selected by the employee for displaying
        #Under_limit= Limit under variable (ex age under __ yrs )
        query="SQL Query to fetch the following variable column {variable_selected} < ?"
        (Under_limit,)
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
          print(rows)
        conn.close

    def print_specific():
        import sqlite3
        conn=sqlite3.connect()
        cursor=conn.sqlite3("db")
        #name_selected=variable selected by the employee for displaying 
        query="SQL Query to show the records of the following  {name_selected}"
        cursor.execute(query)     
        rows=cursor.fetchall()
        for row in rows:
          print(rows)
        conn.close


    def var_over_limit():
        import sqlite3
        conn=sqlite3.connect()
        cursor=conn.sqlite3("db")
        #variable_selected=variable selected by the employee for displaying
        #Under_limit= Limit over variable (ex age over __ yrs )
        query="SQL Query to fetch the following variable column {variable_selected} > ?"
        (Under_limit,)
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
          print(rows)
        conn.close
                