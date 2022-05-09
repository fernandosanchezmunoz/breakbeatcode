#       BreakBeatCode example Day 5 lesson
#       script_name: 05.loops_1.py 
#       version/date: 20220510
#
#       author: Fernando Sanchez 
#
#       description: 
#       - show a repetitive task using insetMedia() with a vocal drop as an example
#       - show the equivalent loop
#

from earsketch import *

init()                              #in latest version this is not required

setTempo(120)                       #set Tempo to 120 Beats Per Minute (BPM)


### Start with a beat, a bass and a vocal

beat1 = COMMON_LOVE_DRUMBEAT_1
#beat2 = KHALID_NORM_DRUMBEAT        

track = 1
start = 1
end = 20

fitMedia( beat1, track, start, end  )   

synth1 = HIPHOP_SYNTHBASS_004
track = 2
start = start + 2 #"start" is now 5

fitMedia( synth1, track, start, end  )

vocal1 = ENTREP_VOX_JAYZ_BUILD
track = 3
start = start + 2 #"start" is now 7

fitMedia( vocal1, track, start, end  )

#### Now I'd like to insert a vocal drop

track = 4
start = 9

vocal_drop_1 = YG_HIP_HOP_VOX_1
#vocal_drop_2 = YG_TRAP_VOX_1

insertMedia(vocal_drop_1, track, start )

# Now I'd like to inser this every two measures
#start = start + 2 #"start" is now 11
#insertMedia(vocal_drop_1, track, start )

#start = start + 2 #"start" is now 13
#insertMedia(vocal_drop_1, track, start )

#start = start + 2 #"start" is now 15
#insertMedia(vocal_drop_1, track, start )

#start = start + 2 #"start" is now 17
#insertMedia(vocal_drop_1, track, start )

#start = start + 2 #"start" is now 19
#insertMedia(vocal_drop_1, track, start )

##How can we make this with a simple loop?






#while start < end:
#	start = start + 2 #"start" increases two every pass of the loop
#	insertMedia(vocal_drop_1, track, start )

finish()

