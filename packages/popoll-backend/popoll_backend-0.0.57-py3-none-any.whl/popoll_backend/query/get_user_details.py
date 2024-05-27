import sqlite3

from popoll_backend.model.db.answer import Answer
from popoll_backend.model.db.date import Date
from popoll_backend.model.db.user import User
from popoll_backend.model.payload.user_with_instruments import UserWithInstruments
from popoll_backend.model.payload.user_details import UserDetails
from popoll_backend.query import Query


class GetUserDetails(Query):
    
    id: int
    
    def __init__(self, poll: str, id: int):
        super().__init__(poll)
        self.id = id
    
    def process(self, cursor: sqlite3.Cursor) -> None:
        pass
        
    def buildResponse(self, cursor: sqlite3.Cursor) -> UserWithInstruments:
        return UserDetails(
            user=self.fetchlast(cursor.execute('SELECT * FROM users WHERE id=?', (self.id,)), User), 
            answers=self.fetchall(cursor.execute('SELECT * FROM answers WHERE user_id=?', (self.id,)), Answer),
            dates=self.fetchall(cursor.execute('SELECT * FROM dates ORDER BY date, time'), Date)
        )
        
        
        