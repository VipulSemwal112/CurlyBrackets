#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.1),
    on May 16, 2022, at 09:33
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




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.1'
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
    originPath='C:\\Users\\SE-Chair\\Documents\\GitHub\\CurlyBrackets\\Experiment-DataAnalysis\\EyeTrackingStudy_lastrun.py',
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
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
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
df4=pd.read_csv("./snippets/Final/Demo.csv")

use_eyetracker = expInfo["use_eyetracking"]

list1 = df['Combination1']
list2 = df['Combination2']
list3 = df['Combination3']

all_list = [list1,list2,list3]


global df_timing
global df_answers

df_timing = pd.DataFrame(columns=["ImagePath", "StartTime", "EndTime","ImageTime"])
df_answers = pd.DataFrame(columns=["Index", "Answer","StartTimeAnswer","EndTimeAnswer","AnswerTime"])



Current_index = None
Current_index2 = None

index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

index2 =[0,1,2]

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
Introduction = visual.TextStim(win=win, name='Introduction',
    text='Welcome to an Eye tracking study to Investigate the Effect of Curly brackets in Program Comprehension. \n\n\nPlease press <spacebar to continue>',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
EndTaskKey = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Thank you for participation in this survey.\n\nFirst of all,study will take about 30 minutes to complete. \n\nOver the following study you will be shown various snippets of source code in Java. This aims at testing your comprehension of the given algorithms. You will be asked to compute output after each snippets and click the correct output in given options.\n\n\nPlease Press <spacebar> to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
KyeNext = keyboard.Keyboard()

# Initialize components for Routine "Start_Task"
Start_TaskClock = core.Clock()
text_start = visual.TextStim(win=win, name='text_start',
    text='In this study you will see 8 snippets. The snippets will be shown in two parts, First part is going to be computational part of the snippet and in second you are going to see the main function.\n\nFirstly , you are going to see a demo programs with instructions. Please follow the instructions through further study.\n\nPlease Press <spacebar> to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
srart_key = keyboard.Keyboard()

# Initialize components for Routine "demo1"
demo1Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', units='pix', 
    image='snippets/Final/Demo.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "demo2"
demo2Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', units='pix', 
    image='snippets/Final/Demoresp.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1920, 1080),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Demo_Output"
Demo_OutputClock = core.Clock()
C = visual.ButtonStim(win, 
    text='Hellow,World', font='Arvo',
    pos=(0, 0.1),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor='white', borderColor='darkblue',
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='C'
)
C.buttonClock = core.Clock()
D = visual.ButtonStim(win, 
    text='World, Hellow', font='Arvo',
    pos=(0, -0.1),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor='white', borderColor='darkblue',
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='D'
)
D.buttonClock = core.Clock()
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Choose your output',
    font='Open Sans',
    pos=(-0.07, 0.33), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Start"
StartClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Now everything looks perfect. Lets begin the study.\n\nPlease press <spacebar> to continue..',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

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
    name='image', units='pix', 
    image='sin', mask=None,
    ori=0.0, pos=(0,0 ), size=1.0,
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
    fillColor='white', borderColor='darkblue',
    color='black', colorSpace='rgb',
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
    fillColor='white', borderColor='darkblue',
    color='black', colorSpace='rgb',
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
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "EEG"
EEGClock = core.Clock()

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for your participation. \n\n\nPress <spacebar> to exit',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
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

# ------Prepare to start Routine "demo1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
demo1Components = [image_3, key_resp_4]
for thisComponent in demo1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo1"-------
while continueRoutine:
    # get current time
    t = demo1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo1"-------
for thisComponent in demo1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "demo1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
demo2Components = [image_4, key_resp_5]
for thisComponent in demo2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo2"-------
while continueRoutine:
    # get current time
    t = demo2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo2"-------
for thisComponent in demo2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "demo2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Demo_Output"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Demo_OutputComponents = [C, D, mouse_2, text_5]
for thisComponent in Demo_OutputComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Demo_OutputClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Demo_Output"-------
while continueRoutine:
    # get current time
    t = Demo_OutputClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Demo_OutputClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *C* updates
    if C.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        C.frameNStart = frameN  # exact frame index
        C.tStart = t  # local t and not account for scr refresh
        C.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C, 'tStartRefresh')  # time at next scr refresh
        C.setAutoDraw(True)
    if C.status == STARTED:
        # check whether C has been pressed
        if C.isClicked:
            if not C.wasClicked:
                C.timesOn.append(C.buttonClock.getTime()) # store time of first click
                C.timesOff.append(C.buttonClock.getTime()) # store time clicked until
            else:
                C.timesOff[-1] = C.buttonClock.getTime() # update time clicked until
            if not C.wasClicked:
                continueRoutine = False  # end routine when C is clicked
                None
            C.wasClicked = True  # if C is still clicked next frame, it is not a new click
        else:
            C.wasClicked = False  # if C is clicked next frame, it is a new click
    else:
        C.wasClicked = False  # if C is clicked next frame, it is a new click
    
    # *D* updates
    if D.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        D.frameNStart = frameN  # exact frame index
        D.tStart = t  # local t and not account for scr refresh
        D.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(D, 'tStartRefresh')  # time at next scr refresh
        D.setAutoDraw(True)
    if D.status == STARTED:
        # check whether D has been pressed
        if D.isClicked:
            if not D.wasClicked:
                D.timesOn.append(D.buttonClock.getTime()) # store time of first click
                D.timesOff.append(D.buttonClock.getTime()) # store time clicked until
            else:
                D.timesOff[-1] = D.buttonClock.getTime() # update time clicked until
            if not D.wasClicked:
                continueRoutine = False  # end routine when D is clicked
                None
            D.wasClicked = True  # if D is still clicked next frame, it is not a new click
        else:
            D.wasClicked = False  # if D is clicked next frame, it is a new click
    else:
        D.wasClicked = False  # if D is clicked next frame, it is a new click
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([C,D])
                    clickableList = [C,D]
                except:
                    clickableList = [[C,D]]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Demo_OutputComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Demo_Output"-------
for thisComponent in Demo_OutputComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('C.started', C.tStartRefresh)
thisExp.addData('C.stopped', C.tStopRefresh)
thisExp.addData('C.numClicks', C.numClicks)
if C.numClicks:
   thisExp.addData('C.timesOn', C.timesOn)
   thisExp.addData('C.timesOff', C.timesOff)
else:
   thisExp.addData('C.timesOn', "")
   thisExp.addData('C.timesOff', "")
thisExp.addData('D.started', D.tStartRefresh)
thisExp.addData('D.stopped', D.tStopRefresh)
thisExp.addData('D.numClicks', D.numClicks)
if D.numClicks:
   thisExp.addData('D.timesOn', D.timesOn)
   thisExp.addData('D.timesOff', D.timesOff)
else:
   thisExp.addData('D.timesOn', "")
   thisExp.addData('D.timesOff', "")
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter([C,D])
        clickableList = [C,D]
    except:
        clickableList = [[C,D]]
    for obj in clickableList:
        if obj.contains(mouse_2):
            gotValidClick = True
            mouse_2.clicked_name.append(obj.name)
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
if len(mouse_2.clicked_name):
    thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "Demo_Output" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
StartComponents = [text_4, key_resp_3]
for thisComponent in StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start"-------
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EEG_Setup"-------
continueRoutine = True
# update component parameters for each repeat
global start_of_eyetracking
start_of_eyetracking = datetime.now()
start_of_eyetracking = datetime.timestamp(start_of_eyetracking)

logger = None

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

   
    
if use_eyetracker==True:
    logger.start_recording()   
    
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
        
        
        image.setSize((1920,1080))
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
        
        image_time = current_time_end-current_time_start
        df_timing.loc[len(df_timing)] = [image_path, current_time_start, current_time_end,image_time]
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
    
    # get names of stimulus parameters
    if trials_2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_2.trialList[0].keys()
    # save data for this loop
    trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
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
    start_of_eyetracking
    current_time_start = datetime.now()
    current_time_start = datetime.timestamp(current_time_start)- start_of_eyetracking 
    print("Start Time Stamp: ")
    print(current_time_start)
    
    answer_time= current_time_end-current_time_start
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
        start_of_eyetracking
        current_time_end = datetime.now()
        current_time_end = datetime.timestamp(current_time_end)- start_of_eyetracking
        answer_time= current_time_end-current_time_start
        
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
                    df_answers.loc[len(df_answers)] = [Current_index,df3.iloc[Current_index]["Value1"],current_time_start,current_time_end,answer_time]
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
                    df_answers.loc[len(df_answers)] = [Current_index,df3.iloc[Current_index]["Value2"],current_time_start,current_time_end,answer_time]
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
    start_of_eyetracking
    current_time_end = datetime.now()
    current_time_end = datetime.timestamp(current_time_end)- start_of_eyetracking
    
    answer_time= current_time_end-current_time_start
    
    #if mouse.clicked_name== 'A':
        #df_answers.loc[len(df_answers)] = [Current_index,answer_path1, current_time_start,current_time_end]
    #elif mouse.clicked_name== 'B':
        #df_answers.loc[len(df_answers)] = [Current_index,answer_path2, current_time_start,current_time_end]
        
    print("End Time Stamp: ")
    
    print(current_time_end)
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

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "EEG"-------
continueRoutine = True
# update component parameters for each repeat
if use_eyetracker:
    logger.stop_recording()
    
df_timing.to_csv(".\data\study_cutting_data_" + expInfo['session'].strip() + " _ " + expInfo['participant'].strip() + ".csv",sep=",")
df_answers.to_csv(".\data\study_answers_" + expInfo['session'].strip() + " _ " + expInfo['participant'].strip() + ".csv",sep=",")
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
