#!/usr/bin/python
import os

#: current file path
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

#: data path which contains data file(s) and log file(s)
DATA_PATH = os.path.join(BASE_PATH, "data")

#: data file path for exam1
DATA_FILE = os.path.join(DATA_PATH, "data.json")
#: log file path for exam1
LOG_FILE = os.path.join(DATA_PATH, "a.log")

#: regex expression to extract from logs content
SEGMENT_PATTERN_DICT={
    "datetime": r"(?P<datetime>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})",
    #"datetime": r"(?P<datetime>[\d-:\s]+)",
    "sqlsentence": r"\"(?P<sqlsentence>.*)\"",
}
