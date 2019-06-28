from database import CursorFromConnectionPool

class Results:
    def __init__(self, center_number, center_name, walid_votes, id=None):
        self.center_number = center_number
        self.center_name = center_name
        self.walid_votes = walid_votes
        self.id = id

    def __repr__(self):
        return "<Voter {}>".format(self.center_number)

    def save_to_db(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO results ("center_number", "center_name", "walid_voter") VALUES (%s, %s, %s)',
                            (self.center_number, self.center_name, self.walid_votes))

    @classmethod
    def load_from_db(cls, center_number):
        with CursorFromConnectionPool() as cursor:
            cursor.execute('SELECT * FROM results WHERE "center_number"=%s', (center_number,))
            user_data = cursor.fetchone()
            print(user_data)
            return cls(center_number=user_data[1], center_name=user_data[2], walid_votes=user_data[3], id=user_data[0])