from random import randint
from random import randrange
import datetime
import uuid
from datetime import timedelta


def make_me(gen_type, length, content):
    if gen_type == 'straight':
        return make_array(length, content)
    elif gen_type == 'reversed':
        return make_reversed(length, content)
    elif gen_type == 'sorted':
        return make_sorted(length, content)
    elif gen_type == 'partly_sorted':
        return make_partly_sorted(length, content)
    elif gen_type == 'same_elements':
        return make_same_elements(length, content)
    elif gen_type == 'partly_same':
        return make_partly_same(length, content)


def make_array(length, content):
    newbie = []
    for i in range(length):
        if content == 'byte':
            newbie.append(randint(0, 9))
        elif content == 'int':
            newbie.append(randint(0, 999))
        elif content == 'string':
            newbie.append(uuid.uuid4().hex)
        elif content == 'date':
            start = datetime.date(year=1970, month=1, day=1)
            end = datetime.date(year=2018, month=5, day=3)
            delta = end - start
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = randrange(int_delta)
            newbie.append(start + timedelta(seconds=random_second))
    return newbie


def make_reversed(length, content):
    newbie = []
    if content == 'byte':
        newbie = make_array(length, content)
        newbie.sort(reverse=True)
    elif content == 'int':
        for i in range(length):
            newbie.append(length - i)
    elif content == 'string':
        for i in range(length):
            newbie.append(uuid.uuid4().hex)
        newbie.sort(reverse=True)
    elif content == 'date':
        start_date = datetime.date.today()
        for i in range(length):
            newbie.append(start_date - timedelta(days=i))
    return newbie


def make_sorted(length, content):
    newbie = []
    if content == 'byte':
        for value in range(0, 10):
            for i in range(int(length / 10)):
                newbie.append(value)
    elif content == 'int':
        for i in range(length):
            newbie.append(i)
    elif content == 'string':
        for i in range(length):
            newbie.append(uuid.uuid4().hex)
        newbie.sort()
    elif content == 'date':
        start_date = datetime.date.today()
        for i in range(length):
            newbie.append(start_date + timedelta(days=i))
    return newbie


def make_partly_sorted(length, content):
    newbie = []
    for _ in range(10):
        newbie = make_array(length, content)
        start_index = randint(0, length - 4)
        newbie[start_index:start_index + 4].sort()
    return newbie


def make_same_elements(length, content):
    newbie = []
    if content == 'byte':
        for i in range(length):
            newbie.append(5)
    elif content == 'int':
        for i in range(length):
            newbie.append(1337)
    elif content == 'string':
        for i in range(length):
            newbie.append('kek')
    elif content == 'date':
        date = datetime.date.today()
        for i in range(length):
            newbie.append(date)
    return newbie


def make_partly_same(length, content):
    newbie = make_array(length, content)
    if content == 'byte':
        for i in range(length // 2):
            random_index = randint(0, length - 1)
            newbie[random_index] = 5
    elif content == 'int':
        for i in range(length // 2):
            random_index = randint(0, length - 1)
            newbie[random_index] = 1337
    elif content == 'string':
        for i in range(length // 2):
            random_index = randint(0, length - 1)
            newbie[random_index] = 'kek'
    elif content == 'date':
        date = datetime.date.today()
        for i in range(length // 2):
            random_index = randint(0, length - 1)
            newbie[random_index] = date
    return newbie
