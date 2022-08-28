from pypresence import Presence
from yandex_music import Client
import time

#Yandex token. You can get it from "get_yandex_token.py"
TOKEN = "Your TOKEN HERE"

# This is Aplications ID
client_id = Your APPLICATION ID HERE
  
# Inicalize the RPC  
RPC = Presence(client_id=client_id)
RPC.connect()

# Inicalize Yandex Music API
client = Client(TOKEN).init()

# Work until the program doesnt stoped
while True:  
    queues = client.queues_list()
    last_queue = client.queue(queues[0].id)
    last_track_id = last_queue.get_current_track()
    last_track = last_track_id.fetch_track()
    artists = ', '.join(last_track.artists_name())
    title = last_track.title
    track_link = f"https://music.yandex.ru/album/{last_track['albums'][0]['id']}/track/{last_track['id']}/"
    image_link="https://" + last_track.cover_uri.replace("%%", "1000x1000")
    btns = [
            { 
        "label": "Слушать Трек",
        "url": track_link
            }
    ]

    RPC.update(
        details="Слушает: " + title,
        state="Исполнитель: " + artists,
        large_image=image_link,
        small_image="Link for small image if you want",
        large_text="Your Text Here",
        small_text="Your Text Here",
        buttons=btns  
    )
    
    time.sleep(1) # update the rpc status (in seconds), default: 1 
