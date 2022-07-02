import sqlite3
import requests
import json


mainlink = "http://127.0.0.1:8000"


def get_info_about_room(tg_id, room_id):
    try:
        response = requests.get(f"{mainlink}/api/get_rooms/").json()
        room = [i for i in list(response) if str(i["id"])==str(room_id)][0]
        owner_room_id = room["owner_id"]
        res = [room["id"], room["name_room"], room["is_music"], owner_room_id]
        print(room)
        return res
    except:
        res = ['', '', '', '']
        return res


def leave_room(tg_id):
    try:
        con = sqlite3.connect("botDB.db")
        cur = con.cursor()
        cur.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cur.execute(
            f"""UPDATE users SET room_id=Null, password_room=Null
                     where tg_id='{tg_id}' """)
        con.commit()
        con.close()
        return True
    except:
        return False


def add_room_id(tg_id, room_id):
    try:
        con = sqlite3.connect("botDB.db")
        cur = con.cursor()
        cur.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cur.execute(
            f"""UPDATE users SET room_id='{room_id}'
                     where tg_id='{tg_id}' """)
        con.commit()
        con.close()
        return True
    except:
        return False


def add_password_room(tg_id, password):
    try:
        con = sqlite3.connect("botDB.db")
        cur = con.cursor()
        cur.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cur.execute(
            f"""UPDATE users SET password_room='{password}'
                     where tg_id='{tg_id}' """)
        con.commit()
        con.close()
        return True
    except:
        return False


def add_user_id(tg_id, user_id):
    try:
        con = sqlite3.connect("botDB.db")
        cur = con.cursor()
        cur.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cur.execute(
            f"""UPDATE users SET user_id='{user_id}'
                     where tg_id='{tg_id}' """)
        con.commit()
        con.close()
        return True
    except:
        return False


def add_password(tg_id, password):
    try:
        con = sqlite3.connect("botDB.db")
        cur = con.cursor()
        cur.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cur.execute(
            f"""UPDATE users SET password_room='{password}'
                     where tg_id='{tg_id}' """)
        con.commit()
        con.close()
        return True
    except:
        return False


def create_user_tg(tg_id):
    try:
        con = sqlite3.connect("botDB.db")
        cur = con.cursor()
        cur.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cur.execute(
            f"""INSERT INTO users  (tg_id) VALUES('{tg_id}')""")
        con.commit()
        con.close()
        return True
    except:
        return False


def is_room_tied(tg_id):
    try:
        con = sqlite3.connect("botDB.db")
        cursor = con.cursor()
        cursor.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cursor.execute(f"""SELECT room_id FROM users where tg_id='{tg_id}'""")
        room = cursor.fetchall()[0][0]
        con.commit()
        con.close()
        return True if room else False
    except:
        return False


def get_all_info(tg_id):
    try:
        con = sqlite3.connect("botDB.db")
        cursor = con.cursor()
        cursor.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cursor.execute(f"""SELECT * FROM users where tg_id='{tg_id}'""")
        room = cursor.fetchall()[0]
        con.commit()
        con.close()
        return room
    except:
        return ['', '', '','']


def is_password_tied(tg_id):
    try:
        con = sqlite3.connect("botDB.db")
        cursor = con.cursor()
        cursor.execute('''
                  CREATE TABLE IF NOT EXISTS users (tg_id         STRING UNIQUE, user_id       STRING, room_id       STRING,password_room STRING)''')
        cursor.execute(f"""SELECT password_room FROM users where tg_id='{tg_id}'""")
        password = cursor.fetchall()[0][0]
        con.commit()
        con.close()
        return True if password else False
    except:
        return False

# api


def get_user_name(tg_id):
    try:
        response = requests.get(f"{mainlink}/api/get_users/").json()
        for i in response:
            print(i, str(i['tg_name']), str(tg_id))
            if str(i['tg_name']) == str(tg_id):
                return i['username']
        return ''
    except:
        return ''


def get_owner(id):
    try:
        response = requests.get(f"{mainlink}/api/get_users/").json()
        for i in response:
            if str(i['id']) == str(id):
                return i['username']
        return ''
    except:
        return ''


def tg_tied(tg_id):
    try:
        response = requests.get(f"{mainlink}/api/get_users/").json()
        for i in response:
            if str(i['tg_name']) == str(tg_id):
                add_user_id(tg_id, i['id'])
                return True
        return False
    except:
        return False


def password_is_valid(tg_id, enter_password):
    try:
        room_id = get_all_info(tg_id)[2]
        #  print(room_id)
        response = requests.get(f"{mainlink}/api/get_rooms/").json()
        password_room = [i["password_room"] for i in list(response) if i["id"] == room_id][0]
        #  print(password_room)
        if password_room == enter_password:
            add_password(tg_id, enter_password)
            return True
        return False
    except:
        return False


def room_exist(tg_id, room_id):
    try:
        #  print(room_id)
        response = requests.get(f"{mainlink}/api/get_rooms/").json()
        all_rooms_id = [str(i["id"]) for i in list(response)]
        #  print(all_rooms_id)

        if room_id in all_rooms_id:
            add_room_id(tg_id, room_id)
            return True
        return False
    except:
        return False


def add_link(tg_id, link):
    try:
        info = get_all_info(tg_id)
        #  print(info)
        # (link=str, room=id_room, tg_name=str, password=password)
        json_link = {'link': str(link), 'room': int(info[2]),
                     'tg_name': str(tg_id), 'password': str(info[3])}

        response = requests.post(f"{mainlink}/api/new_link/", data=json_link)

        print(json_link, type(json_link))
        print({'link': str(link), 'room': int(info[2]),
                                       'tg_name': str(tg_id), 'password': str(info[3])})
        return True
    except Exception as error:
        print(error)
        return False
