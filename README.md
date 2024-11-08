# Mt5Csv-StatVis
Status: Alpha (do not use)

## Planner...
The options should be automated to be found through machine learning, adjusting visualization as it figures the best settings to use for the timeframe, the idea is the user specifies the timeframe, and the scripts analyze the data, and it finds and visualizes the patterns. The plan is to create a tool for visualizing and analyzing statistical information from CSV files exported from MetaTrader 5. The tool will include features for calculating SMMA and MACD, plotting data, and providing a WebUI for interaction. The main focus of the python project being visualization of the file>save output on given MetaTrader 5 pairs.

### Work Done:
- Created the launcher script (`run_main.sh`) to install requirements and manage persistent settings.
- Developed the main Python script (`main_script.py`) to load and process data.
- Implemented utility functions in `utility.py` for data processing and visualization.
- Created a WebUI using Flask in `interface.py` for user interaction.

### Work Remaining:
- Enhance the data processing and visualization capabilities.
- Implement additional statistical indicators and analysis tools.
- Improve the WebUI for better user experience and functionality.
- Ensure compatibility with various CSV formats exported from MetaTrader 5.

## Details:
- `Mt5Csv-StatVis` is a tool designed to visualize and analyze statistical data from CSV files exported from MetaTrader 5.
- The tool includes features for calculating SMMA and MACD indicators, plotting data, and providing a WebUI for interaction.

### Preview:
- Main Menu is like...
```
================================================================================
    Mt5Csv-StatVis
================================================================================

    1) Install Requirements
    2) Configure Settings
    3) Run Mt5Csv-StatVis

--------------------------------------------------------------------------------

    Data Directory:
./data
    Persistent Settings:
./data/persistence.json

================================================================================
Selection; Menu Options 1-3, Exit Program = X: 
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
Setting up virtual environment...
✓ Virtual environment created at ./data/venv

...

✓ Requirements installed successfully!
================================================================================
```

- Configuration Option...
```
================================================================================
    Configuration Menu
================================================================================

    1) Set Data File Path
    2) Set Strategy Timeframe
    3) Set SMMA Period
    4) Set MACD Fast Period
    5) Set MACD Slow Period
    6) Set MACD Signal Period
    7) Enable/Disable Display

--------------------------------------------------------------------------------

    Data File Path:
./data/exported_data.csv
    Strategy Timeframe:
M15_TIME
    SMMA Period:
100
    MACD Fast Period:
12
    MACD Slow Period:
26
    MACD Signal Period:
9
    Enable Display:
False

================================================================================
Selection; Menu Options = 1-7, Back to Main = B: 
```

## Links:
- [Mt5Csv-StatVis on GitHub](https://github.com/yourusername/Mt5Csv-StatVis)
- [MetaTrader 5](https://www.metatrader5.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)


## Notes:
- Funding: Kofi, Patreon

This README provides an overview of the `Mt5Csv-StatVis` project, including its current status, planned features, and a preview of the user interface. It also includes links to relevant resources for further information.
