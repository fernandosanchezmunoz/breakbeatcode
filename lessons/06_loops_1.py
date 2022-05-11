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

my_tempo = readInput("What tempo would you like to use?") #readInput returns a string
# TODO: Add input validation to ensure mytempo is a number
my_tempo_int = int(my_tempo)
setTempo(my_tempo_int)                       #set Tempo to 120 Beats Per Minute (BPM)


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
insert_point = 7

vocal_drop_1 = YG_HIP_HOP_VOX_1
#vocal_drop_2 = YG_TRAP_VOX_1

insertMedia(vocal_drop_1, track, insert_point )

# Now I'd like to inser this every two measures
while ( insert_point < end ):
    insertMedia(vocal_drop_1, track, insert_point )
    insert_point = insert_point + 2 #"insert_point" is increased in every loop pass

finish()

