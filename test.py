# yoii - ishikki

from GramDB import GramDB
import asyncio


CACHE_TABLE = {
  "info_gramdb": {
    "name": "ishikki", "password": "v_143", "telegram_id": 6282920
  },
  "bio_table": [21, 22]
}

CACHE_DATA = {
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
  }
}


async def aa():
  db = GramDB("https://blue-api.vercel.app/database?client=ishikki@xyz242.gramdb")

  while True:
    try:
      command = input("Enter a command")
      if command == "end":
        break
      result = eval(command)
      if asyncio.iscoroutine(result):
        result = await result
      print(result)
    except Exception as e:
      print(e)
  db.close()
    
asyncio.run(aa())

print("ending...")
