from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
import models,schema
from database import engine,get_db

app= FastAPI()

@app.post("/user/register",tags=["User blog"])
def register_user(dotto:schema.User,db:Session=Depends(get_db)):
    register = models.user(
        username = dotto.username,
        email = dotto.email,
        password= dotto.password
    )
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
    register_user= db.query(models.user).filter(models.User.id==id).first()
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
    update_user.passsword = request.passwoed   
    return f"A user with id {id} updated"

@app.delete("/uesrDelete/{id}",tags=["user blog"])
def delete(id,db:Session=Depends(get_db)):
    user = db.query(models.user).filter(models.User.id==id).delete(synchronize_session=True)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"A user with id {id} not found")
    db.commit()
    return f"A user with id {id} successful deleted"