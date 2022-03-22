
from typing import final


def letMeIntroduceMyself():
    name= input("Enter your name:")
    hobby=input("What is your hobby?")
    university=input("Enter your university name:")
    birthday=input("Enter your birthday (Like :981128) : ")
    year=birthday[:2]
    month=birthday[4:2]
    day=birthday[4:]
    final="My name is {name} and my hobby is {hobby}. I am going to {university} and my birthday is on {month} month {day} day".format(name=name,hobby=hobby,university=university,month=birthday[2:4],day=birthday[4:])
    return final
print(letMeIntroduceMyself())
    