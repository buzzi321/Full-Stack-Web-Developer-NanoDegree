from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

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


# Create dummy user
User1 = User(name="Dummy", email="dummy@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


User2 = User(name="Sekhar Gogineni", email="buzzi321@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()

# items for livingroom
category1 = Category(user_id=2, name="LIVING ROOM")

session.add(category1)
session.commit()

Item2 = Item(user_id=1, itemname="KALLAX shelf unit", description="Storage or display. Your shelving, your choice.",
                     price="$64.99", category=category1)

session.add(Item2)
session.commit()


Item1 = Item(user_id=2, itemname="EKTORP Sectional 3-seat", description="The comfortable sofa for all seasons",
                     price="$499", category=category1)

session.add(Item1)
session.commit()

# items for DINING ROOM
category2 = Category(user_id=2, name="DINING ROOM")

session.add(category2)
session.commit()


Item1 = Item(user_id=1, itemname="STEFAN chair", description="Sitting pretty, from appetizer to dessert",
                     price="$25.00", category=category2)

session.add(Item1)
session.commit()

Item2 = Item(user_id=2, itemname="STORNAS Extendable table", description="EVERY DAY CAN FEEL LIKE A SPECIAL OCCASION",
                     price="$299.00", category=category2)

session.add(Item2)
session.commit()

# items for KITCHEN
category1 = Category(user_id=2, name="KITCHEN")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, itemname="FOLJSAM oven dish", description="Straight from the oven to your table",
                     price="$2.99", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=2, itemname="SEKTION Kitchen", description="with HAGGEBY White doors, drawer fronts and FORVARA Drawers",
                     price="$569.00", category=category1)

session.add(Item2)
session.commit()

# items for BEDROOM
category1 = Category(user_id=2, name="BEDROOM")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, itemname="HYLLE Queen pillow", description="Polyester fiber filling. Imported.",
                     price="$2.99", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=2, itemname="HAUGSVAR Queen spring mattress", description="The individually wrapped pocket springs in HAUGSVAR work independently and closely follow your body.",
                     price="$399.00", category=category1)

session.add(Item2)
session.commit()


# items for BATHROOM
category1 = Category(user_id=2, name="BATHROOM")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, itemname="VESKEN", description="Shelving in a flash",
                     price="$9.95", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=2, itemname="HEMNES", description="Cabinet with sink",
                     price="$349.00", category=category1)

session.add(Item2)
session.commit()


# items for PRODUCTS
category1 = Category(user_id=2, name="PRODUCTS")

session.add(category1)
session.commit()


Item1 = Item(user_id=1, itemname="BESTA", description="storage system has been keeping everything from personal knick-knacks and memories.",
                     price="$494.00", category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=2, itemname="KIVIK", description="Our KIVIK seating family has been hugging behinds for over a decade",
                     price="$250", category=category1)

session.add(Item2)
session.commit()



print "added items!"
