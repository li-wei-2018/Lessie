""" Android Radio log Interpreter
Author: Lucas de Lima Barros
Team: Protocol TG

The idea of this project is to provide an interface capable of parsing log files in order to show the better matches for
analyze according with the problem. Some steps for this implementation:
1. Read logfile and split in lines
2. Identify radio buffer
3. Match Problem with Key Words ( For example, Emergency Numbers: [EmergencyTracker])
4. Show only the lines according with the problem
Once this is done, we are going to create an end point that can be used by PLM server, to download logs, parse
description and provide a comment automatically.
"""


def read_log(log_file_from_user):
    try:
        if 'logcat' in log_file_from_user:
            log = open(log_file_from_user)
            return log
        else:
            print("We are not dealing with dumpstate file yet!")

    except FileNotFoundError:
        return "Please verify file format! Accepted Dumpstate and logcat"


def get_problems():
    # It will get the problems from user
    pass


def get_key_words(problems):
    # For each problem, it will return a list os key words from DB
    pass


def parse_log_with_key_words(key_words):
    # It will parse the log getting all lines that have the key words
    pass


if __name__ == "__main__":
    # Criar banco mongodb - ok
    # Conectar ao django
    # Escrever models

    example_os = {
        "id": 1,
        "OS": "OO"
    }
    example_themes = {
        "id": 1,
        "theme": "Emergency Numbers"
    }

    example_matches = {
        "theme": 1,
        "os": 1,
        "key_words": ["SIM-MGR", "EmergencyTracker:"]
    }

    print('Starting Project:')
    log_file = 'logcat.log'

    log = read_log(log_file)
    print(log.readlines())