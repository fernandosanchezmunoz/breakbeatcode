#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

# add a baseline
end = 9
8_measure_song = CIARA_SET_BASSLINE_1
fitMedia(8_measure_song, 1, start, start + 8)

# add an ad lib
adLib = CIARA_SET_TALK_ADLIB_A_1
insertMedia(ad_lib, 1, start, start + 1)

# add a beat
clap = CIARA_MELANIN_DRUMBEAT_1
beat1 = "+++0+0+"
makeBeat(beat1, 2, start, clap)

# print some information about the artist and sounds
artist = ciara
sound_count = 3
print("this song is made up of" + count + artist + "sounds")

finish()

