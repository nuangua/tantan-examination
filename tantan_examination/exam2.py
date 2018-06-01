#!/usr/bin/python

import re
from tantan_examination import config

if __name__ == "__main__":

    logging_data_dict = {}

    with open(config.LOG_FILE, 'rb') as handler:
        for line in handler:
            #print("#%s" % (line))
            _datetime = re.findall(config.SEGMENT_PATTERN_DICT["datetime"], line)
            #print(_datetime)
            _sqlsentence = re.findall(config.SEGMENT_PATTERN_DICT["sqlsentence"], line)
            #print(_sqlsentence)
            if _datetime[0][:-3] not in logging_data_dict.keys():
                logging_data_dict[_datetime[0][:-3]] = {}
            if _sqlsentence[0] not in logging_data_dict[_datetime[0][:-3]].keys():
                logging_data_dict[_datetime[0][:-3]][_sqlsentence[0]] = 1
            else:
                logging_data_dict[_datetime[0][:-3]][_sqlsentence[0]] += 1

    #print(logging_data_dict)
    for item in logging_data_dict:
        max_executed = 0
        max_executed_sql = ''
        for item2 in logging_data_dict[item]:
            if logging_data_dict[item][item2]>=max_executed:
                max_executed = logging_data_dict[item][item2]
                max_executed_sql = item2
        logging_data_dict[item]['max_executed'] = max_executed_sql

    print(logging_data_dict)
