import contextlib
import os
from tests import IntegrationTest

class TestCreatePoll(IntegrationTest):
    
    def test_db_creation(self):
        _json = self.get_instruments(False)
        
        self.assertEqual(self.instru1_id, _json['instruments'][0]['id'])
        self.assertEqual(self.INSTRU1, _json['instruments'][0]['name'])
        self.assertEqual(self.instru2_id, _json['instruments'][1]['id'])
        self.assertEqual(self.INSTRU2, _json['instruments'][1]['name'])
        self.assertEqual(self.instru3_id, _json['instruments'][2]['id'])
        self.assertEqual(self.INSTRU3, _json['instruments'][2]['name'])
        
    def test_can_create_another_db(self):
        _json = self.create_poll(f'{self.db_name}2', f'/{self.db_name}2', '#ff8b00')
        self.assertEqual(0, _json['id'])

    def test_no_duplicate_poll_id(self):
        rs = self.create_poll(f'{self.db_name}', f'/{self.db_name}2', '#ff8b00', fail=True)
        self.assertEqual(409, rs.status_code)
        
    def tearDown(self):
        with contextlib.suppress(FileNotFoundError): os.remove(f'{self.db_name}2.db')