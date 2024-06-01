# yoii - ishikki

from GramDB import GramDB
import asyncio


CACHE_TABLE = {
  "info_gramdb": {
    "name": "ishikki", "password": "v_143", "telegram_id": 6282920
  },
  "test_table": [20],
  "bio_table": [21, 22]
}

CACHE_DATA = {
  '20': {'_m_id': '20', '_table_': 'test_table', 'username': 'ishikki_akabane', 'bio': "I'm natsu dragneel"},
  '21': {'_m_id': '21', '_table_': 'bio_table', 'id': 1234567891, 'bio': "I'm alpha"},
  '22': {'_m_id': '22', '_table_': 'bio_table', 'id': 1234567892, 'bio': "I'm cat"}
}

sample_efficitiantdb = {
  'bio_table': {
    '1234567891': {
      '_id': 1234567891, '_m_id': '21', 'bio': "I'm alpha"
    },
    '1234567892': {
      '_id': 1234567892, '_m_id': '22', 'bio': "I'm cat"
    }
  },
  'test_table': {
    '638928387': {
      '_id': 638928387, '_m_id': '20', 'bio': "I'm natsu dragneel", 'username': 'ishikki_akabane'
    }
  }
}


async def aa():
  db = GramDB("https://blue-api.vercel.app/database?client=ishikki@xyz242.gramdb")
  
  bbbbb = await db.insert("testt_table", {'bio': "I'm alpha male", "username": "alphamale"})
  print(bbbbb)
  print("hmm")
  d = await db.fetch_all()
  for m, n in d.items():
    print("\n", m)
    for o, p in n.items():
      print(p)
  db.close()
    
asyncio.run(aa())

print("ending...")
