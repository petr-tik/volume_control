import soco
import time

def keep_volume(vol_level, time_period, speaker):
        while True:
                if speaker.volume > vol_level:
                        print("Lowering volume from {} to {}".format(speaker.volume, vol_level))
                        speaker.volume = vol_level
                time.sleep(time_period)


if __name__ == '__main__':
        speakers = soco.discover()
        speaker = speakers.pop()
        print("Found: {}".format(speaker))
        keep_volume(15, 3, speaker)
