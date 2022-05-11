#		python code
#		script_name: chillout_full_beat
#
#		author: Bad Placebo
#		description: Chillout Hip Hop Pattern from Attack Magazine
#       url: https://www.attackmagazine.com/technique/beat-dissected/chillout-dusty-hip-hop/
#

from earsketch import *

init()
setTempo(84)

# Drum Kit Sounds
kick = IRCA_OS_KICK
snare = OS_SNARE03
clap = OS_CLAP02
closed_hat = OS_CLOSEDHAT06
open_hat = OS_OPENHAT06
conga = IRCA_OS_CONGA_TAPAO
tom = OS_LOWTOM04

# Drum Kit Patterns
kick_pattern = [1,8,9,11,16]
snare_pattern = [5,13]
closed_hat_pattern = [1,3,5,7,9,11,13,16]
open_hat_pattern = [15]
conga_pattern = [1,2,4,5]
tom_pattern = [14,15]

def add_pattern(sound,start_track,measure,pattern):
    track = start_track
    for pos in range(len(pattern)):
        insertMedia(sound,track,measure + (pattern[pos]-1)/16.0)
        track = track + 1
    return track
    
start_measure = 1

#Beats
while start_measure < 8: 
    track = 1
    track = add_pattern(kick,track,start_measure,kick_pattern)
    track = add_pattern(snare,track,start_measure,snare_pattern)
    track = add_pattern(clap,track,start_measure,snare_pattern)
    track = add_pattern(closed_hat,track,start_measure,closed_hat_pattern)
    track = add_pattern(open_hat,track,start_measure,open_hat_pattern)
    track = add_pattern(conga,track,start_measure,conga_pattern)
    track = add_pattern(tom,track,start_measure,tom_pattern)
    #start_measure = start_measure + 1
    start_measure += 1

finish()

