from db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from api.schema.potion import CreatePotion, UpdatePotion


class Potion(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    cost = Column(Integer, default=0)
    is_active = Column(Boolean(), default=True)
    seller_id = Column(Integer, ForeignKey("user.id"))
    seller = relationship("User", back_populates="potions")


def create_potion(potion: CreatePotion, seller_id: int, db: Session):
    potion = Potion(
        name=potion.name,
        cost=potion.cost,
        is_active=False,
        seller_id=seller_id
    )
    db.add(potion)
    db.commit()
    db.refresh(potion)
    return potion


def get_potion(potion_id, db: Session):
    potion = db.query(Potion).filter(Potion.id == potion_id).first()
    return potion


def get_potions(db: Session):
    potions = db.query(Potion).filter(Potion.is_active == True).all()
    return potions


def update_potion(potion_id: int, potion: UpdatePotion, seller_id: int, db: Session):
    _potion = db.query(Potion).filter((Potion.id == potion_id, Potion.seller_id == seller_id)).first()
    if not _potion:
        return None
    _potion.name = potion.name
    _potion.cost = potion.cost
    _potion.is_active = potion.is_active
    db.add(_potion)
    db.commit()
    return _potion


def delete_potion(potion_id: int, seller_id: int, db: Session):
    _potion = db.query(Potion).filter((Potion.isd == potion_id, Potion.seller_id == seller_id)).first()
    if not _potion:
        return False
    db.delete(_potion)
    db.commit()
    return True
