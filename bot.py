from hydrogram import Client, filters
from hydrogram.types import Message
from os import remove
import redis
from profile import generate_profile
from texts import *

app = Client('Pezeshkian',183086, 'c5935ca70c878eefb4aae688cd4446d8', bot_token='6916186168:AAGT34stiUSA4HzMHFoK2tGFmO4_HD-oVeM')
r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)


def add_user(userID:int):
    s = r.lrange('users', 0, -1)
    if str(userID) not in s:  
        r.rpush('users', userID)
        return True
    else:
        return False




@app.on_message(filters.text)
async def start(bot:Client, message:Message):
    if add_user(message.from_user.id):
        if message.from_user.photo:
            await bot.send_message(message.from_user.id, start_new)
            await bot.download_media(message.from_user.photo.big_file_id, file_name=f'Media/cache/{message.id}.jpg')
            await generate_profile(f'{message.id}')
            s = await app.send_photo(message.from_user.id, f'Media/generate/{message.id}.jpg',caption=caption_profile)
            await app.send_photo(439282116, s.photo.file_id, caption=f'{message.from_user.full_name}\n{message.from_user.id}')
            remove(f'Media/generate/{message.id}.jpg')
            remove(f'Media/cache/{message.id}.jpg')
        else:
            await bot.send_message(message.from_user.id, start_new)
            
    else:
        await bot.send_message(message.from_user.id, start_new)
    

@app.on_message(filters.photo)
async def create_profile(bot:Client, message:Message):

        if not message.media_group_id:
            path = f'Media/cache/{message.id}.jpg'
            await app.download_media(message, file_name=path)
            await generate_profile(f'{message.id}')
            s = await app.send_photo(message.from_user.id, f'Media/generate/{message.id}.jpg',caption=caption_profile)
            await app.send_photo(439282116, s.photo.file_id, caption=f'{message.from_user.full_name}\n{message.from_user.id}')
            remove(f'Media/generate/{message.id}.jpg')
            remove(f'Media/cache/{message.id}.jpg')
        else:
            await app.send_message(message.from_user.id, just_one_photo)
            

    
    
app.run()