from datetime import datetime, timedelta

class TimeTool:
    def __init__(self, date_string):
        self.date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

    def add_time(self, hours=0, minutes=0, seconds=0):
        delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        self.date += delta

    def subtract_time(self, hours=0, minutes=0, seconds=0):
        delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        self.date -= delta

    def convert_format(self, format_string):
        return self.date.strftime(format_string)

# 使用示例
time_tool = TimeTool('2023-05-27 12:00:00')
print(time_tool.convert_format('%Y-%m-%d %H:%M:%S'))  # 原始格式
time_tool.add_time(2, 30, 0)  # 增加2小时30分钟
print(time_tool.convert_format('%Y-%m-%d %H:%M:%S'))  # 增加后的时间
time_tool.subtract_time(1, 0, 0)  # 减去1小时
print(time_tool.convert_format('%Y-%m-%d %H:%M:%S'))  # 减去后的时间
print(time_tool.convert_format('%d %B %Y'))  # 转换为其他格式