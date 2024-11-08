# PhyData-Launcher
Status: Alpha (do not use)

## Planner...
The plan is to create agents with two models, optimized for thinking, coding, planning, GUI interaction, etc. The launcher will pre-configure GUI-based agents for planning and getting on with tasks involving interaction with applications, code, and research. The goal is to find the best configuration for the current models fitting within a dynamic number of layers to GPU, with the rest on system RAM.

### Work Done:
- Made the launcher to install the requirements following the information available from multiple sources. The launcher also enables configuration of launch commands and relevant paths, with persistence.

### Work Remaining:
- The main program requires specific functions/scripts to be modified, possibly with new ones added, to work with the best solution for local models through built-in llama-cpp-python. Find relevant files and figure out.
- When relevant files are figured out, modify those files, delete all other files in the fork to clean up, and make them into drop-in files for PhiData.
- Nemotron GGUF without matrix supposedly works on AMD GPU. If not, revert to possibly one model through Llama 3.2. Otherwise, decide to go for another model. This would have to be figured out for optimally 64GB system RAM + 8GB GPU, possibly multiple smaller DeepSeek 2.5 models?
- Data visualization would be nice.

## Details:
- It's a launcher for PhiData, and maybe some additional files. The plan is to get `Llama 3.1 70B NemoTron` and `Llama-3.1-Unhinged-Vision-8B-GGUF` working on PhiData, then try to make a drop-in mod for that and convenience.

### Preview:
- Main Menu is like...
```
================================================================================
    PhiData-Launch
================================================================================

    1) Install PhiData Requirements
    2) Configure Arguments and Settings
    3) Configure Models Used
    4) Run PhiData Now

--------------------------------------------------------------------------------

    VENV Location:
/media/mastar/Progs-Linux_250/Programs-External/PhiData/phidata-2.5.21/phidata-venv
    Models Used:
Llama-3.1-Nemotron-70B-Instruct-HF.Q4_K_M.gguf
Llama-3.1-Unhinged-Vision-8B-q8_0.gguf

================================================================================
Selection; Menu Options 1-4, Exit Program = X: 
```

- Install Option...
```
================================================================================
    Checking and Installing Prerequisites...
================================================================================
Checking Python 3...
✓ Python 3 installed and verified
--------------------------------------------------------------------------------
Checking pip...
✓ pip installed and verified
--------------------------------------------------------------------------------
Checking python3-venv...
✓ python3-venv installed and verified
--------------------------------------------------------------------------------
Checking git...
✓ git installed and verified
--------------------------------------------------------------------------------
Setting up PhiData virtual environment...
✓ Virtual environment created at /media/mastar/Progs-Linux_250/Programs-External/phidata-venv

...

✓ PhiData and dependencies installed successfully!
================================================================================
```

- Model Selection...
```
================================================================================
    Model Configuration Menu
================================================================================

    1) Set Instruct Model Path
    2) Set Visual Model Path

--------------------------------------------------------------------------------

    Instruct Model:
Llama-3.1-Nemotron-70B-Instruct-HF.Q4_K_M.gguf

    Visual Model:
Llama-3.1-Unhinged-Vision-8B-q8_0.gguf

================================================================================
Selection; Menu Options = 1-2, Back to Main = B: 
```

## Links:
- [PhiData on GitHub](https://github.com/phidatahq/phidata)
- [PhiData on local models](https://www.youtube.com/watch?v=T_P5wiJXkwk&pp)
- [PhiData](https://www.youtube.com/watch?v=d-Kh0SvgB6k&pp)

---

This README provides an overview of the PhyData-Launcher project, including its current status, planned features, and a preview of the user interface. It also includes links to relevant resources for further information.
