from typing import List
from api.route_login import get_current_user
from sqlalchemy.orm import Session
from db.model.user import User
from db.model.potion import create_potion, get_potion, get_potions, update_potion, delete_potion
from db.session import get_db
from fastapi import APIRouter, status, HTTPException, Depends
from api.schema.potion import CreatePotion, ShowPotion, UpdatePotion


router = APIRouter()


@router.post("/potion", response_model=ShowPotion, status_code=status.HTTP_201_CREATED)
def _create_potion(potion: CreatePotion, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    potion = create_potion(potion=potion, seller_id=current_user.id, db=db)
    return potion


@router.get("/potion", response_model=List[ShowPotion])
def _get_potions(db: Session = Depends(get_db)):
    potions = get_potions(db=db)
    return potions


@router.get("/potion/{potion_id}", response_model=ShowPotion)
def _get_potion(potion_id: int, db: Session = Depends(get_db)):
    potion = get_potion(potion_id=potion_id, db=db)
    if not potion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Potion with ID {potion_id} does not exist")
    return potion


@router.put("/potion/{potion_id}", response_model=ShowPotion)
def _update_potion(potion_id: int, potion: UpdatePotion, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    potion = update_potion(potion_id=potion_id, potion=potion, seller_id=current_user.id, db=db)
    if not potion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Potion with ID {potion_id} does not exist")
    return potion


@router.delete("/potion/{potion_id}")
def _delete_potion(potion_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not delete_potion(potion_id=potion_id, seller_id=current_user.id, db=db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Potion with ID {potion_id} does not exist")
    return {"status": 0}
