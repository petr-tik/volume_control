import soco
import time


ACCEPTABLE_VOLUME = 15  # int value between 0 ... 100

# in case, others persistently try to increase the volume, decrease time period
EVERY_SECONDS = 3


def keep_volume(vol_level, time_period, speaker):
    while True:
        if speaker.volume > vol_level:
            print("Lowering volume from {} to {}".format(
                speaker.volume, vol_level))
            speaker.volume = vol_level
        time.sleep(time_period)


if __name__ == '__main__':
    speakers = soco.discover()
    speaker = speakers.pop()
    print("Found: {}".format(speaker))
    keep_volume(ACCEPTABLE_VOLUME, EVERY_SECONDS, speaker)
