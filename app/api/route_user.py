from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from api.route_login import get_current_user
from api.schema.user import CreateUser, GetUser, UpdateUser
from db.model.user import User, create_user, update_user, get_user


router = APIRouter()


@router.post("/user", response_model=GetUser, status_code=status.HTTP_201_CREATED)
def _create_user(user: CreateUser, db: Session = Depends(get_db)):
    user = create_user(user=user, db=db)
    return user


@router.put("/user", response_model=UpdateUser)
def _update_user(user: UpdateUser, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = update_user(user_id=current_user.id, user=user, db=db)
    return user


@router.put("/user", response_model=GetUser)
def _get_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = get_user(user_id=current_user.id, db=db)
    return user
