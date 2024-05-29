import glob
import sqlite3

from popoll_backend.model import Payload
from popoll_backend.model.payload.polls import Poll, Polls
from popoll_backend.query import Query


class GetAllSession(Query):
    
    id: int
    
    def __init__(self, id: str):
        self.id = id

    def run(self) -> Payload:
        polls: Polls = Polls()
        for db in sorted(glob.glob('*.db')):
            with sqlite3.connect(db) as connection:
                cursor: sqlite3.Cursor = connection.cursor()
                if cursor.execute('SELECT COUNT(*) FROM sessions WHERE session_id=?', (self.id,)).fetchone()[0] > 0:
                    polls.add(Poll(db[0:-3], cursor.execute('SELECT name FROM options').fetchone()[0]))
        return polls        
        
    