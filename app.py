import database
from voter import Voter
import json
from results import Results
database.Database.initialise(database="elections", user="faisal13", password="1314ff@", host="localhost")

# voter = Voter('Faisal', 'Rahil', 'Algilani')
# voter1 = Voter('Faisal1', 'Rahil1', 'Algilani1')
v1t = Voter.load_from_db_by_name('Faisal111111')

# r = requests.get('https://tiny.cc/hnecdata')
# print(r.status_code)

with open('results.json','r') as f:
    data=json.load(f)
    for p in data:
        result1 = Results(str(p['Center Number']), p['Center Name'], p['Valid Votes'], p['id'])
        result1.save_to_db()
result1 = Results.load_from_db('31001')
