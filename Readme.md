## Volume control

Imagine you are required to regularly spend time with people from different backgrounds. Your shared space has 1 sound system connected via Sonos, which is supposed to help you enjoy spending time together. Sonos allows anyone to make playlists, add songs to current play queue and control playback options like volume. Some people's definition of acceptable music volume might be much higher than your pain threshold. They might also be hard to reason with and persistent in turning the volume up, even after you turn it down. Enter **vol_control** to save your life. You need to input the frequency and the maximum volume you are prepared to tolerate. It will connect to your Sonos system, check the volume every given number of seconds and correct it to acceptable. Thus it should defeat even the most persistent lovers of loud music by virtue of being a computer programme that doesn't get bored of doing the same task. 


## Requirements

    * Sonos speaker system connected to the network
    * Machine connected to the same network
    * 0.12+ version of the [SoCo - Sonos Python API](https://github.com/SoCo/SoCo)
    


## Gotchas

### Use Windows - install SoCo from source

If deploying on Windows, it's best to install from source of the master branch. 0.12 release available on PyPy throws a socket error on Windows. It has been fixed in a later commit and until 0.13 is released (discussion ongoing as of 14/11/2017) on PyPy, it's best to install from source.

## Assumes only 1 Sonos system on the network

The current version of the code, assumes only system will be found when `soco.discover` is run. Support for controlling multiple systems will come in future releases. 
