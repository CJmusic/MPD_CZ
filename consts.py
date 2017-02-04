#Christopher Zaworski, 2017

'''
This file is for setting what midi controls to use for each feature 
with the control script. Currently this is the setup I use for my Akai 
MPD 26.

It can easily be adapted to use with other MIDI controllers: 

I recommended that you download a program to monitor incoming midi messages, 
such as MIDI Monitor for OS X, so that you can know what MIDI messages your 
controller is sending and then simply change the values here to correspond 
to the midi note and CC number you want to assign to each control.
'''

CHANNEL = 1 #I have this set to midi channel 2 (which corresponds to 1
			#in python since python counts from zero) on my MPD, that way
			#I have all midi 128 notes available to me on channel 1 (0 in python)
			#for playing instruments


##RED BOX Control
GRIDSIZE = [4,4] ##the red box grid size(does not have to be square)

LAUNCH_BUTTONS =[[64,65,66,67],
				[60,61,62,63],
				[56,57,58,59],
				[52,53,54,55]] 
				##these are the midi note values that correspond to the scene launch 
				#buttons withing the SessionGrid. You will need to add more values or 
				#delete values coressponding to the size of the Grid you set.\

SCENE_BUTTONS = [72,73,74,75]

##NAV Controls, move the red box in live
DOWN_BUTTON =48
UP_BUTTON = 49
LEFT_BUTTON =50
RIGHT_BUTTON = 51


##MIXER Controls 
#The below mixer controls correspond to the RedBox in Live. Again, if you 
#change the grid size you will need to update these lists accordingly. 


MUTE_BUTTONS = [44,45,46,47]
ARM_BUTTONS = [36,37,38,39]
SOLO_BUTTONS = [40,41,42,43]

MIX_FADERS = [12,13,14,15] ##these correspond to the CC message number for each fader


TRACK_SELECTS = [80,81,82,83]
TRACK_STOPS = [68,69,70,71]

##DEVICE Controls 
#use these in combination with the track select buttons to quickly navigate to
#and control devices

NEXT_DEVICE = 77
PREVIOUS_DEVICE = 76

DEVICE_ON = 79 
DEVICE_LOCK = 78 #Locks your macro controls to current device regardless of where
				 #you are in your session

#MACRO Controls 
#these correspond to the knobs and Sliders you want to use to for the first 8 
#controls in any ableton device (these also correspond to the 8 macro knobs in 
#an instrument or effects rack)


MACRO_CONTROLS = [0,1,2,3,4,5,6,7]

#TRANSPORT Controls 
#channels may be different from the channel you specify above

PLAY_BUTTON = 118
STOP_BUTTON = 117
RECORD_BUTTON = 119
SEEK_LEFT = 116
SEEK_RIGHT = 115








