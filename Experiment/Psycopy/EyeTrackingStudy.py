#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Feb 23 01:11:51 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

use_eyetracker = False
use_eeg = False


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'EyeTrackingStudy'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'use_eyetracking': False}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/vipulsemwal/Desktop/Editing Final/FINAL/Psycopy  Final2/EyeTrackingStudy.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.2,0,0.5], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Code_intial"
Code_intialClock = core.Clock()
import pandas as pd
import random
from datetime import datetime

global df
global df3

df=pd.read_csv("./snippets/Final/Combi.csv",sep=';')
df3=pd.read_csv("./snippets/Final/Answers.csv",sep=";",error_bad_lines=False)



use_eyetracker = expInfo["use_eyetracking"]

list1 = df['Combination1']
list2 = df['Combination2']
list3 = df['Combination3']

all_list = [list1,list2,list3]


global df_timing
global df_answers
df_timing = pd.DataFrame(columns=["ImagePath", "StartTime", "EndTime"])
df_answers = pd.DataFrame(columns=["Index", "Answer"])


Current_index = None
Current_index2 = None

index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

index2 =[0,1,2]

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
Introduction = visual.TextStim(win=win, name='Introduction',
    text='Welcome to “ An Eye tracking study to Investigate the Effect of Curly brackets in Programming Comprehension” study \n\nThank you for participating in this study.\n\n\nPlease press <spacebar to continue>',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EndTaskKey = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='The experiment we are going to do shortly is an Eye tracking study for code comprehension. \n\nYour task is to comprehend multiple code snippets which will present to you shortly , after that you have to figure out the output of the code.\n\n\nPress <spacebar> to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KyeNext = keyboard.Keyboard()

# Initialize components for Routine "Study_Structure"
Study_StructureClock = core.Clock()
introduction2 = visual.TextStim(win=win, name='introduction2',
    text='\nThe code snippests are going to be in Java. The Snippets includes If/else statements , for loops , for each loop, Basic of OOP(Objeect Oriented Programming) , but do not bother about difficulty level of programms are really simple and interesting.\n\nPlease Enter your Responses as in the same was as mentioned. \n\nPress <spacebar> to continue.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
SpaceBar = keyboard.Keyboard()

# Initialize components for Routine "Start_Task"
Start_TaskClock = core.Clock()
text_start = visual.TextStim(win=win, name='text_start',
    text='So now everything looks great. Now we are going to strart our Study\n\nAll The Best!!\n\n\nPress <spacebar> to continue..',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
srart_key = keyboard.Keyboard()

# Initialize components for Routine "EEG_Setup"
EEG_SetupClock = core.Clock()

# Initialize components for Routine "Index_update3"
Index_update3Clock = core.Clock()

# Initialize components for Routine "Update_Index"
Update_IndexClock = core.Clock()

# Initialize components for Routine "Task"
TaskClock = core.Clock()
key_resp2 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0,0 ), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-2.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press < spacebar > to continue ',
    font='Open Sans',
    pos=(0,-1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "user"
userClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
A = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0, 0.1),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor='black', borderColor='darkblue',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='A'
)
A.buttonClock = core.Clock()
B = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(0, -0.1),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor='black', borderColor='darkblue',
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='B'
)
B.buttonClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Choose your Output',
    font='Open Sans',
    pos=(-0.07, 0.33), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "EEG"
EEGClock = core.Clock()

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for your participation. \n\n\nPress <spacebar> to exit',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Code_intial"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Code_intialComponents = []
for thisComponent in Code_intialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Code_intialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Code_intial"-------
while continueRoutine:
    # get current time
    t = Code_intialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Code_intialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Code_intialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Code_intial"-------
for thisComponent in Code_intialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Code_intial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome_Screen"-------
continueRoutine = True
# update component parameters for each repeat
EndTaskKey.keys = []
EndTaskKey.rt = []
_EndTaskKey_allKeys = []
# keep track of which components have finished
Welcome_ScreenComponents = [Introduction, EndTaskKey]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Introduction* updates
    if Introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Introduction.frameNStart = frameN  # exact frame index
        Introduction.tStart = t  # local t and not account for scr refresh
        Introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Introduction, 'tStartRefresh')  # time at next scr refresh
        Introduction.setAutoDraw(True)
    
    # *EndTaskKey* updates
    waitOnFlip = False
    if EndTaskKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndTaskKey.frameNStart = frameN  # exact frame index
        EndTaskKey.tStart = t  # local t and not account for scr refresh
        EndTaskKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndTaskKey, 'tStartRefresh')  # time at next scr refresh
        EndTaskKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EndTaskKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EndTaskKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EndTaskKey.status == STARTED and not waitOnFlip:
        theseKeys = EndTaskKey.getKeys(keyList=['space'], waitRelease=False)
        _EndTaskKey_allKeys.extend(theseKeys)
        if len(_EndTaskKey_allKeys):
            EndTaskKey.keys = _EndTaskKey_allKeys[-1].name  # just the last key pressed
            EndTaskKey.rt = _EndTaskKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Introduction.started', Introduction.tStartRefresh)
thisExp.addData('Introduction.stopped', Introduction.tStopRefresh)
# check responses
if EndTaskKey.keys in ['', [], None]:  # No response was made
    EndTaskKey.keys = None
thisExp.addData('EndTaskKey.keys',EndTaskKey.keys)
if EndTaskKey.keys != None:  # we had a response
    thisExp.addData('EndTaskKey.rt', EndTaskKey.rt)
thisExp.addData('EndTaskKey.started', EndTaskKey.tStartRefresh)
thisExp.addData('EndTaskKey.stopped', EndTaskKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
KyeNext.keys = []
KyeNext.rt = []
_KyeNext_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructions, KyeNext]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *KyeNext* updates
    waitOnFlip = False
    if KyeNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        KyeNext.frameNStart = frameN  # exact frame index
        KyeNext.tStart = t  # local t and not account for scr refresh
        KyeNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(KyeNext, 'tStartRefresh')  # time at next scr refresh
        KyeNext.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(KyeNext.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(KyeNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if KyeNext.status == STARTED and not waitOnFlip:
        theseKeys = KyeNext.getKeys(keyList=['space'], waitRelease=False)
        _KyeNext_allKeys.extend(theseKeys)
        if len(_KyeNext_allKeys):
            KyeNext.keys = _KyeNext_allKeys[-1].name  # just the last key pressed
            KyeNext.rt = _KyeNext_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if KyeNext.keys in ['', [], None]:  # No response was made
    KyeNext.keys = None
thisExp.addData('KyeNext.keys',KyeNext.keys)
if KyeNext.keys != None:  # we had a response
    thisExp.addData('KyeNext.rt', KyeNext.rt)
thisExp.addData('KyeNext.started', KyeNext.tStartRefresh)
thisExp.addData('KyeNext.stopped', KyeNext.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Study_Structure"-------
continueRoutine = True
# update component parameters for each repeat
SpaceBar.keys = []
SpaceBar.rt = []
_SpaceBar_allKeys = []
# keep track of which components have finished
Study_StructureComponents = [introduction2, SpaceBar]
for thisComponent in Study_StructureComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Study_StructureClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Study_Structure"-------
while continueRoutine:
    # get current time
    t = Study_StructureClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Study_StructureClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction2* updates
    if introduction2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction2.frameNStart = frameN  # exact frame index
        introduction2.tStart = t  # local t and not account for scr refresh
        introduction2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction2, 'tStartRefresh')  # time at next scr refresh
        introduction2.setAutoDraw(True)
    
    # *SpaceBar* updates
    waitOnFlip = False
    if SpaceBar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SpaceBar.frameNStart = frameN  # exact frame index
        SpaceBar.tStart = t  # local t and not account for scr refresh
        SpaceBar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SpaceBar, 'tStartRefresh')  # time at next scr refresh
        SpaceBar.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SpaceBar.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SpaceBar.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SpaceBar.status == STARTED and not waitOnFlip:
        theseKeys = SpaceBar.getKeys(keyList=['space'], waitRelease=False)
        _SpaceBar_allKeys.extend(theseKeys)
        if len(_SpaceBar_allKeys):
            SpaceBar.keys = _SpaceBar_allKeys[-1].name  # just the last key pressed
            SpaceBar.rt = _SpaceBar_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Study_StructureComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Study_Structure"-------
for thisComponent in Study_StructureComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction2.started', introduction2.tStartRefresh)
thisExp.addData('introduction2.stopped', introduction2.tStopRefresh)
# check responses
if SpaceBar.keys in ['', [], None]:  # No response was made
    SpaceBar.keys = None
thisExp.addData('SpaceBar.keys',SpaceBar.keys)
if SpaceBar.keys != None:  # we had a response
    thisExp.addData('SpaceBar.rt', SpaceBar.rt)
thisExp.addData('SpaceBar.started', SpaceBar.tStartRefresh)
thisExp.addData('SpaceBar.stopped', SpaceBar.tStopRefresh)
thisExp.nextEntry()
# the Routine "Study_Structure" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_Task"-------
continueRoutine = True
# update component parameters for each repeat
srart_key.keys = []
srart_key.rt = []
_srart_key_allKeys = []
# keep track of which components have finished
Start_TaskComponents = [text_start, srart_key]
for thisComponent in Start_TaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start_TaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start_Task"-------
while continueRoutine:
    # get current time
    t = Start_TaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start_TaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_start* updates
    if text_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_start.frameNStart = frameN  # exact frame index
        text_start.tStart = t  # local t and not account for scr refresh
        text_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_start, 'tStartRefresh')  # time at next scr refresh
        text_start.setAutoDraw(True)
    
    # *srart_key* updates
    waitOnFlip = False
    if srart_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        srart_key.frameNStart = frameN  # exact frame index
        srart_key.tStart = t  # local t and not account for scr refresh
        srart_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(srart_key, 'tStartRefresh')  # time at next scr refresh
        srart_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(srart_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(srart_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if srart_key.status == STARTED and not waitOnFlip:
        theseKeys = srart_key.getKeys(keyList=['space'], waitRelease=False)
        _srart_key_allKeys.extend(theseKeys)
        if len(_srart_key_allKeys):
            srart_key.keys = _srart_key_allKeys[-1].name  # just the last key pressed
            srart_key.rt = _srart_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_TaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_Task"-------
for thisComponent in Start_TaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_start.started', text_start.tStartRefresh)
thisExp.addData('text_start.stopped', text_start.tStopRefresh)
# check responses
if srart_key.keys in ['', [], None]:  # No response was made
    srart_key.keys = None
thisExp.addData('srart_key.keys',srart_key.keys)
if srart_key.keys != None:  # we had a response
    thisExp.addData('srart_key.rt', srart_key.rt)
thisExp.addData('srart_key.started', srart_key.tStartRefresh)
thisExp.addData('srart_key.stopped', srart_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start_Task" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EEG_Setup"-------
continueRoutine = True
# update component parameters for each repeat
eeg_rec = None
logger = None

if use_eeg==True:
    from EEGTools.Recorders.LiveAmpRecorder.liveamp_recorder import LiveAmpRecorder as Recorder
    eeg_rec = Recorder()
    eeg_rec.connect()
    
if use_eyetracker==True:
    from EyetrackerUtils.base_functionalities.logger import Logger
    logger = Logger(".\\data\\eye_tracking_data_" + expInfo['session'] + " _ " + expInfo['participant'] + ".csv")
    logger.add_key_to_log('left_gaze_point_validity')
    logger.add_key_to_log('right_gaze_point_validity')
    logger.add_key_to_log('left_gaze_point_on_display_area')
    logger.add_key_to_log('right_gaze_point_on_display_area')
    logger.add_key_to_log('system_time_stamp')
    logger.add_key_to_log('left_pupil_diameter')
    logger.add_key_to_log('right_pupil_diameter')

    
if use_eeg==True:
    eeg_rec.start_recording()
    
if use_eyetracker==True:
    logger.start_recording()   
    
global start_of_eyetracking
start_of_eyetracking = datetime.now()
start_of_eyetracking = datetime.timestamp(start_of_eyetracking)
# keep track of which components have finished
EEG_SetupComponents = []
for thisComponent in EEG_SetupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EEG_SetupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EEG_Setup"-------
while continueRoutine:
    # get current time
    t = EEG_SetupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EEG_SetupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EEG_SetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EEG_Setup"-------
for thisComponent in EEG_SetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EEG_Setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Index_update3"-------
continueRoutine = True
# update component parameters for each repeat


Current_index2 = index2.pop(0)
Current_index2 = index2.pop(0)
Current_index2 = index2.pop(0)


# if 1 active - Combination 1

# if 2 active - Combination 2

# if all active - Combination 3


# keep track of which components have finished
Index_update3Components = []
for thisComponent in Index_update3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Index_update3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Index_update3"-------
while continueRoutine:
    # get current time
    t = Index_update3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Index_update3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Index_update3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Index_update3"-------
for thisComponent in Index_update3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Index_update3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=16.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=2.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Update_Index"-------
        continueRoutine = True
        # update component parameters for each repeat
        if len(index)>0:
            Current_index = index.pop(0)
        else:
            break
        # keep track of which components have finished
        Update_IndexComponents = []
        for thisComponent in Update_IndexComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Update_IndexClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Update_Index"-------
        while continueRoutine:
            # get current time
            t = Update_IndexClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Update_IndexClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Update_IndexComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Update_Index"-------
        for thisComponent in Update_IndexComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Update_Index" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Task"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp2.keys = []
        key_resp2.rt = []
        _key_resp2_allKeys = []
        #print(all_list[Current_index2][Current_index])
        start_of_eyetracking
        current_time_start = datetime.now()
        current_time_start = datetime.timestamp(current_time_start) - start_of_eyetracking 
        
        image_path = all_list[Current_index2][Current_index]
        
        print("Start Time Stamp: ")
        print(current_time_start)
        
        
        image.setImage(all_list[Current_index2][Current_index])
        # keep track of which components have finished
        TaskComponents = [key_resp2, image, text_2]
        for thisComponent in TaskComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Task"-------
        while continueRoutine:
            # get current time
            t = TaskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TaskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp2* updates
            waitOnFlip = False
            if key_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp2.frameNStart = frameN  # exact frame index
                key_resp2.tStart = t  # local t and not account for scr refresh
                key_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
                key_resp2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp2.getKeys(keyList=['space'], waitRelease=False)
                _key_resp2_allKeys.extend(theseKeys)
                if len(_key_resp2_allKeys):
                    key_resp2.keys = _key_resp2_allKeys[-1].name  # just the last key pressed
                    key_resp2.rt = _key_resp2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Task"-------
        for thisComponent in TaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp2.keys in ['', [], None]:  # No response was made
            key_resp2.keys = None
        trials_2.addData('key_resp2.keys',key_resp2.keys)
        if key_resp2.keys != None:  # we had a response
            trials_2.addData('key_resp2.rt', key_resp2.rt)
        trials_2.addData('key_resp2.started', key_resp2.tStartRefresh)
        trials_2.addData('key_resp2.stopped', key_resp2.tStopRefresh)
        start_of_eyetracking
        current_time_end = datetime.now()
        current_time_end = datetime.timestamp(current_time_end) - start_of_eyetracking
        
        df_timing.loc[len(df_timing)] = [image_path, current_time_start, current_time_end]
        print("End Time Stamp: ")
        print(current_time_end)
        trials_2.addData('image.started', image.tStartRefresh)
        trials_2.addData('image.stopped', image.tStopRefresh)
        trials_2.addData('text_2.started', text_2.tStartRefresh)
        trials_2.addData('text_2.stopped', text_2.tStopRefresh)
        # the Routine "Task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'trials_2'
    
    
    # ------Prepare to start Routine "user"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    A.setText(df3.iloc[Current_index]["Value1"])
    B.setText(df3.iloc[Current_index]["Value2"])
    # keep track of which components have finished
    userComponents = [mouse, A, B, text_3]
    for thisComponent in userComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    userClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "user"-------
    while continueRoutine:
        # get current time
        t = userClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=userClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([A,B])
                        clickableList = [A,B]
                    except:
                        clickableList = [[A,B]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *A* updates
        if A.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            A.frameNStart = frameN  # exact frame index
            A.tStart = t  # local t and not account for scr refresh
            A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A, 'tStartRefresh')  # time at next scr refresh
            A.setAutoDraw(True)
        if A.status == STARTED:
            # check whether A has been pressed
            if A.isClicked:
                if not A.wasClicked:
                    A.timesOn.append(A.buttonClock.getTime()) # store time of first click
                    A.timesOff.append(A.buttonClock.getTime()) # store time clicked until
                else:
                    A.timesOff[-1] = A.buttonClock.getTime() # update time clicked until
                if not A.wasClicked:
                    df_answers.loc[len(df_answers)] = [Current_index, df3.iloc[Current_index]["Value1"]]
                A.wasClicked = True  # if A is still clicked next frame, it is not a new click
            else:
                A.wasClicked = False  # if A is clicked next frame, it is a new click
        else:
            A.wasClicked = False  # if A is clicked next frame, it is a new click
        
        # *B* updates
        if B.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            B.frameNStart = frameN  # exact frame index
            B.tStart = t  # local t and not account for scr refresh
            B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B, 'tStartRefresh')  # time at next scr refresh
            B.setAutoDraw(True)
        if B.status == STARTED:
            # check whether B has been pressed
            if B.isClicked:
                if not B.wasClicked:
                    B.timesOn.append(B.buttonClock.getTime()) # store time of first click
                    B.timesOff.append(B.buttonClock.getTime()) # store time clicked until
                else:
                    B.timesOff[-1] = B.buttonClock.getTime() # update time clicked until
                if not B.wasClicked:
                    df_answers.loc[len(df_answers)] = [Current_index, df3.iloc[Current_index]["Value2"]]
                B.wasClicked = True  # if B is still clicked next frame, it is not a new click
            else:
                B.wasClicked = False  # if B is clicked next frame, it is a new click
        else:
            B.wasClicked = False  # if B is clicked next frame, it is a new click
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in userComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "user"-------
    for thisComponent in userComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    if len(mouse.x): trials.addData('mouse.x', mouse.x[0])
    if len(mouse.y): trials.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): trials.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): trials.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): trials.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): trials.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    trials.addData('A.started', A.tStartRefresh)
    trials.addData('A.stopped', A.tStopRefresh)
    trials.addData('A.numClicks', A.numClicks)
    if A.numClicks:
       trials.addData('A.timesOn', A.timesOn)
       trials.addData('A.timesOff', A.timesOff)
    else:
       trials.addData('A.timesOn', "")
       trials.addData('A.timesOff', "")
    trials.addData('B.started', B.tStartRefresh)
    trials.addData('B.stopped', B.tStopRefresh)
    trials.addData('B.numClicks', B.numClicks)
    if B.numClicks:
       trials.addData('B.timesOn', B.timesOn)
       trials.addData('B.timesOff', B.timesOff)
    else:
       trials.addData('B.timesOn', "")
       trials.addData('B.timesOff', "")
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    # the Routine "user" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 16.0 repeats of 'trials'


# ------Prepare to start Routine "EEG"-------
continueRoutine = True
# update component parameters for each repeat
if use_eeg:
    eeg_rec.refresh()
    eeg_rec.disconnect()
    eeg_rec.save("EEG_data_raw")

if use_eyetracker:
    logger.stop_recording()
    
df_timing.to_csv(".\data\study_cutting_data_" + expInfo['session'].strip() + " _ " + expInfo['participant'].strip() + ".csv",sep=";")
df_answers.to_csv(".\data\study_answers_" + expInfo['session'].strip() + " _ " + expInfo['participant'].strip() + ".csv",sep=";")
# keep track of which components have finished
EEGComponents = []
for thisComponent in EEGComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EEGClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EEG"-------
while continueRoutine:
    # get current time
    t = EEGClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EEGClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EEGComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EEG"-------
for thisComponent in EEGComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "EEG" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
EndComponents = [text, key_resp_2]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
