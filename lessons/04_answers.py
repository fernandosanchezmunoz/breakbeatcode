#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

# add a baseline
end = 9 # unnecessary variable definition
8_measure_song = CIARA_SET_BASSLINE_1 # can't start with a variable
fitMedia(8_measure_song, 1, start, start + 8) # start is not defined, need a different sound variable name

# add an ad lib
adLib = CIARA_SET_TALK_ADLIB_A_1 # sound is not defined
insertMedia(ad_lib, 1, start, start + 1) # insert media takes 3 parameters

# add a beat
clap = CIARA_MELANIN_DRUMBEAT_1
beat1 = "+++-+-+" # beat is all ties and rests, so there shouldn't be sound
makeBeat(beat1, 2, start, clap) # make beat params are sound, track, start, beat. start is still not defined

# print some information about the artist and sounds
artist = ciara # ciara is not a string
sound_count = 3
print("this song is made up of" + count + artist + "sounds") # count is not defined, can't concat str and int, no spaces

finish()

