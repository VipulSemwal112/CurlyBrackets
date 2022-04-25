/************************* 
 * Eyetrackingstudy Test *
 *************************/


// store info about the experiment session:
let expName = 'EyeTrackingStudy';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001', 'use_eyetracking': False};

// Start code blocks for 'Before Experiment'
import * as matplotlib from 'matplotlib';
import * as plt from 'matplotlib/pyplot';
var use_eeg, use_eyetracker;
matplotlib.use("TKAgg");
use_eyetracker = false;
use_eeg = false;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.2, 0, 0.5]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Code_intialRoutineBegin());
flowScheduler.add(Code_intialRoutineEachFrame());
flowScheduler.add(Code_intialRoutineEnd());
flowScheduler.add(Welcome_ScreenRoutineBegin());
flowScheduler.add(Welcome_ScreenRoutineEachFrame());
flowScheduler.add(Welcome_ScreenRoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
flowScheduler.add(Study_StructureRoutineBegin());
flowScheduler.add(Study_StructureRoutineEachFrame());
flowScheduler.add(Study_StructureRoutineEnd());
flowScheduler.add(Start_TaskRoutineBegin());
flowScheduler.add(Start_TaskRoutineEachFrame());
flowScheduler.add(Start_TaskRoutineEnd());
flowScheduler.add(EEG_SetupRoutineBegin());
flowScheduler.add(EEG_SetupRoutineEachFrame());
flowScheduler.add(EEG_SetupRoutineEnd());
flowScheduler.add(Index_update3RoutineBegin());
flowScheduler.add(Index_update3RoutineEachFrame());
flowScheduler.add(Index_update3RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(EEGRoutineBegin());
flowScheduler.add(EEGRoutineEachFrame());
flowScheduler.add(EEGRoutineEnd());
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "Code_intial"
  Code_intialClock = new util.Clock();
  import * as pd from 'pandas';
  import * as random from 'random';
  var All_list, df, list1, list2, list3;
  df = pd.read_csv("Snippets_project.csv");
  list1 = df["Snippet_path"].slice(0, 8);
  list2 = df["Snippet_path"].slice(8, 16);
  list3 = df["Snippet_path"].slice(16, 24);
  All_list = [list1, list2, list3];
  
  // Initialize components for Routine "Welcome_Screen"
  Welcome_ScreenClock = new util.Clock();
  Introduction = new visual.TextStim({
    win: psychoJS.window,
    name: 'Introduction',
    text: 'Welcome to “ An Eye tracking study to Investigate the Effect of Curly brackets in Programming Comprehension” study \n\nThank you for participating in this study.\n\n\nPlease press <spacebar to continue>',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  EndTaskKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions',
    text: 'The experiment we are going to do shortly is an Eye tracking study for code comprehension. \n\nYour task is to comprehend multiple code snippets which will present to you shortly , after that you have to figure out the output of the code.\n\n\nPress <spacebar> to continue.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  KyeNext = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Study_Structure"
  Study_StructureClock = new util.Clock();
  introduction2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'introduction2',
    text: '\nThe code snippests are going to be in Java. The Snippets includes If/else statements , for loops , for each loop, Basic of OOP(Objeect Oriented Programming) , but do not bother about difficulty level of programms are really simple and interesting.\n\nPlease Enter your Responses as in the same was as mentioned. \n\nPress <spacebar> to continue.\n\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  SpaceBar = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Start_Task"
  Start_TaskClock = new util.Clock();
  text_start = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_start',
    text: 'So now everything looks great. Now we are going to strart our Study\n\nAll The Best!!\n\n\nPress <spacebar> to continue..',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  srart_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EEG_Setup"
  EEG_SetupClock = new util.Clock();
  // Initialize components for Routine "Index_update3"
  Index_update3Clock = new util.Clock();
  // Initialize components for Routine "Update_Index"
  Update_IndexClock = new util.Clock();
  // Initialize components for Routine "Task"
  TaskClock = new util.Clock();
  key_resp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -2.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Press < spacebar > to continue ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 1)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "user"
  userClock = new util.Clock();
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  A = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'A',
    text: '',
    pos: [0, 0.1], letterHeight: 0.05,
    size: null
  });
  A.clock = new util.Clock();
  
  B = new visual.ButtonStim({
    win: psychoJS.window,
    name: 'B',
    text: '',
    pos: [0, (- 0.1)], letterHeight: 0.05,
    size: null
  });
  B.clock = new util.Clock();
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Choose your Output',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.07), 0.33], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "EEG"
  EEGClock = new util.Clock();
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thank you for your participation. \n\n\nPress <spacebar> to exit',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function Code_intialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Code_intial'-------
    t = 0;
    Code_intialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    Code_intialComponents = [];
    
    Code_intialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Code_intialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Code_intial'-------
    // get current time
    t = Code_intialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Code_intialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Code_intialRoutineEnd() {
  return async function () {
    //------Ending Routine 'Code_intial'-------
    Code_intialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Code_intial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function Welcome_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Welcome_Screen'-------
    t = 0;
    Welcome_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    EndTaskKey.keys = undefined;
    EndTaskKey.rt = undefined;
    _EndTaskKey_allKeys = [];
    // keep track of which components have finished
    Welcome_ScreenComponents = [];
    Welcome_ScreenComponents.push(Introduction);
    Welcome_ScreenComponents.push(EndTaskKey);
    
    Welcome_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Welcome_ScreenRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Welcome_Screen'-------
    // get current time
    t = Welcome_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Introduction* updates
    if (t >= 0.0 && Introduction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Introduction.tStart = t;  // (not accounting for frame time here)
      Introduction.frameNStart = frameN;  // exact frame index
      
      Introduction.setAutoDraw(true);
    }

    
    // *EndTaskKey* updates
    if (t >= 0.0 && EndTaskKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndTaskKey.tStart = t;  // (not accounting for frame time here)
      EndTaskKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { EndTaskKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { EndTaskKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { EndTaskKey.clearEvents(); });
    }

    if (EndTaskKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = EndTaskKey.getKeys({keyList: ['space'], waitRelease: false});
      _EndTaskKey_allKeys = _EndTaskKey_allKeys.concat(theseKeys);
      if (_EndTaskKey_allKeys.length > 0) {
        EndTaskKey.keys = _EndTaskKey_allKeys[_EndTaskKey_allKeys.length - 1].name;  // just the last key pressed
        EndTaskKey.rt = _EndTaskKey_allKeys[_EndTaskKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Welcome_ScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Welcome_ScreenRoutineEnd() {
  return async function () {
    //------Ending Routine 'Welcome_Screen'-------
    Welcome_ScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('EndTaskKey.keys', EndTaskKey.keys);
    if (typeof EndTaskKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('EndTaskKey.rt', EndTaskKey.rt);
        routineTimer.reset();
        }
    
    EndTaskKey.stop();
    // the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Instructions'-------
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    KyeNext.keys = undefined;
    KyeNext.rt = undefined;
    _KyeNext_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(instructions);
    InstructionsComponents.push(KyeNext);
    
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function InstructionsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Instructions'-------
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions* updates
    if (t >= 0.0 && instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions.tStart = t;  // (not accounting for frame time here)
      instructions.frameNStart = frameN;  // exact frame index
      
      instructions.setAutoDraw(true);
    }

    
    // *KyeNext* updates
    if (t >= 0.0 && KyeNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      KyeNext.tStart = t;  // (not accounting for frame time here)
      KyeNext.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { KyeNext.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { KyeNext.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { KyeNext.clearEvents(); });
    }

    if (KyeNext.status === PsychoJS.Status.STARTED) {
      let theseKeys = KyeNext.getKeys({keyList: ['space'], waitRelease: false});
      _KyeNext_allKeys = _KyeNext_allKeys.concat(theseKeys);
      if (_KyeNext_allKeys.length > 0) {
        KyeNext.keys = _KyeNext_allKeys[_KyeNext_allKeys.length - 1].name;  // just the last key pressed
        KyeNext.rt = _KyeNext_allKeys[_KyeNext_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function InstructionsRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instructions'-------
    InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('KyeNext.keys', KyeNext.keys);
    if (typeof KyeNext.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('KyeNext.rt', KyeNext.rt);
        routineTimer.reset();
        }
    
    KyeNext.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function Study_StructureRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Study_Structure'-------
    t = 0;
    Study_StructureClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    SpaceBar.keys = undefined;
    SpaceBar.rt = undefined;
    _SpaceBar_allKeys = [];
    // keep track of which components have finished
    Study_StructureComponents = [];
    Study_StructureComponents.push(introduction2);
    Study_StructureComponents.push(SpaceBar);
    
    Study_StructureComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Study_StructureRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Study_Structure'-------
    // get current time
    t = Study_StructureClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *introduction2* updates
    if (t >= 0.0 && introduction2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      introduction2.tStart = t;  // (not accounting for frame time here)
      introduction2.frameNStart = frameN;  // exact frame index
      
      introduction2.setAutoDraw(true);
    }

    
    // *SpaceBar* updates
    if (t >= 0.0 && SpaceBar.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SpaceBar.tStart = t;  // (not accounting for frame time here)
      SpaceBar.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SpaceBar.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SpaceBar.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SpaceBar.clearEvents(); });
    }

    if (SpaceBar.status === PsychoJS.Status.STARTED) {
      let theseKeys = SpaceBar.getKeys({keyList: ['space'], waitRelease: false});
      _SpaceBar_allKeys = _SpaceBar_allKeys.concat(theseKeys);
      if (_SpaceBar_allKeys.length > 0) {
        SpaceBar.keys = _SpaceBar_allKeys[_SpaceBar_allKeys.length - 1].name;  // just the last key pressed
        SpaceBar.rt = _SpaceBar_allKeys[_SpaceBar_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Study_StructureComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Study_StructureRoutineEnd() {
  return async function () {
    //------Ending Routine 'Study_Structure'-------
    Study_StructureComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('SpaceBar.keys', SpaceBar.keys);
    if (typeof SpaceBar.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('SpaceBar.rt', SpaceBar.rt);
        routineTimer.reset();
        }
    
    SpaceBar.stop();
    // the Routine "Study_Structure" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function Start_TaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Start_Task'-------
    t = 0;
    Start_TaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    srart_key.keys = undefined;
    srart_key.rt = undefined;
    _srart_key_allKeys = [];
    // keep track of which components have finished
    Start_TaskComponents = [];
    Start_TaskComponents.push(text_start);
    Start_TaskComponents.push(srart_key);
    
    Start_TaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Start_TaskRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Start_Task'-------
    // get current time
    t = Start_TaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_start* updates
    if (t >= 0.0 && text_start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_start.tStart = t;  // (not accounting for frame time here)
      text_start.frameNStart = frameN;  // exact frame index
      
      text_start.setAutoDraw(true);
    }

    
    // *srart_key* updates
    if (t >= 0.0 && srart_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      srart_key.tStart = t;  // (not accounting for frame time here)
      srart_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { srart_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { srart_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { srart_key.clearEvents(); });
    }

    if (srart_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = srart_key.getKeys({keyList: ['space'], waitRelease: false});
      _srart_key_allKeys = _srart_key_allKeys.concat(theseKeys);
      if (_srart_key_allKeys.length > 0) {
        srart_key.keys = _srart_key_allKeys[_srart_key_allKeys.length - 1].name;  // just the last key pressed
        srart_key.rt = _srart_key_allKeys[_srart_key_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Start_TaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Start_TaskRoutineEnd() {
  return async function () {
    //------Ending Routine 'Start_Task'-------
    Start_TaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('srart_key.keys', srart_key.keys);
    if (typeof srart_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('srart_key.rt', srart_key.rt);
        routineTimer.reset();
        }
    
    srart_key.stop();
    // the Routine "Start_Task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function EEG_SetupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'EEG_Setup'-------
    t = 0;
    EEG_SetupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    eeg_rec = null;
    logger = null;
    if ((use_eeg === true)) {
        import {LiveAmpRecorder as Recorder} from 'EEGTools/Recorders/LiveAmpRecorder/liveamp_recorder';
        eeg_rec = new Recorder();
        eeg_rec.connect();
    }
    if ((use_eyetracker === true)) {
        import {Logger} from 'EyetrackerUtils/base_functionalities/logger';
        logger = new Logger(".\\data\\eye_tracking_data.csv");
        logger.add_key_to_log("left_gaze_point_in_user_coordinate_system");
        logger.add_key_to_log("left_gaze_point_validity");
        logger.add_key_to_log("right_gaze_point_validity");
        logger.add_key_to_log("right_gaze_point_in_user_coordinate_system");
        logger.add_key_to_log("left_gaze_origin_in_user_coordinate_system");
        logger.add_key_to_log("right_gaze_origin_in_user_coordinate_system");
        logger.add_key_to_log("left_gaze_point_on_display_area");
        logger.add_key_to_log("right_gaze_point_on_display_area");
        logger.add_key_to_log("system_time_stamp");
        logger.add_key_to_log("left_pupil_diameter");
        logger.add_key_to_log("right_pupil_diameter");
    }
    if ((use_eeg === true)) {
        eeg_rec.start_recording();
    }
    if ((use_eyetracker === true)) {
        logger.start_recording();
    }
    
    // keep track of which components have finished
    EEG_SetupComponents = [];
    
    EEG_SetupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function EEG_SetupRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'EEG_Setup'-------
    // get current time
    t = EEG_SetupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EEG_SetupComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EEG_SetupRoutineEnd() {
  return async function () {
    //------Ending Routine 'EEG_Setup'-------
    EEG_SetupComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "EEG_Setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function Index_update3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Index_update3'-------
    t = 0;
    Index_update3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    random.choice(number_list);
    
    // keep track of which components have finished
    Index_update3Components = [];
    
    Index_update3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Index_update3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Index_update3'-------
    // get current time
    t = Index_update3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Index_update3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Index_update3RoutineEnd() {
  return async function () {
    //------Ending Routine 'Index_update3'-------
    Index_update3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Index_update3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 16, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      trialsLoopScheduler.add(trials_2LoopScheduler);
      trialsLoopScheduler.add(trials_2LoopEnd);
      trialsLoopScheduler.add(userRoutineBegin(snapshot));
      trialsLoopScheduler.add(userRoutineEachFrame());
      trialsLoopScheduler.add(userRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      const snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(Update_IndexRoutineBegin(snapshot));
      trials_2LoopScheduler.add(Update_IndexRoutineEachFrame());
      trials_2LoopScheduler.add(Update_IndexRoutineEnd());
      trials_2LoopScheduler.add(TaskRoutineBegin(snapshot));
      trials_2LoopScheduler.add(TaskRoutineEachFrame());
      trials_2LoopScheduler.add(TaskRoutineEnd());
      trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}

async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

function Update_IndexRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Update_Index'-------
    t = 0;
    Update_IndexClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    Update_IndexComponents = [];
    
    Update_IndexComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function Update_IndexRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Update_Index'-------
    // get current time
    t = Update_IndexClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Update_IndexComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function Update_IndexRoutineEnd() {
  return async function () {
    //------Ending Routine 'Update_Index'-------
    Update_IndexComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Update_Index" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function TaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Task'-------
    t = 0;
    TaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp2.keys = undefined;
    key_resp2.rt = undefined;
    _key_resp2_allKeys = [];
    image.setImage(all_list[Current_index2][Current_index]);
    // keep track of which components have finished
    TaskComponents = [];
    TaskComponents.push(key_resp2);
    TaskComponents.push(image);
    TaskComponents.push(text_2);
    
    TaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function TaskRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Task'-------
    // get current time
    t = TaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp2* updates
    if (t >= 0.0 && key_resp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp2.tStart = t;  // (not accounting for frame time here)
      key_resp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp2.clearEvents(); });
    }

    if (key_resp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp2_allKeys = _key_resp2_allKeys.concat(theseKeys);
      if (_key_resp2_allKeys.length > 0) {
        key_resp2.keys = _key_resp2_allKeys[_key_resp2_allKeys.length - 1].name;  // just the last key pressed
        key_resp2.rt = _key_resp2_allKeys[_key_resp2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function TaskRoutineEnd() {
  return async function () {
    //------Ending Routine 'Task'-------
    TaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp2.keys', key_resp2.keys);
    if (typeof key_resp2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp2.rt', key_resp2.rt);
        routineTimer.reset();
        }
    
    key_resp2.stop();
    // the Routine "Task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function userRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'user'-------
    t = 0;
    userClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    A.setText(df3.iloc[Current_index]["Value1"]);
    B.setText(df3.iloc[Current_index]["Value2"]);
    // keep track of which components have finished
    userComponents = [];
    userComponents.push(mouse);
    userComponents.push(A);
    userComponents.push(B);
    userComponents.push(text_3);
    
    userComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function userRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'user'-------
    // get current time
    t = userClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [A,B]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *A* updates
    if (t >= 0 && A.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      A.tStart = t;  // (not accounting for frame time here)
      A.frameNStart = frameN;  // exact frame index
      
      A.setAutoDraw(true);
    }

    if (A.status === PsychoJS.Status.STARTED) {
      // check whether A has been pressed
      if (A.isClicked) {
        if (!A.wasClicked) {
          // store time of first click
          A.timesOn.push(A.clock.getTime());
          // store time clicked until
          A.timesOff.push(A.clock.getTime());
        } else {
          // update time clicked until;
          A.timesOff[A.timesOff.length - 1] = A.clock.getTime();
        }
        if (!A.wasClicked) {
          df_answers.loc[df_answers.length] = [Current_index, df3.iloc[Current_index]["Value1"]];
        }
        // if A is still clicked next frame, it is not a new click
        A.wasClicked = true;
      } else {
        // if A is clicked next frame, it is a new click
        A.wasClicked = false
      }
    } else {
      // keep clock at 0 if A hasn't started / has finished
      A.clock.reset();
      // if A is clicked next frame, it is a new click
      A.wasClicked = false;
    }
    
    // *B* updates
    if (t >= 0 && B.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      B.tStart = t;  // (not accounting for frame time here)
      B.frameNStart = frameN;  // exact frame index
      
      B.setAutoDraw(true);
    }

    if (B.status === PsychoJS.Status.STARTED) {
      // check whether B has been pressed
      if (B.isClicked) {
        if (!B.wasClicked) {
          // store time of first click
          B.timesOn.push(B.clock.getTime());
          // store time clicked until
          B.timesOff.push(B.clock.getTime());
        } else {
          // update time clicked until;
          B.timesOff[B.timesOff.length - 1] = B.clock.getTime();
        }
        if (!B.wasClicked) {
          df_answers.loc[df_answers.length] = [Current_index, df3.iloc[Current_index]["Value2"]];
        }
        // if B is still clicked next frame, it is not a new click
        B.wasClicked = true;
      } else {
        // if B is clicked next frame, it is a new click
        B.wasClicked = false
      }
    } else {
      // keep clock at 0 if B hasn't started / has finished
      B.clock.reset();
      // if B is clicked next frame, it is a new click
      B.wasClicked = false;
    }
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    userComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function userRoutineEnd() {
  return async function () {
    //------Ending Routine 'user'-------
    userComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    if (mouse.clicked_name) {  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0])};
    
    // the Routine "user" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function EEGRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'EEG'-------
    t = 0;
    EEGClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if (use_eeg) {
        eeg_rec.refresh();
        eeg_rec.disconnect();
        eeg_rec.save("EEG_data_raw");
    }
    if (use_eyetracker) {
        logger.stop_recording();
    }
    
    // keep track of which components have finished
    EEGComponents = [];
    
    EEGComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function EEGRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'EEG'-------
    // get current time
    t = EEGClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EEGComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EEGRoutineEnd() {
  return async function () {
    //------Ending Routine 'EEG'-------
    EEGComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "EEG" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function EndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(text);
    EndComponents.push(key_resp_2);
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function EndRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'End'-------
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EndRoutineEnd() {
  return async function () {
    //------Ending Routine 'End'-------
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
