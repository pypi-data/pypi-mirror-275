import sqlite3

from popoll_backend.model.db.instrument import Instrument
from popoll_backend.query import PollQuery


class CreateInstrument(PollQuery):
    
    name: str
    rank: int
    
    instrument_id: int
    
    def __init__(self, poll: str, name: str, rank: int):
        super().__init__(poll)
        self.name = name
        self.rank = rank
       
    def process(self, cursor: sqlite3.Cursor) -> None:
        self.instrument_id = cursor.execute('INSERT INTO instruments.instruments(name, rank) VALUES (?,?)', (self.name, self.rank)).lastrowid
    
    def buildResponse(self, cursor: sqlite3.Cursor) -> Instrument:
        return self.fetchlast(cursor.execute('SELECT * FROM instruments.instruments WHERE id=?', (self.id,)), Instrument)
