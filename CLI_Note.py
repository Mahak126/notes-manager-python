import json
import os
filename="notes.json"

def load_notes(): 
     if os.path.exists(filename):
      with open(filename,"r") as f:
           data=json.load(f)
           return data
     else:
          return [] 
     

     
def save_notes():
   
     with open(filename,"w") as f:
          json.dump(notes,f,indent=4)



def AddNote():
     Title=input("Enter the title:")
     content=input("Enter  the content:")
     d={"Title":Title,"Content":content}
     notes.append(d)
     save_notes()
     print("Notes have been succesfully added.")
       
def ViewNote():
     if not notes:
          print("No Notes available.")
          return
     
     for i,note in enumerate(notes,start=1):
          print(f"{i}. Title:{note['Title']}\n ") 

     try:     
       n=int(input("Enter the no. of  the note:"))
     except ValueError:
          print("please enter valid number.")  
          return 
     if(n>i or n<=0):
          print("Invalid Title no")
          return
     print(notes[n-1]["Content"])

    
def SearchNote():
    if not notes:
          print("No Notes available.")
          return
    t=input("Enter the title of content to be searched:")
    t=t.lower()
    flg=False
    for note in notes:
         if(note["Title"]==t):
              print("found")
              print(f"{note['Title']}\n {note['Content']}\n")
              flg=True
              break
    if not flg:
         print("Not Found.")
               
    
def DeleteNote():
     if not notes:
          print("No Notes available.")
          return
     for i,note in enumerate(notes,start=1):
          print(f"{i}. Title:{note['Title']}\n ") 
     try:     
       n=int(input("Enter the no. of  the note:"))
     except ValueError:
          print("please enter valid number.")  
          return 
     if(n>i or n<=0):
          print("Invalid Title no") 
          return 
     option=input("Are you sure you want to delete the notes?(y/n)").strip().lower()
     if option=='y':
      notes.pop(n-1)  
      save_notes()
      print("Deleted Successfully.")   
     else :
          print("Delete Cancelled.")
          return 

def EditNote():
     if not notes:
          print("No Notes available.")
          return
     for i,note in enumerate(notes,start=1):
          print(f"{i}.Title:{note['Title']}\n")
     try:     
       n=int(input("Enter the no. of  the note:"))
     except ValueError:
          print("please enter valid number.")  
          return 
     if(n>i or n<=0):
          print("Invalid Title no") 
          return  
     else:
          print("1.Edit Title\n2.Edit Content\n3.Edit Both")
          choice=int(input("Enter the Choice:"))
          match choice:
               case 1:
                    new_title=input("Enter New Title:")
                    notes[n-1]["Title"]=new_title
                    print("Title updated successfullly.")

               case 2:
                     new_content=input("Enter updated Content:")
                     notes[n-1]["Content"]=new_content
                     print("content updated successfullly.")

                    
               case 3: 
                    new_title=input("Enter New Title:")
                    new_content=input("Enter updated Content:")
                    notes[n-1]["Title"]=new_title
                    notes[n-1]["Content"]=new_content
                    print("Title  and content updated successfullly.")
               case _:
                    print("INvalid edit choice.")


     


def menu(choice):
            match choice:
                case 1:
                    AddNote()
                case 2:
                    ViewNote()
                case 3:
                    SearchNote()
                case 4:
                    DeleteNote() 
                case 5:
                      EditNote()    
                case _:
                       return "Incorrect Choice."     


def main():
    print("\nWelcome to Notes App \n")
    while 1:
        print(" 1.Add Note\n 2.View Note\n 3.search Note\n 4.Delete Note\n5.Edit Note \n6.Exit\n")
        choice=int(input("Enter your choice:"))
        if choice==6:
            break
        menu(choice)  
     
notes=load_notes()               

main()
