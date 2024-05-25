import os
import getpass

username = getpass.getuser()
print(username)

def chdir_bachelor(username):
      os.chdir(f"C:/Users/{username}/Desktop/bachelor")

def chdir_data(username):
      os.chdir(f"C:/Users/{username}/Desktop/bachelor/data")

def chdir_sql(username):
      if username == "lukas":
            os.chdir("E:\sql")
      if username=="Lukas":
            os.chdir("C:\sql")
      
      

def chdir_pdf(username):
      os.chdir(f"C:/Users/{username}/Desktop/bachelor/pdf") 

def chdir_auth(username):
      os.chdir(f"C:/Users/{username}/Desktop/bachelor/auth")    

def chdir_txt(username):
      os.chdir(f"C:/Users/{username}/Desktop/bachelor/txt")    

def chdir_fig(username):
      os.chdir(f"C:/Users/{username}/Desktop/bachelor/data/figures")          

def switch_dir(type):
      if type =="pdf":
            chdir_pdf()
      if type == "json":
            chdir_data()