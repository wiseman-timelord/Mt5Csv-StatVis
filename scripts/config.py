class Config:
    # Global Variables and Constants
    # ------------------------------
    # Path to the data file exported from MetaTrader 5
    DATA_FILE_PATH: str = "path/to/exported/data.csv"
    
    # Strategy Timeframe
    STRATEGY_TIMEFRAME: str = "M15_TIME"
    
    # SMMA Period
    SMMA_PERIOD: int = 100
    
    # MACD Fast Period
    MACD_FAST_PERIOD: int = 12
    
    # MACD Slow Period
    MACD_SLOW_PERIOD: int = 26
    
    # MACD Signal Period
    MACD_SIGNAL_PERIOD: int = 9
    
    # Enable Display
    ENABLE_DISPLAY: bool = False

    def __init__(self, persistence_data: dict):
        self._persistence_data = persistence_data
        self._browser = persistence_data.get('browser', '')
        self._settings = persistence_data.get('settings', {})

    @property
    def browser(self) -> str:
        return self._browser

    @property
    def settings(self) -> dict:
        return self._settings

    def get_config(self) -> dict:
        return {
            "data_file_path": self.DATA_FILE_PATH,
            "strategy_timeframe": self.STRATEGY_TIMEFRAME,
            "smma_period": self.SMMA_PERIOD,
            "macd_fast_period": self.MACD_FAST_PERIOD,
            "macd_slow_period": self.MACD_SLOW_PERIOD,
            "macd_signal_period": self.MACD_SIGNAL_PERIOD,
            "enable_display": self.ENABLE_DISPLAY,
            "browser": self.browser,
            "settings": self.settings,
        }