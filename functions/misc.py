from typing import overload

import spotipy


class MiscFunctions:
    def __init__(self, sp: spotipy.Spotify):
        self.sp = sp

    def get_device_list(self) -> list:
        try:
            return self.sp.devices()["devices"]
        except:
            print("[Error] Cannot get list of devices")
            return None

    def set_device(self, id_: str):
        try:
            self.sp.transfer_playback(id_, True)
        except:
            None

    def set_default_device(self):
        try:
            device_id = self.sp.devices()["devices"][0]["id"]
            self.sp.transfer_playback(device_id, False)
        except:
            print("[Error] could not select default device.")

    def set_volume(self, value: int):
        try:
            int_ = int(value)
            if 0 <= int_ <= 100:
                self.sp.volume(int_, self.current_device_id)
        except:
            print("[Error] Invalid volume value. Valid command example: 'volume 20'")
