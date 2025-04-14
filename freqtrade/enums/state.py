from enum import Enum


class State(Enum):
    """
    Bot application states
    """

    RUNNING = 1
    PAUSED = 2
    STOPPED = 3
    RELOAD_CONFIG = 4

    def __str__(self):
        state_names = {
            "RUNNING": "运行中",
            "PAUSED": "暂停",
            "STOPPED": "已停止",
            "RELOAD_CONFIG": "重新加载配置",
        }
        return state_names.get(self.name, f"{self.name.lower()}")
