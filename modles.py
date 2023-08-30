from sqlalchemy import create_engine, Column, ForeignKey, String, Integer
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()

class Players(Base):
    __tablename__ = "players"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(15))
    username = Column("username", String(15))
    wins = Column("wins", Integer)
    loses = Column("loses", Integer)
    deck = Column("deck", String(15))

    games = relationship("Games", secondary="player_games", back_populates="players")

    def __repr__(self):
        return f"id:{self.id}, name:{self.name}, username:{self.username} wins:{self.wins},  loses:{self.loses}, deck:{self.deck}"


class Games(Base):
    __tablename__ = "games"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    season = Column("season", Integer)
    winner = Column("winner", String(15))

    players = relationship("Players", secondary="player_games", back_populates="games")

    def __repr__(self):
        return f"({self.id}, {self.season}, {self.winner})"


class PlayerGames(Base):
    __tablename__ = "player_games"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    game_id = Column(Integer, ForeignKey("games.id"))


engine = create_engine("sqlite:///database.db", echo=True)   
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# players = session.query(Players).filter(Players.name == "reed").all()
# for player in players:
#     session.delete(player)

# session.commit()
# players = session.query(Players).all()
# new_players = sorted(players, key=lambda x: x.wins, reverse=True)
# for player in new_players:
#     print(f"-{player.name}| wins:{player.wins} loses:{player.loses}")

# session.close()