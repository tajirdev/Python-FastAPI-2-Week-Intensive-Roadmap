from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import engine,get_db
import schema,models

models.Base.metadata.create_all(engine)

app = FastAPI(title="building a note and user api with fastapi")
#blog for user
@app.post("/post/user",tags=["user"])
def create_user(request:schema.User,db:Session=Depends(get_db)):
    new_user = models.User(username=request.username,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "data": new_user,
        "message": "User created successfully✅"
    }

@app.get("/get_all_user",tags=["user"])
def all_user(db:Session = Depends(get_db)):
    user= db.query(models.User).all()
    return {
        "data": user,
        "message": "all Users retrieved successfully✅"
    }

@app.get("/user_single/{id}",tags=["user"])
def single(id:str,db:Session=Depends(get_db)):
    single_user = db.query(models.User).filter(models.User.id ==id).first()
    if not single_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
    return {
        "data": single_user,
        "message": "User retrieved successfully✅"
    }

@app.put("/user_update/{id}",tags=["user"])
def update_single_user( id:str,request:schema.User,db:Session=Depends(get_db)):
    upgrade = db.query(models.User).filter(models.User.id==id).first()
    if not upgrade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the user with {id} not found")
    upgrade.username= request.username
    upgrade.password = request.password
    
    db.commit()
    db.refresh(upgrade)
    
    return {
        "data": upgrade,
        "message": "User updated successfully✅"
    }
@app.delete("/user_delete/{id}",tags=["user"])    
def delete_user(id:str,db:Session=Depends(get_db)):    
    note = db.query(models.User).filter(models.User.id ==id).delete(synchronize_session= False)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
    return { 
            "message":f"User with id {id} successfully deleted "
        }    

#blog for note
@app.post("/post/notes",tags=["Note"])
def create_note(request:schema.Note,db:Session=Depends(get_db)):
    new_note = models.Note(title=request.title,content=request.content,user_id=request.user_id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    
    return {
        "data": new_note,
        "message": "Note created successfully✅"
    }
@app.get("/get_all",tags=["Note"])
def all_notes(db:Session = Depends(get_db)):
    my_note= db.query(models.Note).all()
    return {
        "data":my_note,
        "message":"successfully retrieved all notes✅"        
    }


@app.get("/get_single/{id}",tags=["Note"])
def single(id:str,db:Session=Depends(get_db)):
    single_note = db.query(models.Note).filter(models.Note.id ==id).first()
    if not single_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"note with id {id} not found")
    return {
        "data": single_note,
        "message": "Note retrieved successfully✅"
    }

@app.put("/notes/{id}",tags=["Note"])
def update( id:str,request:schema.Note,db:Session=Depends(get_db)):
    upgrade = db.query(models.note).filter(models.note.id==id).first()
    if not upgrade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="the note with {id} not found")
    upgrade.title= request.title
    upgrade.content = request.content
    
    db.commit()
    db.refresh(upgrade)
    
    return {
        "data": upgrade,
        "message": "Note updated successfully✅"
    }
@app.delete("/delete/{id}",tags=["Note"])    
def delete_note(id:str,db:Session=Depends(get_db)):    
    note = db.query(models.note).filter(models.note.id ==id).delete(synchronize_session= False)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"note with id {id} not found")
    return { 
            "message":f"note with id {id} successfully deleted "     
        }    
























