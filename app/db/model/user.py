from db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, Session
from api.schema.user import CreateUser, UpdateUser
from core.hashing import Hasher


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    potions = relationship("Potion", back_populates="seller")


def get_user(db: Session, user_id: int = None, nickname: str = None):
    if nickname:
        user = db.query(User).filter(User.nickname == nickname).first()
    elif user_id:
        user = db.query(User).filter(User.id == user_id).first()
    else:
        return None
    return user


def create_user(user: CreateUser, db: Session):
    user = User(
        nickname=user.nickname,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(user_id: int, user: UpdateUser, db: Session):
    _user = db.query(User).filter(User.id == user_id).first()
    if not _user:
        return None
    _user.email = user.email
    db.add(_user)
    db.commit()
    return _user
