from __future__ import print_function
from __future__ import division
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import time
import copy
import math
import random
import numpy
from array import array
import datetime
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import visual,core,data,event,gui
from psychopy import sound
from psychopy.constants import *  # things like STARTED, FINISHED
import csv
#
#
#
#
#
#
#
# Last updated on: 29/10/2019
#
#
#
#
#
#
#
#
#

########################################################################################
# Draw a box to get experiment and participant information
########################################################################################
expName = u'Flashing_grid_task'  # Name the experiment
expInfo = {u'Session': u'001', u'Participant': u'001'} # What the box should ask for
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName) # Draw the bloody box!
if dlg.OK == False: core.quit() # If "cancel" is clicked end the whole thing
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
########################################################################################
########################################################################################


########################################################################################
# Where To Write File
########################################################################################
# Setup files for saving
if not os.path.isdir('JD_task_results'): # Create this folder wherever this script is saved
    os.makedirs('JD_task_results')  # If this fails (e.g. permissions) we will get error
filename = 'JD_Task_' + '%s_%s' %(expInfo['Participant'], expInfo['date'])+'.txt'
print('filename used for data is ' +filename)
########################################################################################
########################################################################################


########################################################################################
# Define the window
########################################################################################
# flag for 'escape' or other condition => quit the exp
endExpNow = False

# Setup the Window
win = visual.Window(fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='cm')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess 
########################################################################################
########################################################################################


########################################################################################
# Changeable experimental parameters
########################################################################################
# Number of experimental trials
singletrials = 2     # **Number of single grid trials per colour_order block which should be set to 40 in the real experiment**
practicetrials = 6    # Number of practice trials for single AND paired grid trials
numtrials = 1000 # The calculated TOTAL amount of practice and experimental single grid trials 
hst = 120 # how many single trials

# Text size:
textsize = 0.75
# Fixation cross:
fcross = visual.TextStim(win, text="+")
#########################################################################################





####################
# initial introduction text:
####################
# Section 2 practice trials text:
section2prac = '''During this experiment you will have to perform two types of judgements. On some trials you will be required to determine whether there are more blue or orange patches in a grid. Other trials will require you to judge if determining whether there are more blue or orange patches in a grid is easy or hard. Example grids are shown below. '''
section2practice22i = visual.TextStim(win, text=section2prac,pos=(0.0, 10), height=textsize,wrapWidth=40,alignHoriz = 'center')
one111t = '''Observe the grid on the left for a few seconds. For the grid to the left, on tasks involving determining whether there are more blue or oranges patches in the grid you may be asked: Are there more blue than orange patches in the grid? Press "z" for YES or "m" or NO.'''
section2practice22ii = visual.TextStim(win, text=one111t,pos=(0.0, 6), height=textsize,wrapWidth=40,alignHoriz = 'center') 
one1112t = '''Observe the Grid on the Right for a few seconds. For the grid on the right, on trials involving judgements determining whether the task is easy or difficult to answer, you may be asked: If you think this decision would be hard press "z" or if you think this decision would be easy press "m". '''
section2practice22iii = visual.TextStim(win, text=one1112t,pos=(0.0, 2), height=textsize,wrapWidth=40,alignHoriz = 'center') 
one1113t = '''Press the spacebar to continue...'''
section2practice22iiii = visual.TextStim(win, text=one1113t,pos=(0.0, -10), height=textsize) 
####################
####################



##################################################
# proportions practice block 1:
##################################################
# Practice text:
practice01 = '''Practice trials for proportion judgements will now begin. For these practice trials you must answer the following question on each trial: Does the grid have more Orange than Blue Patches? Press "z" for YES or "m" for NO.'''
practicetext1 = visual.TextStim(win, text=practice01,pos=(0,3), height=textsize, wrapWidth=30,alignHoriz = 'center') 
# Practice text:
practice0199 = '''In order to successfull complete the practice trials, you must answer 5 trials correctly in a row. Press any key on the keyboard to begin the practice trials...'''
practicetext17 = visual.TextStim(win, text=practice0199,pos=(0,-0.5), height=textsize, wrapWidth=30,alignHoriz = 'center')
##################################################
# task difficulty practice block 2:
##################################################
# Practice text:
practice012 = '''Practice trials for difficulty judgements will now begin. For these practice trials you must judge whether the decision about colour proportions is hard or easy. If you think the decision would be hard Press "z" or "m" if you think the decision would be easy.'''
practicetext12 = visual.TextStim(win, text=practice012,pos=(0,3), height=textsize, wrapWidth=30,alignHoriz = 'center') 
# Practice text:
practice01992 = '''In order to successfull complete the practice trials, you must answer 5 trials correctly in a row. Press any key on the keyboard to begin the practice trials...'''
practicetext172 = visual.TextStim(win, text=practice01992,pos=(0,-0.5), height=textsize, wrapWidth=30,alignHoriz = 'center')
###################################################




####################################################
# End of practice text - PROPORTIONS:
####################################################
# practice trials for blue
prac001bf = '''Practice trials have now finished.'''
endspractice_bf = visual.TextStim(win, text=prac001bf,pos=(-0.7,3.5), height=textsize) 
prac001b1 = '''On the next set of trials you must answer the following question: Does the grid have more Blue than Orange Patches? Press "z" for YES or "m" for NO.'''
endspractice_b1 = visual.TextStim(win, text=prac001b1,pos=(0,0), height=textsize, wrapWidth=27,alignHoriz = 'center') 
prac001b2 = '''Press any key on the keyboard to begin the actual trials...'''
endspractice_b2 = visual.TextStim(win, text=prac001b2,pos=(-0.5,-3.5), height=textsize,wrapWidth=20) 
# Practice trials for orange
prac001of = '''Practice trials have now finished.'''
endspractice_of = visual.TextStim(win, text=prac001of,pos=(-0.7,3.5), height=textsize) 
prac001o1 = '''On the next set of trials you must answer the following question: Does the grid have more Orange than Blue Patches? Press "z" for YES or "m" for NO.'''
endspractice_o1 = visual.TextStim(win, text=prac001o1,pos=(0,0), height=textsize, wrapWidth=27,alignHoriz = 'center') 
prac001o2 = '''Press any key on the keyboard to begin the actual trials...'''
endspractice_o2 = visual.TextStim(win, text=prac001o2,pos=(-0.5,-3.5), height=textsize,wrapWidth=20) 
####################################################
####################################################
# End of practice text - JUDGEMENTS:
####################################################
# 
prac001b1j = '''On the next set of trials you must answer the following question: If you think the decision would be hard Press "z" or "m" if you think the decision would be easy..'''
endspractice_b1j = visual.TextStim(win, text=prac001b1j,pos=(0,0), height=textsize, wrapWidth=27,alignHoriz = 'center') 
####################################################



################################################################################################
# Odd bits:
################################################################################################
# End of first part of the experiment text
two01 = '''One set of trials have now finished.'''
endtext01 = visual.TextStim(win, text=two01,pos=(-2.4,1.5), height=textsize)  
two010 = '''Press any key on the keyboard to continue...'''
endtext010 = visual.TextStim(win, text=two010,pos=(-1.0,0), height=textsize) 
# Break text
breaktext01 = '''You are now on a break. Press any key on the keyboard to end your break and continue with the task immediately...'''
breaktext = visual.TextStim(win, text=breaktext01, height=textsize) 
# End of experiment text
two = '''Please take a short break now, before continuing ...'''
endtext = visual.TextStim(win, text=two, height=textsize)  
# End of the whole experiment text 
two22 = '''The experiment has now finished!'''
endtext1 = visual.TextStim(win, text=two22, height=textsize)  
# Correct practice trial text:
cres = '''CORRECT'''
correct_res = visual.TextStim(win, text=cres, pos=(0,0), height=1)
# Inccorect practice trial text:
icres = '''INCORRECT'''
incorrect_res = visual.TextStim(win, text=icres, pos=(0,0), height=1)
# Inccorect practice trial text:
timedtext = '''TOO SLOW'''
timedout = visual.TextStim(win, text=timedtext, pos=(0,0), height=1)
################################################################################################












########################################################################################
########################################################################################
# Orange:
color1 = [0.9686,0.6392,0.0353]
# Blue:
color2 = [-0.8980,1.0000,1.0000] 

# Define some clocks
checkclock01 = core.Clock() # For single grid trials     S1
checkclock = core.Clock() # For paired grid trials       P1
checkclock01s2 = core.Clock() # For single grid trials   S2
checkclock = core.Clock() # For paired grid trials       P2
########################################################################################
########################################################################################


########################################################################################
# List That Will Record Responses & RTs
########################################################################################
# For single grid trials s1
keyspressed = []*singletrials
correctresponse = []*singletrials
RT =[]*singletrials
trialNo = []*singletrials
conused = []*singletrials
difflevel = []*singletrials
colourcolour1 = []*singletrials

# For single grid trials s2
keyspressed2 = []*singletrials
correctresponse2 = []*singletrials
RT2 =[]*singletrials
trialNo2 = []*singletrials
conused2 = []*singletrials
difflevel2 = []*singletrials
colourcolour2 = []*singletrials

# For single grid trials s3
keyspressed3 = []*singletrials
correctresponse3 = []*singletrials
RT3 =[]*singletrials
trialNo3 = []*singletrials
conused3 = []*singletrials
difflevel3 = []*singletrials
colourcolour3 = []*singletrials

# For single grid trials s4
keyspressed4 = []*singletrials
correctresponse4 = []*singletrials
RT4 =[]*singletrials
trialNo4 = []*singletrials
conused4 = []*singletrials
difflevel4 = []*singletrials
colourcolour4 = []*singletrials

# Initilise the colour variable:
colour = []
########################################################################################
########################################################################################

########################################################################################
# Set the conditions for the single grid trials - JUDGING PROPORTIONS:
########################################################################################
con1 = (1)
con2 = (2)
con3 = (3)
con4 = (4)
con5 = (5)
con6 = (6)
con7 = (7)
con8 = (8)

# Define the blue and orange block signle grid trials:
single_proportions = []


for i in range(15):
# The single grid trials for the blue block:
    single_proportions.append(con1)
    single_proportions.append(con2)
    single_proportions.append(con3)
    single_proportions.append(con4)
    single_proportions.append(con5)
    single_proportions.append(con6)
    single_proportions.append(con7)
    single_proportions.append(con8)
np.random.shuffle(single_proportions)
print('number of pp trials ======',len(single_proportions))

# Conditions for practice trials:
singlegridpractice = []
for i in range(2):
    singlegridpractice.append(10)
    singlegridpractice.append(20)
    singlegridpractice.append(30)
    
np.random.shuffle(singlegridpractice) # Randomly shuffle single grid practice trials


# Create and shuffle which colour block participants will see first:
colour_order = [1,2] # 1 is the colour blue and 2 is the colour orange
np.random.shuffle(colour_order)
########################################################################################
########################################################################################


########################################################################################
########################################################################################
########################################################################################
# INTRODUCTION
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100


########################################################################################
########################################################################################

########################################################################################
# Set main conditions and loop
########################################################################################
for i in range(1):
     
    p1=.70 # How much Blue for the first grid (we want more blue here for easy trials: 70/30)
    p2=.48 # How much Blue for the second grid (we want more orange here for hard trials: 52/48)

    leftside  = [-6,-5]
    rightside = [6,-5]
    
    # Set the position of left stimulus
    def set_positions():
        global fl_p # Where should the flash be drawn
        fl_p = leftside
            
    # Set the position of right stimulus
    def set_positions2():
        global fl_p2 # Where should the flash be drawn
        fl_p2 = rightside
        
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position=[0,0], position2=[0,0], square_size=10, columns=20, rows=20, percent_color1=p1, percent_color2=p2): # Colour 1 being manipulated
        global flash # The flash stimulus (an array of flashing squares)
        global flash2
        color_set = [color2, color1]   # BLUE
        color_set2 = [color2, color1]  # BLUE
        cell_number = columns * rows
    
        num_color1 = int(np.floor(float(cell_number)*percent_color1)) # First colour
        num_color2 = int(np.floor(float(cell_number)*(1-percent_color1))) # Second f
    
        num_color3 = int(np.floor(float(cell_number)*percent_color2)) # First colour
        num_color4 = int(np.floor(float(cell_number)*(1-percent_color2))) # Second f
        
        #print(cell_number,num_color1,num_color2)
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors = []
        for i in range(num_color1):
            f_colors.append(color_set[0])
        for i in range(num_color2):
            f_colors.append(color_set[1])
        numpy.random.shuffle(color_set)
        i = cell_number - len(f_colors)
        while i > 0:
            f_colors.append(color_set[i])
            i -= 1
        
        f_colors2 = []
        for i in range(num_color3):
            f_colors2.append(color_set2[0])
        for i in range(num_color4):
            f_colors2.append(color_set2[1])
        numpy.random.shuffle(color_set2)
        i = cell_number - len(f_colors2)
        while i > 0:
            f_colors2.append(color_set2[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors)
        shuffle(f_colors2)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash = visual.ElementArrayStim(win=win,
                            fieldPos=position,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
        # MAIN FUNCTION TO CREATE SECOND GRID
        flash2 = visual.ElementArrayStim(win=win,
                        fieldPos=position2,
                        fieldShape='sqr',
                        nElements=cell_number,
                        sizes=square_size,
                        xys=xys2,
                        colors=f_colors2,
                        elementTex=None,
                        elementMask=None,
                        name='flash',
                        autoLog=False)
                            
                            
    
    # flash stimulus change
    def flash_change():
        global flash
        shuffle(flash.colors)
        flash.setColors(flash.colors)
    
    def flash2_change():
        global flash2
        shuffle(flash2.colors)
        flash2.setColors(flash2.colors)
    
    # Time variables used during the experiment
    def set_timing():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions()
    set_positions2()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p, fl_p2, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents = []
    show_flashComponents.append(frame_fl)
    for thisComponent in show_flashComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################

    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # update/draw components on each frame
        #print(frameN)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_change()
            flash2_change()
            f_change += f_t
        
        section2practice22i.draw() # Draw ending message here
        section2practice22ii.draw() # Draw ending message here
        section2practice22iii.draw() # Draw ending message here
        section2practice22iiii.draw() # Draw ending message here
        flash.draw()  # First stimulus is drawn here
        flash2.draw() # Second stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        if event.getKeys(keyList=["space"]):
            break
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
########################################################################################
########################################################################################


########################################################################################
########################################################################################
########################################################################################
# Single Grid Trials - JUDGING PROPORTIONS - BLOCK 1:
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100
    
# Set the position of left stimulus
def set_positions01():
    global fl_p3 # Where should the flash be drawn
    fl_p3 = [0, 0]

########################################################################################
# Set main conditions and loop
########################################################################################

# Counter to keep track of things
counter = 0
thecount = 0
counter01 = 0
thecount01 = 0
pcounter = 1
pcounter2 = 0
titi = 1
# Some additional variables:
theline = 500 # theline variable must be greater than 500 to continue onto the experimental trials. 500 is just an arbitary number
practicecount = [] # Length of this must be greater than 5 to end practice trials
pcounternew = 1 #
pcounternew2 = 0 #

# Set the colour order for the first colour block:
colour_order1 = colour_order[0]
for j in range(numtrials): # 
    
    # Update the pcounter after participants have gotten 5 questions in a row correct during practice:
    if len(practicecount) == 5:
        pcounter = theline+10
        pcounternew2 = pcounternew2+1
    
    
    
    if pcounter <= 500:
        singleconditionsx = singlegridpractice[pcounternew-1]
    elif pcounter > 500:
        # Select what condition is to be performed on experimental trials:
        if colour_order1 == 1:
            singleconditionsx = single_proportions[counter01]
        elif colour_order1 == 2:
            singleconditionsx = single_proportions[counter01]
    
    if pcounter > 500:
        # Append the condition we're on:
        if singleconditionsx == 1:
            conused.append('B,o')
            difflevel.append('Easy 1')
        elif singleconditionsx == 2:
            conused.append('b,o')
            difflevel.append('Easy 2')
        elif singleconditionsx == 3:
            conused.append('b,b')
            difflevel.append('Hard 1')
        elif singleconditionsx == 4:
            conused.append('B,b') 
            difflevel.append('Hard 2')
        elif singleconditionsx == 5:
            conused.append('O,b')
            difflevel.append('Easy 1')
        elif singleconditionsx == 6:
            conused.append('o,b')
            difflevel.append('Easy 2')
        elif singleconditionsx == 7:
            conused.append('o,b') 
            difflevel.append('Hard 1')
        elif singleconditionsx == 8:
            conused.append('O,b') 
            difflevel.append('Hard 2')
    
    # More Blue Trials:
    if singleconditionsx == 1:
        p01 = .66#(66/34) PTASK - EASY
    elif singleconditionsx == 2:
        p01 = .62#(62/38) PTASK - EASY
    elif singleconditionsx == 3:
        p01 = .52#(52/48) PTASK - HARD
    elif singleconditionsx == 4:
        p01 = .56#(56/44) PTASK - HARD
        
    # More Orange Trials:
    elif singleconditionsx == 5:
        p01 = .66#(66/34) PTASK - EASY
    elif singleconditionsx == 6:
        p01 = .62#(62/38) PTASK - EASY
    elif singleconditionsx == 7:
        p01 = .52#(52/48) PTASK - HARD
    elif singleconditionsx == 8:
        p01 = .56#(56/44) PTASK - HARD
        
    
    elif singleconditionsx == 10:
        p01 = .66 # (66/34) orange EASY (more orange)
    elif singleconditionsx == 20:
        p01 = .38 # (62/38) a lot of blue EASY (more blue)
    elif singleconditionsx == 30:
        p01 = .56 # (56/44) a lot of orange HARD (more orange)
        
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position01=[0,0], square_size=10, columns=20, rows=20, percent_color01=p01): # Colour2 being manipulated whic is BLUE
        global flash01 # The flash stimulus (an array of flashing squares)
        
        if singleconditionsx <= 4:
            color_set01 = [color2, color1] # color2 is being manipulated which is the BLUE
        elif singleconditionsx >= 5:
            color_set01 = [color1, color2] # colour1 is being manipulated which is the ORANGE
        cell_number = columns * rows
    
        num_color4 = int(np.floor(float(cell_number)*percent_color01)) # First colour
        num_color5 = int(np.floor(float(cell_number)*(1-percent_color01))) # Second colour
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors3 = []
        for i in range(num_color4):
            f_colors3.append(color_set01[0])
        for i in range(num_color5):
            f_colors3.append(color_set01[1])
        numpy.random.shuffle(color_set01)
        i = cell_number - len(f_colors3)
        while i > 0:
            f_colors3.append(color_set01[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors3)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash01 = visual.ElementArrayStim(win=win,
                            fieldPos=position01,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors3,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
                            
                            
    
    # flash stimulus change
    def flash_change():
        global flash01
        shuffle(flash01.colors)
        flash01.setColors(flash01.colors)
    
    # Time variables used during the experiment
    def set_timing():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions01()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p3, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock01 = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p3, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock01 = core.Clock()  # to track the time since experiment started
    routineTimer01 = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock01.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents01 = []
    show_flashComponents01.append(frame_fl)
    for thisComponent in show_flashComponents01:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    # Put up the introduction text 
    if pcounternew == 1 and titi == 1:
        win.flip()
        practicetext1.draw()
        practicetext17.draw()
        win.flip()
        keypressed = event.waitKeys(timeStamped=False)
        checkclock01.reset()
                    
                    
    if pcounternew2 == 1:
        if colour_order1 == 1:
            win.flip()
            endspractice_b1.draw()
            endspractice_b2.draw()
            endspractice_bf.draw()
            win.flip()
        elif colour_order1 == 2:
            win.flip()
            endspractice_o1.draw()
            endspractice_o2.draw()
            endspractice_of.draw()
            win.flip()
        keypressed = event.waitKeys(timeStamped=False)
        checkclock01.reset()
    tot = core.Clock() # For timing out participants during practice trials
    tot.reset()
    titi = 2
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:
            
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock01.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_change()
            f_change += f_t
        flash01.draw()  # First stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer01.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents01:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
                
        outtimer = tot.getTime()
        if pcounter <= 500:
            if event.getKeys(keyList=["z"]):
                if singleconditionsx is 10 or singleconditionsx is 30:
                    win.flip()
                    correct_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                    practicecount.append(1)
                    pcounternew = pcounternew+1
                else:
                    win.flip()
                    incorrect_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                    practicecount =[]
                    pcounternew = 1
                event.clearEvents(eventType='keyboard')
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                event.clearEvents(eventType='keyboard')
                break
            elif event.getKeys(keyList=["m"]):
                if singleconditionsx is 20:
                    win.flip()
                    correct_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                    practicecount.append(1)
                    pcounternew = pcounternew+1
                else:
                    win.flip()
                    incorrect_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                    practicecount =[]
                    pcounternew = 1
                event.clearEvents(eventType='keyboard')
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                event.clearEvents(eventType='keyboard')
                break
            elif outtimer > 1.0:
                win.flip()
                timedout.draw()
                win.flip()
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                practicecount =[]
                pcounternew = 1
                event.clearEvents(eventType='keyboard')
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                tot.reset()
                event.clearEvents(eventType='keyboard')
                break
                
        # For experimental trials:
        elif pcounter > theline:
            # RESPONSE 1:
            if event.getKeys(keyList=["escape"]):
                win.flip()
                breaktext.draw()
                win.flip()
                keypressed = event.waitKeys(timeStamped=False)
                checkclock01.reset()
            if event.getKeys(keyList=["6"]):
                win.close()
                core.quit()
            if event.getKeys(keyList=["z"]): # MORE key
            
                # Update practice trial counter
                pcounter = pcounter+1
                pcounternew2 = pcounternew2+1
                
                # print the condition we did
                print("actual single trial done =", singleconditionsx)
                
                # Track response times
                #rt = rtclock.getTime()
                time01 = checkclock01.getTime()
                RT.append(time01)
                
                if colour_order1 == 1:
                    if singleconditionsx <= 4:
                        correctresponse.append('1')
                        print('response ===========  correct')
                    elif singleconditionsx >= 5:
                        correctresponse.append('0')
                        print('response ===========  incorrect')
                elif colour_order1 == 2:
                    if singleconditionsx <= 4:
                        correctresponse.append('0')
                        print('response ===========  incorrect')
                    elif singleconditionsx >= 5:
                        correctresponse.append('1')
                        print('response ===========  correct')
                # Append which colour question was being asked:
                colourcolour1.append(colour_order1)
                
                # Keep track of keys pressed
                keyspressed.append('left')
                
                # Update the counter
                counter01 = counter01+1
                
                # Keep track of trial number to be saved 
                trialNo.append(counter01)
                
                
                # DRAW FIXATION CROSS AFTER EACH TRIAL
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                event.clearEvents(eventType='keyboard')
                
                # END THE EXPERIMENT HERE AND SAVE DATA
                if counter01 == hst:
                    win.flip() # Clears the window
                    endtext01.draw() # Draw ending message here
                    endtext010.draw()
                    win.flip() # Clears the window
                    keypressed = event.waitKeys(timeStamped=False)
                break # End the expriment
                
             # RESPONSE 2: (Right Side)
            if event.getKeys(keyList=["m"]): # LESS key
                
                
                # Update practice trial counter
                pcounter = pcounter+1
                pcounternew2 = pcounternew2+1
                
                # print the condition we did
                print("actual single trial done =", singleconditionsx)
                
                time01 = checkclock01.getTime()
                RT.append(time01)
                
                if colour_order1 == 1:
                    if singleconditionsx <= 4:
                        correctresponse.append('0')
                        print('response ===========  incorrect')
                    elif singleconditionsx >= 5:
                        correctresponse.append('1')
                        print('response ===========  correct')
                elif colour_order1 == 2:
                    if singleconditionsx <= 4:
                        correctresponse.append('1')
                        print('response ===========  correct')
                    elif singleconditionsx >= 5:
                        correctresponse.append('0')
                        print('response ===========  incorrect')
                # Append which colour question was being asked:
                colourcolour1.append(colour_order1)
                
                # Keep track of keys pressed
                keyspressed.append('right')
                
                # Update the counter
                counter01 = counter01+1
                
                # Keep track of trial number to be saved 
                trialNo.append(counter01)
                
                
                # DRAW FIXATION CROSS AFTER EACH TRIAL
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                event.clearEvents(eventType='keyboard')
                
                # END THE EXPERIMENT HERE AND SAVE DATA
                if counter01 == hst:
                    win.flip() # Clears the window
                    endtext01.draw() # Draw ending message here
                    endtext010.draw()
                    win.flip() # Clears the window
                    keypressed = event.waitKeys(timeStamped=False)
                break # End the expriment
            
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
        
        # END THE EXPERIMENT HERE
        if counter01 == hst:
            win.flip() # Clears the window
            endtext01.draw() # Draw ending message here
            endtext010.draw()
            win.flip() # Clears the window
            keypressed = event.waitKeys(timeStamped=False)
            break
            
    if counter01 == hst:
        break
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents01:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################

# Shuffle the single grid conditions again:
np.random.shuffle(single_proportions)

########################################################################################
########################################################################################
########################################################################################
# Single Grid Trials - JUDGING DIFFICULTY - BLOCK 1:
########################################################################################
########################################################################################
########################################################################################

########################################################################################
# Set the conditions for the single grid trials - JUDGING PROPORTIONS:
########################################################################################
con1 = (1)
con2 = (2)
con3 = (3)
con4 = (4)
con5 = (5)
con6 = (6)
con7 = (7)
con8 = (8)

# Define the blue and orange block signle grid trials:
single_proportions2 = []


for i in range(15):
# The single grid trials for the blue block:
    single_proportions2.append(con1)
    single_proportions2.append(con2)
    single_proportions2.append(con3)
    single_proportions2.append(con4)
    single_proportions2.append(con5)
    single_proportions2.append(con6)
    single_proportions2.append(con7)
    single_proportions2.append(con8)
np.random.shuffle(single_proportions2)
print('number of jt trials ====',len(single_proportions2))
l1 = single_proportions2.count(1)
l2 = single_proportions2.count(2)
l3 = single_proportions2.count(3)
l4 = single_proportions2.count(4)
l5 = single_proportions2.count(5)
l6 = single_proportions2.count(6)
l7 = single_proportions2.count(7)
l8 = single_proportions2.count(8)
#print('lol =',l1,l2,l3,l4,l5,l6,l7,l8)

# Conditions for practice trials:
singlegridpractice2 = []
for i in range(3):
    singlegridpractice2.append(10)
    singlegridpractice2.append(20)
    singlegridpractice2.append(30)
np.random.shuffle(singlegridpractice2) # Randomly shuffle single grid practice trials
#######################################################################################
#######################################################################################



# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100
    
# Set the position of left stimulus
def set_positions01():
    global fl_p3 # Where should the flash be drawn
    fl_p3 = [0, 0]

########################################################################################
# Set main conditions and loop
########################################################################################

# Counter to keep track of things
counter = 0
thecount = 0
counter01 = 0
thecount01 = 0
pcounter = 1
pcounter2 = 0
tata = 1
# Some additional variables:
theline = 500 # theline variable must be greater than 500 to continue onto the experimental trials. 500 is just an arbitary number
practicecount = [] # Length of this must be greater than 5 to end practice trials
pcounternew = 1 #
pcounternew2 = 0 #

# Set the colour order for the first colour block:
colour_order1 = colour_order[0]
for j in range(numtrials): # 
    
    # Update the pcounter after participants have gotten 5 questions in a row correct during practice:
    if len(practicecount) == 5:
        pcounter = theline+10
        pcounternew2 = pcounternew2+1
    
    
    
    if pcounter <= 500:
        singleconditionsx = singlegridpractice2[pcounternew-1]
    elif pcounter > 500:
        # Select what condition is to be performed on experimental trials:
        if colour_order1 == 1:
            singleconditionsx = single_proportions2[counter01]
        elif colour_order1 == 2:
            singleconditionsx = single_proportions2[counter01]
    
    if pcounter > 500:
        # Append the condition we're on:
        if singleconditionsx == 1:
            conused2.append('b,o')
            difflevel2.append('Easy 1')
        elif singleconditionsx == 2:
            conused2.append('B,o')
            difflevel2.append('Easy 2')
        elif singleconditionsx == 3:
            conused2.append('b,b')
            difflevel2.append('Hard 1')
        elif singleconditionsx == 4:
            conused2.append('B,b') 
            difflevel2.append('Hard 2')
        elif singleconditionsx == 5:
            conused2.append('o,b')
            difflevel2.append('Easy 1')
        elif singleconditionsx == 6:
            conused2.append('O,b')
            difflevel2.append('Easy 2')
        elif singleconditionsx == 7:
            conused2.append('o,b')
            difflevel2.append('Hard 1')
        elif singleconditionsx == 8:
            conused2.append('O,b') 
            difflevel2.append('Hard 2')
    
    # More BLUE Trials:
    if singleconditionsx == 1:
        p01 = .52#(52/48) JDTASK - Easy
    elif singleconditionsx == 2:
        p01 = .66#(66/34) JDTASK - EASY
    elif singleconditionsx == 3:
        p01 = .56#(56/44) JDTASK - HARD
    elif singleconditionsx == 4:
        p01 = .62#(62/38) JDTASK - HARD
        
    # More ORANGE Trials:
    elif singleconditionsx == 5:
        p01 = .52#(52/48) JDTASK - Easy
    elif singleconditionsx == 6:
        p01 = .66#(66/34) TASK - EASY
    elif singleconditionsx == 7:
        p01 = .56#(56/44) JDTASK - HARD
    elif singleconditionsx == 8:
        p01 = .62#(62/38) JDTASK - HARD
    
    
    elif singleconditionsx == 10:
        p01 = .52 # orange (52/48) EASY
    elif singleconditionsx == 20:
        p01 = .34 # blue (66/34) EASY
    elif singleconditionsx == 30:
        p01 = .56 # orange (56/44) HARD
    #elif singleconditionsx == 40:
        #p01 = .38 # blue (62/38) HARD
        
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position01=[0,0], square_size=10, columns=20, rows=20, percent_color01=p01): # Colour2 being manipulated whic is BLUE
        global flash01 # The flash stimulus (an array of flashing squares)
        
        if singleconditionsx <= 4:
            color_set01 = [color2, color1] # color2 is being manipulated which is the BLUE
        elif singleconditionsx >= 5:
            color_set01 = [color1, color2] # colour1 is being manipulated which is the ORANGE
        cell_number = columns * rows
    
        num_color4 = int(np.floor(float(cell_number)*percent_color01)) # First colour
        num_color5 = int(np.floor(float(cell_number)*(1-percent_color01))) # Second colour
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors3 = []
        for i in range(num_color4):
            f_colors3.append(color_set01[0])
        for i in range(num_color5):
            f_colors3.append(color_set01[1])
        numpy.random.shuffle(color_set01)
        i = cell_number - len(f_colors3)
        while i > 0:
            f_colors3.append(color_set01[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors3)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash01 = visual.ElementArrayStim(win=win,
                            fieldPos=position01,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors3,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
                            
                            
    
    # flash stimulus change
    def flash_change():
        global flash01
        shuffle(flash01.colors)
        flash01.setColors(flash01.colors)
    
    # Time variables used during the experiment
    def set_timing():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions01()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p3, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock01 = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p3, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock01 = core.Clock()  # to track the time since experiment started
    routineTimer01 = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock01.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents01 = []
    show_flashComponents01.append(frame_fl)
    for thisComponent in show_flashComponents01:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    # Put up the introduction text 
    if pcounternew == 1 and tata == 1:
        win.flip()
        practicetext12.draw()
        practicetext172.draw()
        win.flip()
        keypressed = event.waitKeys(timeStamped=False)
        checkclock01.reset()
                    
                    
    if pcounternew2 == 1:
        if colour_order1 == 1:
            win.flip()
            endspractice_b1j.draw()
            endspractice_b2.draw()
            endspractice_bf.draw()
            win.flip()
        elif colour_order1 == 2:
            win.flip()
            endspractice_b1j.draw()
            endspractice_o2.draw()
            endspractice_of.draw()
            win.flip()
        keypressed = event.waitKeys(timeStamped=False)
        checkclock01.reset()
    tot.reset()
    tata = 2
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:
            
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock01.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_change()
            f_change += f_t
        flash01.draw()  # First stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer01.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents01:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        outtimer = tot.getTime()
        if pcounter <= 500:
            if event.getKeys(keyList=["z"]):
                # Update pcounter:
                if singleconditionsx is 10 or singleconditionsx is 30:
                    win.flip()
                    correct_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                    practicecount.append(1)
                    pcounternew = pcounternew+1
                else:
                    win.flip()
                    incorrect_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                    practicecount =[]
                    pcounternew = 1
                event.clearEvents(eventType='keyboard')
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                event.clearEvents(eventType='keyboard')
                break
            elif event.getKeys(keyList=["m"]):
                # Update pcounter:
                
                if singleconditionsx is 20:
                    win.flip()
                    correct_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                    practicecount.append(1)
                    pcounternew = pcounternew+1
                else:
                    win.flip()
                    incorrect_res.draw()
                    win.flip()
                    core.wait(1.5) # Keep the cross on screen for 2 seconds
                    practicecount =[]
                    pcounternew = 1
                event.clearEvents(eventType='keyboard')
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                event.clearEvents(eventType='keyboard')
                break
            elif outtimer > 1.0:
                win.flip()
                timedout.draw()
                win.flip()
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                practicecount =[]
                pcounternew = 1
                event.clearEvents(eventType='keyboard')
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                tot.reset()
                event.clearEvents(eventType='keyboard')
                break
        # For experimental trials:
        elif pcounter > theline:
            # RESPONSE 1:
            if event.getKeys(keyList=["escape"]):
                win.flip()
                breaktext.draw()
                win.flip()
                keypressed = event.waitKeys(timeStamped=False)
                checkclock01.reset()
            if event.getKeys(keyList=["6"]):
                win.close()
                core.quit()
            if event.getKeys(keyList=["z"]): # HARD key
            
                # Update practice trial counter
                pcounter = pcounter+1
                pcounternew2 = pcounternew2+1
                
                # print the condition we did
                print("actual single trial done =", singleconditionsx)
                
                # Track response times
                #rt = rtclock.getTime()
                time01 = checkclock01.getTime()
                RT2.append(time01)
                
                if singleconditionsx is 1 or singleconditionsx is 5 or singleconditionsx is 3 or singleconditionsx is 7 or singleconditionsx is 4 or singleconditionsx is 8:
                    correctresponse2.append('1')
                else:
                    correctresponse2.append('0')
                # Append which colour question was being asked:
                colourcolour2.append(colour_order1)
                
                # Keep track of keys pressed
                keyspressed2.append('left')
                
                # Update the counter
                counter01 = counter01+1
                
                # Keep track of trial number to be saved 
                trialNo2.append(counter01)
                
                
                # DRAW FIXATION CROSS AFTER EACH TRIAL
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                event.clearEvents(eventType='keyboard')
                
                # END THE EXPERIMENT HERE AND SAVE DATA
                if counter01 == hst:
                    win.flip() # Clears the window
                    endtext01.draw() # Draw ending message here
                    endtext010.draw()
                    win.flip() # Clears the window
                    keypressed = event.waitKeys(timeStamped=False)
                break # End the expriment
                
             # RESPONSE 2: (Right Side)
            if event.getKeys(keyList=["m"]): # EASY key
                
                
                # Update practice trial counter
                pcounter = pcounter+1
                pcounternew2 = pcounternew2+1
                
                # print the condition we did
                print("actual single trial done =", singleconditionsx)
                
                time01 = checkclock01.getTime()
                RT2.append(time01)
                
                    
                if singleconditionsx is 2 or singleconditionsx is 6:
                    correctresponse2.append('1')
                else:
                    correctresponse2.append('0')
                # Append which colour question was being asked:
                colourcolour2.append(colour_order1)
                
                
                # Keep track of keys pressed
                keyspressed2.append('right')
                
                # Update the counter
                counter01 = counter01+1
                
                # Keep track of trial number to be saved 
                trialNo2.append(counter01)
                
                
                # DRAW FIXATION CROSS AFTER EACH TRIAL
                win.flip() # Clears the window
                fcross.draw() # Draw the fixation cross
                win.flip() # Clears the window
                core.wait(1.5) # Keep the cross on screen for 2 seconds
                checkclock01.reset()
                event.clearEvents(eventType='keyboard')
                
                # END THE EXPERIMENT HERE AND SAVE DATA
                if counter01 == hst:
                    win.flip() # Clears the window
                    endtext01.draw() # Draw ending message here
                    endtext010.draw()
                    win.flip() # Clears the window
                    keypressed = event.waitKeys(timeStamped=False)
                break # End the expriment
            
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
        
        # END THE EXPERIMENT HERE
        if counter01 == hst:
            win.flip() # Clears the window
            endtext01.draw() # Draw ending message here
            endtext010.draw()
            win.flip() # Clears the window
            keypressed = event.waitKeys(timeStamped=False)
            break
            
    if counter01 == hst:
        break
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents01:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################



# Shuffle the single grid conditions again:
np.random.shuffle(single_proportions)



########################################################################################
########################################################################################
########################################################################################
# Single Grid Trials - JUDGING PROPORTIONS - BLOCK 2:
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100
    
# Set the position of left stimulus
def set_positions01():
    global fl_p3 # Where should the flash be drawn
    fl_p3 = [0, 0]

########################################################################################
# Set main conditions and loop
########################################################################################

# Counter to keep track of things
counters2 = 0
thecounts2 = 0
counter01s2 = 0
thecount01s2 = 0
pcounters2 = practicetrials+1
pcounter2s2 = 1

# Set the colour order for the first colour block:
colour_order1 = colour_order[1]


if colour_order1 == 1:
    win.flip()
    endspractice_b1.draw()
    endspractice_b2.draw()
    endspractice_bf.draw()
    win.flip()
elif colour_order1 == 2:
    win.flip()
    endspractice_o1.draw()
    endspractice_o2.draw()
    endspractice_of.draw()
    win.flip()
keypressed = event.waitKeys(timeStamped=False)
checkclock01s2.reset()
        
for j in range(hst):
    # Select what condition is to be performed on experimental trials:
    if colour_order1 == 1:
        singleconditionsx = single_proportions[counter01s2]
    elif colour_order1 == 2:
        singleconditionsx = single_proportions[counter01s2]
        
    
    if pcounter > practicetrials:
        # Append the condition we're on:
        if singleconditionsx == 1:
            conused3.append('B,o')
            difflevel3.append('Easy 1')
        elif singleconditionsx == 2:
            conused3.append('b,o')
            difflevel3.append('Easy 2')
        elif singleconditionsx == 3:
            conused3.append('b,b')
            difflevel3.append('Hard 1')
        elif singleconditionsx == 4:
            conused3.append('B,b') 
            difflevel3.append('Hard 2')
        elif singleconditionsx == 5:
            conused3.append('O,b')
            difflevel3.append('Easy 1')
        elif singleconditionsx == 6:
            conused3.append('o,b')
            difflevel3.append('Easy 2')
        elif singleconditionsx == 7:
            conused3.append('o,b') 
            difflevel3.append('Hard 1')
        elif singleconditionsx == 8:
            conused3.append('O,b') 
            difflevel3.append('Hard 2')
    
    # More Blue Trials:
    if singleconditionsx == 1:
        p01 = .66#(66/34) PTASK - EASY
    elif singleconditionsx == 2:
        p01 = .62#(62/38) PTASK - EASY
    elif singleconditionsx == 3:
        p01 = .52#(52/48) JDTASK - HARD
    elif singleconditionsx == 4:
        p01 = .56#(56/44) JDTASK - HARD
        
    # More Orange Trials:
    elif singleconditionsx == 5:
        p01 = .66#(66/34) PTASK - EASY
    elif singleconditionsx == 6:
        p01 = .62#(62/38) PTASK - EASY
    elif singleconditionsx == 7:
        p01 = .52#(52/48) JDTASK - HARD
    elif singleconditionsx == 8:
        p01 = .56#(56/44) JDTASK - HARD
        
    
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position01=[0,0], square_size=10, columns=20, rows=20, percent_color01=p01): # Colour2 being manipulated whic is BLUE
        global flash01s2 # The flash stimulus (an array of flashing squares)
        
        if singleconditionsx <= 4:
            color_set01 = [color2, color1] # color2 being manipulated which is the BLUE
        elif singleconditionsx >= 5:
            color_set01 = [color1, color2] # colour1 is being manipulated which is the ORANGE
        cell_number = columns * rows
    
        num_color4 = int(np.floor(float(cell_number)*percent_color01)) # First colour
        num_color5 = int(np.floor(float(cell_number)*(1-percent_color01))) # Second colour
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors3s2 = []
        for i in range(num_color4):
            f_colors3s2.append(color_set01[0])
        for i in range(num_color5):
            f_colors3s2.append(color_set01[1])
        numpy.random.shuffle(color_set01)
        i = cell_number - len(f_colors3s2)
        while i > 0:
            f_colors3s2.append(color_set01[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors3s2)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash01s2 = visual.ElementArrayStim(win=win,
                            fieldPos=position01,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors3s2,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
                            
                            
    
    # flash stimulus change
    def flash_changes2():
        global flash01s2
        shuffle(flash01s2.colors)
        flash01s2.setColors(flash01s2.colors)
    
    # Time variables used during the experiment
    def set_timings2():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions01()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p3, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock01s2 = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p3, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock01s2 = core.Clock()  # to track the time since experiment started
    routineTimer01s2 = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock01s2.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents01s2 = []
    show_flashComponents01s2.append(frame_fl)
    for thisComponent in show_flashComponents01:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:    
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock01s2.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # update/draw components on each frame
        #print(frameN)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_changes2()
            f_change+= f_t
#        if colour_order1 == 1:
#            strialtextb.draw()
#        elif colour_order1 == 2:
#            #strialtexto.draw()
        flash01s2.draw()  # First stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer01s2.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents01s2:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
                
        # RESPONSE 1: (Left Side - BLUE)
        if event.getKeys(keyList=["escape"]):
            win.flip()
            breaktext.draw()
            win.flip()
            keypressed = event.waitKeys(timeStamped=False)
            checkclock01s2.reset()
        if event.getKeys(keyList=["6"]):
            win.close()
            core.quit()
        if event.getKeys(keyList=["z"]): # MORE key
        
            # Update practice trial counter
            pcounters2 = pcounters2+1
            
            # print the condition we did
            print("actual single trial done =", singleconditionsx)
            
            # Track response times
            #rt = rtclock.getTime()
            time01s2 = checkclock01s2.getTime()
            RT3.append(time01s2)
            
            if colour_order1 == 1:
                if singleconditionsx <= 4:
                    correctresponse3.append('1')
                    print('response ===========  correct')
                elif singleconditionsx >= 5:
                    correctresponse3.append('0')
                    print('response ===========  incorrect')
            elif colour_order1 == 2:
                if singleconditionsx <= 4:
                    correctresponse3.append('0')
                    print('response ===========  incorrect')
                elif singleconditionsx >= 5:
                    correctresponse3.append('1')
                    print('response ===========  correct')
            # Append which colour question was being asked:
            colourcolour3.append(colour_order1)
            
            # Keep track of keys pressed
            keyspressed3.append('left')
            
            # Update the counter
            counter01s2 = counter01s2+1
            
            # Keep track of trial number to be saved 
            trialNo3.append(counter01s2)
            
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(1.5) # Keep the cross on screen for 2 seconds
            checkclock01s2.reset()
            event.clearEvents(eventType='keyboard')
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter01s2 == hst:
                win.flip() # Clears the window
                endtext01.draw() # Draw ending message here
                endtext010.draw()
                win.flip() # Clears the window
                keypressed = event.waitKeys(timeStamped=False)
            break # End the expriment
            
         # RESPONSE 2: (Right Side - ORANGE)
        if event.getKeys(keyList=["m"]): # LESS key
            
            
            # Update practice trial counter
            pcounters2 = pcounters2+1
            
            # print the condition we did
            print("actual single trial done =", singleconditionsx)
            
            time01s2 = checkclock01s2.getTime()
            RT3.append(time01s2)
            
            if colour_order1 == 1:
                if singleconditionsx <= 4:
                    correctresponse3.append('0')
                    print('response ===========  incorrect')
                elif singleconditionsx >= 5:
                    correctresponse3.append('1')
                    print('response ===========  correct')
            elif colour_order1 == 2:
                if singleconditionsx <= 4:
                    correctresponse3.append('1')
                    print('response ===========  correct')
                elif singleconditionsx >= 5:
                    correctresponse3.append('0')
                    print('response ===========  incorrect')
        # Append which colour question was being asked:
            colourcolour3.append(colour_order1)
            
            # Keep track of keys pressed
            keyspressed3.append('right')
            
            # Update the counter
            counter01s2 = counter01s2+1
            
            # Keep track of trial number to be saved 
            trialNo3.append(counter01s2)
            
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(1.5) # Keep the cross on screen for 2 seconds
            checkclock01s2.reset()
            event.clearEvents(eventType='keyboard')
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter01s2 == hst:
                win.flip() # Clears the window
                endtext01.draw() # Draw ending message here
                endtext010.draw()
                win.flip() # Clears the window
                keypressed = event.waitKeys(timeStamped=False)
                #nowbreak = nowbreak+1
            break # End the expriment
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
         
        # END THE EXPERIMENT HERE:
        if counter01s2 == hst:
            break
            
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents01s2:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################


# Shuffle the single grid conditions again:
np.random.shuffle(single_proportions)


########################################################################################
########################################################################################
########################################################################################
# Single Grid Trials - JUDGING DIFFICULTY - BLOCK 2:
########################################################################################
########################################################################################
########################################################################################
# Initialize components for Routine "init_experiment"
init_experimentClock = core.Clock()
# set_colors()
# Colors used during the experiment.s
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global sq_c # square color
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = 1
    f_c = -0.06
    sq_c = -0.37
    t_c = -0.06

# set_sizes()
# Sizes used during the experiment
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    f_s = 540
    sq_s = 800
    l_s = 100
    
# Set the position of left stimulus
def set_positions01():
    global fl_p3 # Where should the flash be drawn
    fl_p3 = [0, 0]

########################################################################################
# Set main conditions and loop
########################################################################################

# Counter to keep track of things
counters2 = 0
thecounts2 = 0
counter01s2 = 0
thecount01s2 = 0
pcounters2 = practicetrials+1
pcounter2s2 = 1

# Set the colour order for the first colour block:
colour_order1 = colour_order[1]

if colour_order1 == 1:
    win.flip()
    endspractice_b1j.draw()
    endspractice_b2.draw()
    endspractice_bf.draw()
    win.flip()
elif colour_order1 == 2:
    win.flip()
    endspractice_b1j.draw()
    endspractice_o2.draw()
    endspractice_of.draw()
    win.flip()
keypressed = event.waitKeys(timeStamped=False)
checkclock01.reset()
        
for j in range(hst):
    # Select what condition is to be performed on experimental trials:
    if colour_order1 == 1:
        singleconditionsx = single_proportions[counter01s2]
    elif colour_order1 == 2:
        singleconditionsx = single_proportions[counter01s2]
        
    
    if pcounter > practicetrials:
        # Append the condition we're on:
        if singleconditionsx == 1:
            conused4.append('b,o')
            difflevel4.append('Easy 1')
        elif singleconditionsx == 2:
            conused4.append('B,o')
            difflevel4.append('Easy 2')
        elif singleconditionsx == 3:
            conused4.append('b,b')
            difflevel4.append('Hard 1')
        elif singleconditionsx == 4:
            conused4.append('B,b') 
            difflevel4.append('Hard 2')
        elif singleconditionsx == 5:
            conused4.append('o,b')
            difflevel4.append('Easy 1')
        elif singleconditionsx == 6:
            conused4.append('O,b')
            difflevel4.append('Easy 2')
        elif singleconditionsx == 7:
            conused4.append('o,b')
            difflevel4.append('Hard 1')
        elif singleconditionsx == 8:
            conused4.append('O,b') 
            difflevel4.append('Hard 2')
    
    # More BLUE Trials:
    if singleconditionsx == 1:
        p01 = .52#(52/48) PTASK - Easy
    elif singleconditionsx == 2:
        p01 = .66#(66/34) PTASK - EASY
    elif singleconditionsx == 3:
        p01 = .56#(56/44) JDTASK - HARD
    elif singleconditionsx == 4:
        p01 = .62#(62/38) JDTASK - HARD
        
    # More ORANGE Trials:
    elif singleconditionsx == 5:
        p01 = .52#(52/48) PTASK - Easy
    elif singleconditionsx == 6:
        p01 = .66#(66/34) PTASK - EASY
    elif singleconditionsx == 7:
        p01 = .56#(56/44) JDTASK - HARD
    elif singleconditionsx == 8:
        p01 = .62#(62/38) JDTASK - HARD
    
    
    # flash stimulus functions
    # flash initialization
    def flash_init(win, position01=[0,0], square_size=10, columns=20, rows=20, percent_color01=p01): # Colour2 being manipulated whic is BLUE
        global flash01s2 # The flash stimulus (an array of flashing squares)
        
        if singleconditionsx <= 4:
            color_set01 = [color2, color1] # color2 being manipulated which is the BLUE
        elif singleconditionsx >= 5:
            color_set01 = [color1, color2] # colour1 is being manipulated which is the ORANGE
        cell_number = columns * rows
    
        num_color4 = int(np.floor(float(cell_number)*percent_color01)) # First colour
        num_color5 = int(np.floor(float(cell_number)*(1-percent_color01))) # Second colour
        
        # fill an array with colors. Each color should appear approximatively the same number of times.
        f_colors3s2 = []
        for i in range(num_color4):
            f_colors3s2.append(color_set01[0])
        for i in range(num_color5):
            f_colors3s2.append(color_set01[1])
        numpy.random.shuffle(color_set01)
        i = cell_number - len(f_colors3s2)
        while i > 0:
            f_colors3s2.append(color_set01[i])
            i -= 1
        
        # randomize color order.
        shuffle(f_colors3s2)
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys.append((x_left + c * square_size, y_top + l * square_size))
        
        
        # fill an array with coordinate for each color square. First square should be at the upper left
        # and next should follow from left to right and up to down.
        xys2 = []
        x_left = (1 - columns) * square_size / 2
        y_top = (1 - rows) * square_size / 2
        for l in range(rows):
            for c in range(columns):
                xys2.append((x_left + c * square_size, y_top + l * square_size))
        
        # MAIN FUNCTION TO CREATE FIRST GRID
        flash01s2 = visual.ElementArrayStim(win=win,
                            fieldPos=position01,
                            fieldShape='sqr',
                            nElements=cell_number,
                            sizes=square_size,
                            xys=xys,
                            colors=f_colors3s2,
                            elementTex=None,
                            elementMask=None,
                            name='flash',
                            autoLog=False)
                            
                            
                            
    
    # flash stimulus change
    def flash_changes2():
        global flash01s2
        shuffle(flash01s2.colors)
        flash01s2.setColors(flash01s2.colors)
    
    # Time variables used during the experiment
    def set_timings2():
        global f_t 
        f_t = 5 # The duration (in frame) of a flash image presentation
    
    # data_init
    set_colors()
    set_sizes()
    set_positions01()
    set_timing()
    
    #############################
    # MAIN FUNCTION HERE
    flash_init(win, fl_p3, square_size=0.3, columns=20, rows=20) # set the parameters here for the function!!
    #############################
    
    # Initialize components for Routine "show_flash"
    show_flashClock01s2 = core.Clock()
    frame_fl = visual.ImageStim(win=win, name='frame_fl',
        image=None, mask=None,
        ori=0, pos=fl_p3, size=f_s,
        color=f_c, colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    
    # Create some handy timers
    globalClock01s2 = core.Clock()  # to track the time since experiment started
    routineTimer01s2 = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
    
    #------Prepare to start Routine "init_experiment"-------
    t = 0
    frameN = -1
    
    #------Prepare to start Routine "show_flash"-------
    t = 0
    show_flashClock01s2.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    
    # keep track of which components have finished
    show_flashComponents01s2 = []
    show_flashComponents01s2.append(frame_fl)
    for thisComponent in show_flashComponents01:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    ########################################################################################
    ########################################################################################
    
    
    ########################################################################################
    # MAIN EXPERIMENT
    ########################################################################################
    
    #---Start Routine "show_flash"-------
    continueRoutine = True
    while continueRoutine:    
        # Hides mouse
        mouse = event.Mouse(visible=0)
        
        # get current time
        t = show_flashClock01s2.getTime()
        #print("t =", t)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # update/draw components on each frame
        #print(frameN)
        
        # *frame_fl* updates
        if t >= 0.0 and frame_fl.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_fl.tStart = t  # underestimates by a little under one frame
            frame_fl.frameNStart = frameN  # exact frame index
            frame_fl.draw()
        # flash each frame
        if frameN >= f_change:
            flash_changes2()
            f_change+= f_t
#        if colour_order1 == 1:
#            strialtextb.draw()
#        elif colour_order1 == 2:
#            #strialtexto.draw()
        flash01s2.draw()  # First stimulus is drawn here
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer01s2.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_flashComponents01s2:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
                
        # RESPONSE 1: (Left Side - BLUE)
        if event.getKeys(keyList=["escape"]):
            win.flip()
            breaktext.draw()
            win.flip()
            keypressed = event.waitKeys(timeStamped=False)
            checkclock01s2.reset()
        if event.getKeys(keyList=["6"]):
            win.close()
            core.quit()
        if event.getKeys(keyList=["z"]): # HARD key
        
            # Update practice trial counter
            pcounters2 = pcounters2+1
            
            # print the condition we did
            print("actual single trial done =", singleconditionsx)
            
            # Track response times
            #rt = rtclock.getTime()
            time01s2 = checkclock01s2.getTime()
            RT4.append(time01s2)
            
            if singleconditionsx is 1 or singleconditionsx is 5 or singleconditionsx is 3 or singleconditionsx is 7 or singleconditionsx is 4 or singleconditionsx is 8:
                correctresponse4.append('1')
            else:
                correctresponse4.append('0')
            colourcolour4.append(colour_order1)
            
            # Keep track of keys pressed
            keyspressed4.append('left')
            
            # Update the counter
            counter01s2 = counter01s2+1
            
            # Keep track of trial number to be saved 
            trialNo4.append(counter01s2)
            
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(1.5) # Keep the cross on screen for 2 seconds
            checkclock01s2.reset()
            event.clearEvents(eventType='keyboard')
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter01s2 == hst:
                win.flip() # Clears the window
                endtext1.draw() # Draw ending message here
                win.flip()
                core.wait(5.0)
                win.flip()
                #####################################################################
                #Write Data To File
                #####################################################################
                
                # Write RESULTS To A File 
                os.chdir("JD_task_results") # move to folder called RESULTS, need to CREATE this if it does not exist already.
                fout = open(filename, 'w')
                fout.write('Trial Number, Response, Correct/Incorrect(1/0), RT, Condition, Difficulty, Colour Order:\n')
                for i in range(hst):
                    fout.write('%d\t'% trialNo[i],)
                    fout.write('%s\t'% keyspressed[i],)
                    fout.write('%s\t'% correctresponse[i],)
                    fout.write('%.3f\t'% RT[i],)
                    fout.write('%s\t'% conused[i],)
                    fout.write('%s\t'% difflevel[i],)
                    fout.write('%s\t\n'% colourcolour1[i],)
                    
#               fout.write('\n')
                for i in range(hst):
                    fout.write('%d\t'% trialNo2[i],)
                    fout.write('%s\t'% keyspressed2[i],)
                    fout.write('%s\t'% correctresponse2[i],)
                    fout.write('%.3f\t'% RT2[i],)
                    fout.write('%s\t'% conused2[i],)
                    fout.write('%s\t'% difflevel2[i],)
                    fout.write('%s\t\n'% colourcolour2[i],)
                
#               fout.write('\n')
                for i in range(hst):
                    fout.write('%d\t'% trialNo3[i],)
                    fout.write('%s\t'% keyspressed3[i],)
                    fout.write('%s\t'% correctresponse3[i],)
                    fout.write('%.3f\t'% RT3[i],)
                    fout.write('%s\t'% conused3[i],)
                    fout.write('%s\t'% difflevel3[i],)
                    fout.write('%s\t\n'% colourcolour3[i],)
                    
#               fout.write('\n')
                for i in range(hst):
                    fout.write('%d\t'% trialNo4[i],)
                    fout.write('%s\t'% keyspressed4[i],)
                    fout.write('%s\t'% correctresponse4[i],)
                    fout.write('%.3f\t'% RT4[i],)
                    fout.write('%s\t'% conused4[i],)
                    fout.write('%s\t'% difflevel4[i],)
                    fout.write('%s\t\n'% colourcolour4[i],)
                
                # Close the results data file
                fout.close()
                
                #Say Where Results Are Written & If Experiment Successful
                print('Results Written To File Called ' + filename) 
                print('Program Completed Successfuly.')
                ####################################################################
                ####################################################################
                
                win.close()
                core.quit()
            break # End the expriment
            
         # RESPONSE 2: (Right Side - ORANGE)
        if event.getKeys(keyList=["m"]): # EASY key
            
            
            # Update practice trial counter
            pcounters2 = pcounters2+1
            
            # print the condition we did
            print("actual single trial done =", singleconditionsx)
            
            time01s2 = checkclock01s2.getTime()
            RT4.append(time01s2)
            
            
            
            if singleconditionsx is 2 or singleconditionsx is 6:
                correctresponse4.append('1')
            else:
                correctresponse4.append('0')
            # Append which colour question was being asked:
            colourcolour4.append(colour_order1)
            
            
            
            # Keep track of keys pressed
            keyspressed4.append('right')
            
            # Update the counter
            counter01s2 = counter01s2+1
            
            # Keep track of trial number to be saved 
            trialNo4.append(counter01s2)
            
            
            # DRAW FIXATION CROSS AFTER EACH TRIAL
            win.flip() # Clears the window
            fcross.draw() # Draw the fixation cross
            win.flip() # Clears the window
            core.wait(1.5) # Keep the cross on screen for 2 seconds
            checkclock01s2.reset()
            event.clearEvents(eventType='keyboard')
            
            # END THE EXPERIMENT HERE AND SAVE DATA
            if counter01s2 == hst:
                win.flip() # Clears the window
                endtext1.draw() # Draw ending message herehe window
                win.flip()
                core.wait(5.0)
                win.flip()
                #nowbreak = nowbreak+1
                #####################################################################
                #Write Data To File
                #####################################################################
                
                # Write RESULTS To A File 
                os.chdir("JD_task_results") # move to folder called RESULTS, need to CREATE this if it does not exist already.
                fout = open(filename, 'w')
                fout.write('Trial Number, Response, Correct/Incorrect(1/0), RT, Condition, Difficulty, Colour Order:\n')
                for i in range(hst):
                    fout.write('%d\t'% trialNo[i],)
                    fout.write('%s\t'% keyspressed[i],)
                    fout.write('%s\t'% correctresponse[i],)
                    fout.write('%.3f\t'% RT[i],)
                    fout.write('%s\t'% conused[i],)
                    fout.write('%s\t'% difflevel[i],)
                    fout.write('%s\t\n'% colourcolour1[i],)
                    
#               fout.write('\n')
                for i in range(hst):
                    fout.write('%d\t'% trialNo2[i],)
                    fout.write('%s\t'% keyspressed2[i],)
                    fout.write('%s\t'% correctresponse2[i],)
                    fout.write('%.3f\t'% RT2[i],)
                    fout.write('%s\t'% conused2[i],)
                    fout.write('%s\t'% difflevel2[i],)
                    fout.write('%s\t\n'% colourcolour2[i],)
                
#               fout.write('\n')
                for i in range(hst):
                    fout.write('%d\t'% trialNo3[i],)
                    fout.write('%s\t'% keyspressed3[i],)
                    fout.write('%s\t'% correctresponse3[i],)
                    fout.write('%.3f\t'% RT3[i],)
                    fout.write('%s\t'% conused3[i],)
                    fout.write('%s\t'% difflevel3[i],)
                    fout.write('%s\t\n'% colourcolour3[i],)
                    
#                fout.write('\n')
                for i in range(hst):
                    fout.write('%d\t'% trialNo4[i],)
                    fout.write('%s\t'% keyspressed4[i],)
                    fout.write('%s\t'% correctresponse4[i],)
                    fout.write('%.3f\t'% RT4[i],)
                    fout.write('%s\t'% conused4[i],)
                    fout.write('%s\t'% difflevel4[i],)
                    fout.write('%s\t\n'% colourcolour4[i],)
                
                # Close the results data file
                fout.close()
                
                #Say Where Results Are Written & If Experiment Successful
                print('Results Written To File Called ' + filename) 
                print('Program Completed Successfuly.')
                ####################################################################
                ####################################################################
                
                win.close()
                core.quit()
            break # End the expriment
            
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
         
        # END THE EXPERIMENT HERE:
        if counter01s2 == hst:
            break
            
            
#-------Ending Routine "show_flash"-------
for thisComponent in show_flashComponents01s2:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
########################################################################################
########################################################################################
