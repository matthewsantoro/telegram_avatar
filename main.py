from telethon.sync import TelegramClient, events
from config import *
from telethon import TelegramClient
from config import *
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from generate_image import *
from weather import *
from utils import *

with TelegramClient('name', TELEGRAM_API_ID, API_HASH) as client:
    prev_update_time = ""
    while True:
        if time_has_changed(prev_update_time):
            prev_update_time = convert_time_to_string(datetime.now())
            data = get_current_weather()
            data['dt'] = convert_time_to_string(datetime.now())
            generate_image(data)
            client(DeletePhotosRequest(client.get_profile_photos('me')))
            file = client.upload_file(f"images/result.png")
            client(UploadProfilePhotoRequest(file))

client.run_until_disconnected()
