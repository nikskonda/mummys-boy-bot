# -*- coding: utf-8 -*-
import telebot
import pytz
from _datetime import datetime


class Message:
    def __init__(self, text="", time=datetime.now()):
        self.__text=text
        self.__time=time

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text=text

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time=time


class DailyPlanPoint:
    def __init__(self, message="", hour = 8):
        self.status = False
        self.message = message
        self.hour = hour


class DailyPlan:
        list = [DailyPlanPoint("Good morning!", 2),
                DailyPlanPoint("I am OK!", 4),
                DailyPlanPoint("Good night!", 3)]


def start():
    print("Start " + str(datetime.now()))
    last_message = Message()
    chat_id = 399575400
    tz = pytz.timezone("Europe/Minsk")

    plan = DailyPlan()
    while True:
        #
        # if (last_message.time.day < datetime.now().day):
        #     if (datetime.now().astimezone(tz).hour > 10):
        #         last_message = Message(last_message.text)
        #         bot.send_message(chat_id, last_message.text)

        # every minute
        # if last_message.time.minute < datetime.now().minute:
        #     last_message = Message(last_message.text, datetime.now())
        #     bot.send_message(chat_id, last_message.text)

        if last_message.time.day != datetime.now().day:
            plan = DailyPlan()
            print("New day "+str(datetime.now()))
        for p in plan.list:
            if (not p.status) and (p.hour <= datetime.now().astimezone(tz).hour):
                p.status = True
                bot.send_message(chat_id, p.message)
                print('"' + p.message + '" was send in ' + str(datetime.now()))
                last_message = Message(p.message)


bot = telebot.TeleBot("687132824:AAHKfMpTdH-0RZkxSXEgmX5_8j2VdzXY60s")
start()
bot.polling(none_stop=True, interval=0)


