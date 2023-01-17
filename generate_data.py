#!/usr/bin/env python
from faker import Faker
import time

def generate_data():
    fake = Faker()
    return {
        "name": fake.name(),
        "address": fake.address(),

}


if __name__ == '__main__':
    while 1 == 1:
        time.sleep(5)
        print(generate_data())
        generate_data()
