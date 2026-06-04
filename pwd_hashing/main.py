from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
import models,schema
from hashing import hash
from database import engine,get_db

models.Base.metadata.create_all(bind=engine)

app= FastAPI()

@app.post("/user/register",tags=["user blog"])
def register_user(dotto:schema.User,db:Session=Depends(get_db)):
    hashed_password=hash.hash_password(dotto.password)
    
    register = models.User(
        username = dotto.username,
        email = dotto.email,
        password= hashed_password
    )
    if register.username == dotto.username:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="a user name already exist")
    if register.email== dotto.email:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="an email already exist")
    db.add(register)
    db.add(register)
    db.commit()
    db.refresh(register)
    
    return register

@app.get('/User',tags=["user blog"])
def get_all_registered(db:Session=Depends(get_db)):
    registered= db.query(models.User).all()
    return registered

@app.get("/registered/{id}",tags=["user blog"])
def get_specific_registered(id,db:Session=Depends(get_db)):
    register_user= db.query(models.User).filter(models.User.id==id).first()
    if not register_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"A user with id {id} not found")
    return register_user

@app.put("/updateUser/{id}",tags=["user blog"])
def update(id, request:schema.User,db:Session=Depends(get_db)):
    update_user= db.query(models.User).filter(models.User.id ==id).first()
    if not update_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"A user with id {id} not found")
    update_user.username = request.username
    update_user.email = request.email
    update_user.passsword = request.password  
    db.commit()
    db.refresh(update_user) 
    return f"A user with id {id} updated"

@app.delete("/uesrDelete/{id}",tags=["user blog"])
def delete(id,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).delete(synchronize_session=False)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"A user with id {id} not found")
    db.commit()
    return f"A user with id {id} successful deleted"