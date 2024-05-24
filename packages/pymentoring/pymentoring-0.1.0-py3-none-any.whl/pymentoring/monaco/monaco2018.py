import os
from collections import namedtuple
from datetime import datetime

Racer = namedtuple('Person', ['key', 'name', 'team', 'start', 'finish'])
LogItem = namedtuple('LogItem', ['key', 'date_time'])


class Monaco2018:
    def __init__(self, root_directory=os.getcwd()):
        self.data_directory = root_directory + "/data/"

    def build_table(self):
        racers = self.load_data(filename="abbreviations.txt", mapper=string_to_racer)
        time_logs = self.load_time_items()
        updated_racers = update_racers_time(time_logs, racers)
        table_data = prepare_table_data(updated_racers)
        return build_table_content(table_data)

    def load_time_items(self):
        all_logs = self.load_data(filename="start.log", mapper=string_to_log_item) + self.load_data(
            filename="end.log", mapper=string_to_log_item)
        sorted_logs_dict = create_items_dict(all_logs)
        sorted_logs_dict = {key: sorted(values) for key, values in sorted_logs_dict.items()}
        return sorted_logs_dict

    def load_data(self, filename: str, mapper):
        file_path = os.path.join(self.data_directory, filename)
        with open(file_path, 'r') as file:
            return [mapper(line.rstrip('\n')) for line in file if line]


def string_to_racer(racer_str: str) -> Racer:
    try:
        key, name, team = racer_str.split("_")
        return Racer(key, name, team, None, None)
    except Exception:
        raise ValueError("Invalid Racer record: {0}".format(racer_str))


def string_to_log_item(log_str: str) -> LogItem:
    try:
        timestamp_str = log_str[3:].replace('_', 'T')
        date_time = datetime.fromisoformat(timestamp_str)
        return LogItem(log_str[:3], date_time)
    except Exception:
        raise ValueError("Invalid Time record: {0}".format(log_str))


def create_items_dict(items):
    items_dict = {}
    for item in items:
        if item.key in items_dict:
            items_dict[item.key].append(item.date_time)
        else:
            items_dict[item.key] = [item.date_time]
    return items_dict


def update_racers_time(log_items_map, racers):
    updated_racers = []
    for racer in racers:
        times = log_items_map[racer.key]
        updated_racers.append(
            Racer(key=racer.key, name=racer.name, team=racer.team, start=times[0], finish=times[1])
        )
    return updated_racers


def format_time(time_delta):
    minutes, seconds = divmod(time_delta.seconds, 60)
    millis = round(time_delta.microseconds / 1000)
    time_str = f'{minutes:02}:{seconds:02}.{millis:03}'
    return time_str


def prepare_table_data(updated_racers):
    table_data = []
    for racer in updated_racers:
        best_lap_time_str = format_time(racer.finish - racer.start)
        table_data.append((racer.name, racer.team, best_lap_time_str))
    return sorted(table_data, key=lambda x: x[2])


def build_table_content(table_data):
    names, teams, best_lap_times = zip(*table_data)
    separator = "+------------------------------------------------------------------+\n"
    table_str = separator
    table_str += f"|{'Name':25}\t|{'Team':25}\t|{'Best Time':10}|\n"
    table_str += separator
    for i in range(len(table_data)):
        table_str += f"|{names[i]:25}\t|{teams[i]:25}\t|{best_lap_times[i]:10}|\n"
        if i == 10:
            table_str += separator
    table_str += separator
    return table_str
