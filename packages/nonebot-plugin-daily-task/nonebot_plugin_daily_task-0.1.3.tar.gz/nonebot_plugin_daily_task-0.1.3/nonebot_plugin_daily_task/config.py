from pydantic import BaseModel, field_validator


class Config(BaseModel):
    daily_task_bot_id: str = "123456789"
    daily_task_db_name: str = "daily"
    daily_task_start_hour: int = 0
    daily_task_end_hour: int = 23
    daily_task_interval_hour: int = 2
    daily_task_priority: int = 10
    weather_plugin_enabled: bool = False

    @field_validator("daily_task_priority")
    @classmethod
    def check_priority(cls, v: int) -> int:
        if v >= 1:
            return v
        raise ValueError("daily task priority must greater than 1")
