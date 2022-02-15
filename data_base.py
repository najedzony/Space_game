from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# W tym pliku znajdują się funkcje odpowiedzialnie za bazę danych,
# w której przetrzymujemy wszystkie
# wyniki, które uzyskali gracze.


def add_score(name, player_score):

    # Funkcja add_score jest odpowiedzialna za dodanie wyniku
    # do naszej bazy danych.

    Base = declarative_base()
    engine = create_engine("sqlite:///data_base.db", echo=True)
    Session = sessionmaker(bind=engine)

    class Scores(Base):
        __tablename__ = "Scores"

        id = Column(Integer, primary_key=True)
        player_name = Column(String(50), nullable=False)
        score = Column(Integer, nullable=False)

    Base.metadata.create_all(engine)

    sesja = Session()
    scr = Scores(player_name=name, score=player_score)
    sesja.add(scr)
    sesja.commit()


def view_score():

    # Funkcja view_score jest odpowiedzialna za wyświetlanie
    # naszej bazy danych na ekran terminala.

    Base = declarative_base()
    engine = create_engine("sqlite:///data_base.db", echo=True)
    Session = sessionmaker(bind=engine)

    class Scores(Base):
        __tablename__ = "Scores"

        id = Column(Integer, primary_key=True)
        player_name = Column(String(50), nullable=False)
        score = Column(Integer, nullable=False)

    Base.metadata.create_all(engine)

    sesja = Session()
    lista = sesja.query(Scores).all()
    print("Users name    Score")
    for i in lista:
        print(i.player_name + " " + str(i.score))
