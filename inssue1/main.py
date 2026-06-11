from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore
import models, schemas
from database import get_db, engine, Base

# Create the database tables
models.Base.metadata.create_all(engine)

app = FastAPI(title="FastAPI", description="CRUD API using FastAPI and SQLite", version="1.0")


# Create a note
@app.post("/notes",tags=["note"])
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    
    
    new_note = models.Note(title=note.title, content=note.content,user_id=note.user_id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

# get all notes
@app.get("/notes",tags=["note"])
def get_notes(db: Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return notes

# get a note by id
@app.get("/notes/{id}", response_model=schemas.NoteResponse,tags=["note"])
def get_note(id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == id).first()
    if not note:
        raise HTTPException(status_code=404, detail=f"Note with id {id} not found")
    return note



# update a note
@app.put("/notes/{id}", response_model=schemas.NoteResponse,tags=["note"])
def update_note(id: int, note: schemas.NoteUpdate, db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail=f"Note with id {id} not found")
    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note

# delete a note
@app.delete("/notes/{id}", response_model=schemas.NoteResponse,tags=["note"])
def delete_note(id: int, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == id).delete(synchronize_session=True)
    if not note:
        raise HTTPException(status_code=404, detail=f"Note with id {id} not found")
    db.commit()
    return {"message": "Note deleted successfully"}


# Create a user
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get all users
@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


# get a user by id
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    new_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not new_user:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    return new_user