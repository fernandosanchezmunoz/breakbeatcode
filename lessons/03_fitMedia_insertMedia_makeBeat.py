#       BreakBeatCode example Day 3 lesson
#       script_name: 03.fitMedia-insertMedia-makeBeat.py 
#       version/date: 20220426
#
#       author: Fernando Sanchez 
#
#       description: 
#       - fitMedia on one track
#       - fitMedia on multiple tracks
#       - makeBeat
#

# Anything after a hashtag is a Comment
# It's helpful as documentation to inform the reader/coder
# Makes the code more readable but it's not executed

# It's also used to execute code "in parts" for debugging
# In these examples, you are expected to gradually uncomment some parts
# Execute "RUN" and play the result, then uncomment the next piece and repeat.

from earsketch import *

init()                              #in latest version this is not required

setTempo(120)                       #set Tempo to 120 Beats Per Minute (BPM)


##### Part 1:
##### A few fitMedia() examples:

beat1 = KHALID_NORM_DRUMBEAT        
beat2 = COMMON_LOVE_DRUMBEAT_1

track = 1
start = 3
end = 16

#The line below adds "KHALID_NORM_DRUMBEAT" to track 1
#starting at position 1 and looping until it ends in position 16
fitMedia( beat1, track, start, end  )   

synth1 = HIPHOP_SYNTHBASS_004
track = 2
start = start + 2 #"start" is now 5

#Add HIPHOP_SYNTHBASS_004 to track 2, loop with start at 5 and end at 16 
#Adding sounds gradually on top of each other works as a build-up
fitMedia( synth1, track, start, end  )

vocal1 = ENTREP_VOX_JAYZ_BUILD
track = 3
start = start + 2 #"start" is now 7

#Uncomment the code below to...
#Add ENTREP_VOX_JAYZ_BUILD to track 3, loop with start at 7 and end at 16
#fitMedia( vocal1, track, start, end  )

#### Part 2
#### A few insertMedia() examples:

track = 4
start = 9

vocal_drop_1 = YG_HIP_HOP_VOX_1
vocal_drop_2 = YG_TRAP_VOX_1

#Uncomment the code below to...
#Add YG_HIP_HOP_VOX_1 just once (no loop) on track 4 starting at 9
#insertMedia(vocal_drop_1, track, start )

#start = start + 2 #"start" is now 11

#Uncomment the code below to...
#Add YG_HIP_HOP_VOX_1 once again on track 4, starting at 11
#Repeating the sound periodically after a certain time of silence is common
#Here we're doing it manually, we will see how to do it automatically later...
#insertMedia(vocal_drop_1, track, start )

#### Part 3
#### A few makeBeat() examples:

track=5
start=6

#Create a pattern to repeat a sound as a "remix"
#my_beat = "0++++++++++++++"
#my_beat = "0+++0+++++0++++"

#Call makeBeat() with a sound (vocal_drop_1 is YG_HIP_HOP_VOX_1)
#on a track (track is 5), on a start point (1)
#makeBeat(vocal_drop_1, track, start, my_beat)

finish()

