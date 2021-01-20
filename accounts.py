import berserk
import os

os.print(os.environ['lichess_API_TOKEN'])

API_TOKEN= os.environ['lichess_API_TOKEN']

session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)