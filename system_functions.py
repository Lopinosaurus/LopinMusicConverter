#region Libs
import time

from dotenv import load_dotenv
import json
import discord
#endregion

def is_registered(member):
    """
    Checks if the member is already registered in the JSON database
    :param member: The watched member
    :return: True if registered, False otherwise.
    """
    ply_file = open('players.json', 'r+', encoding="utf-8")
    ply_json = json.load(ply_file)
    players_list = ply_json['players']
    for ply_data in players_list:
        if member.id in ply_data:
            ply_file.close()
            return True

    ply_file.close()
    return False


def watch_games(member):
    """
    Indexes :
    [0]: Member ID \n
    [1]: time.time() when started to play \n
    [2]: Is the member currently on LoL \n
    [3]: Time waste on LoL since bot first use (in hours)
    :param member: The watched member
    """
    ply_file = open('players.json', 'r+', encoding="utf-8")
    ply_json = json.load(ply_file)
    players_list = ply_json['players']
    players_list.append([member.id, 0, str(is_playing_lol(member)), 0])
    ply_file.seek(0)
    json.dump(ply_json, ply_file, indent=4)
    ply_file.truncate()
    ply_file.close()


def is_playing_lol(member):
    if member.activity == None:
        return False
    if member.activity.name == "League of Legend":
        return True
    return False


def start_time(member):
    """
    Start game timer in the JSON database
    :param member: The watched member
    """
    ply_file = open('players.json', 'r+', encoding="utf-8")
    ply_json = json.load(ply_file)
    players_list = ply_json['players']
    for ply_data in players_list:
        if member.id in ply_data:
            ply_data[1] = time.time()
            ply_file.seek(0)
            json.dump(ply_json, ply_file, indent=4)
            ply_file.truncate()
            ply_file.close()

def add_global_time(member):
    """
    Add global time when a player finished a League of Legend game (Index 3 of JSON player database)
    :param member: The watched member
    """
    ply_file = open('players.json', 'r+', encoding="utf-8")
    ply_json = json.load(ply_file)
    players_list = ply_json['players']
    for ply_data in players_list:
        if member.id in ply_data:
            # Global time in hours, that's why I divide by 3600
            ply_data[3] += (time.time() - ply_data[1]) // 3600
            ply_file.seek(0)
            json.dump(ply_json, ply_file, indent=4)
            ply_file.truncate()
            ply_file.close()