from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .category import Category  

class Expense(Base):
    __tablename__ = 'expense'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    amount = Column(Float)
    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship('Category', backref='expenses')
