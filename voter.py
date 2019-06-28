from database import CursorFromConnectionPool

class Voter:
    def __init__(self, first_name, third_name, family_name,
                 # date_birth,place_birth,
                 # governorate, province, district, city, quarter, status, type,
                 # national_id_no, family_book_no, second_name,
                 id):
        self.first_name = first_name
        self.third_name = third_name
        self.family_name = family_name
        # self.date_birth = date_birth
        # self.place_birth = place_birth
        # self.governorate = governorate
        # self.province = province
        # self.district = district
        # self.city = city
        # self.quarter = quarter
        # self.status = status
        # self.type = type
        # self.national_id_no = national_id_no
        # self.family_book_no = family_book_no
        # self.second_name = second_name
        self.id = id

    def __repr__(self):
        return "<User {} -- {} -- {} >".format(self.first_name, self.third_name, self.family_name)

    def save_to_db(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO voter (first_name, third_name, family_name ) VALUES (%s, %s, %s)',
                            (self.first_name, self.third_name, self.family_name))

    @classmethod
    def load_from_db_by_name(cls, first_name):
        with CursorFromConnectionPool() as cursor:
            # Note the (first_name,) to make it a tuple!
            cursor.execute('SELECT * FROM voter where id=%s', (1,))
            voter_data = cursor.fetchone()
            print(voter_data)
            return cls(first_name=voter_data[1], third_name=voter_data[2], family_name=voter_data[3],id=voter_data[0])