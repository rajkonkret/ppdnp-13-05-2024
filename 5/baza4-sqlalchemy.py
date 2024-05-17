# ORM - Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM)
# – sposób odwzorowania obiektowej architektury systemu informatycznego
# na bazę danych (lub inny element systemu) o relacyjnym charakterze.
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# echo=True - logi z bazy danych
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)

new_use = User(name="Jan Kowalski", age=30)

Session = sessionmaker(bind=engine)
ssesion = Session()

ssesion.add(new_use)  # INSERT INTO users (name, age) VALUES (?, ?)
ssesion.commit()
ssesion.close()

# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
users = ssesion.query(User).all()
for user in users:
    print(user.name)

# Jan Kowalski
# Jan Kowalski
