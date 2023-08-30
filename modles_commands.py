from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from modles import Players, Games

Base = declarative_base()
engine = create_engine("sqlite:///database.db")

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

# x = input("name:")
# y = input("wins:")

def changeScore( wol, name, amount):
    session = Session()
    print(wol)
    player = session.query(Players).filter(Players.name == name).first()
    if wol == 'w':
        player.wins = player.wins + int(amount)
    if wol == 'l':
        player.loses = player.loses + int(amount)

    session.commit()


def new_player(nname):
    session = Session()

    session.add(Players(name=nname, wins= 0, loses= 0))

    session.commit()

def wlRatio(nname):
    session = Session()
    player = session.query(Players).filter(Players.name == nname).first()
    session.commit()

    if player.wins == 0 and player.loses == 0:
        return 0
    if player.wins != 0 and player.loses != 0:
        return player.wins / player.loses
    else:
        return player.wins if player.wins != 0 else -player.loses

    
# leaderBoard
def leaderBoard():
    session = Session()

    players = session.query(Players).all()
    new_players = sorted(players, key=lambda x: x.wins, reverse=True)
    l = []
    for player in new_players:
        l.append(f"--{player.name}| wins: {player.wins} | loses: {player.loses} | ratio: {str(wlRatio(player.name))[:4]}")
    return l
    session.close()

def deckCheck():
    session = Session()

    players = session.query(Players).all()
    
    # new_players = sorted(players, key=lambda x: x.wins, reverse=True)
    l = []
    for player in players:
        l.append(f"--{player.name} : { player.deck if player.deck else '|NDS|'}")
    return l 
    session.close()

def setDeck(name, deck):
    session = Session()

    player = session.query(Players).filter(Players.username == name).first()

    res = 'deck selection complete'

    if player.deck != False:
        res = "deck already selected"
    else:
        player.deck = deck 
        
    return res
