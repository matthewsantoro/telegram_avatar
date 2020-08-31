from telethon import TelegramClient, sync
from config import *
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
from generate_image import *
from weather import *
from utils import *


client = TelegramClient('avatar', api_id, api_hash)
client.start()

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



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
