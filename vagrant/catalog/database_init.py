from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()

category1 = Category(name='Vegetables', id=0)
session.add(category1)
session.commit()

category2 = Category(name='Fruits', id=1)
session.add(category2)
session.commit()

category3 = Category(name='Flowers', id=2)
session.add(category3)
session.commit()

item1 = Items(id=0, name='Tomatoes',
              description='Tomatoes are the best vegetables for salad',
              category='Vegetables')
session.add(item1)
session.commit()

item2 = Items(id=1, name='Cucumbers',
              description='Cucumbers are the vegetables with the most water',
              category='Vegetables')
session.add(item2)
session.commit()

item3 = Items(id=2, name='Bananas',
              description='Bananas have got a lot of energy',
              category='Fruits')
session.add(item3)
session.commit()

item4 = Items(id=3,
              name='Watermellon',
              description='Watermellons are the fruits'
                          ' that have the most water',
              category='Fruits')
session.add(item4)
session.commit()

item5 = Items(id=4, name='Roses',
              description='Roses are romantic flowers',
              category='Flowers')
session.add(item5)
session.commit()

item5 = Items(id=5, name='Sunflower',
              description='Sunflower come out in Spring',
              category='Flowers')
session.add(item5)
session.commit()
