from app.process_engine.action.v1 import plugin_validator as r
import pytest
import random
from pydantic import BaseModel


class ValidationType(BaseModel):
    validation_type: str


class Data(BaseModel):
    data: str


class Configuration(BaseModel):
    validator: ValidationType


@pytest.mark.email
def test_email():
    import random
    import string
    number = 0

    def random_char(char_num):
        return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

    while not number == 1:
        a = random_char(12) + "@" + random_char(5) + "." + random_char(3)
        number += 1
        type = ValidationType(validation_type="email_regex")
        data = Data(data="patromi123@gmail.com")
        klass = r.Validate(type, data)
        assert klass.check()
    assert True


def test_url():
    assert r.url("https://www.polska.com/api/e/w/2")


@pytest.mark.date
def test_date():
    a = 0
    while not a == 100000:
        c = random.randint(1, 12)
        if c == 2:
            b = random.randint(1, 28)
        else:
            b = random.randint(1, 30)
        d = random.randint(1600, 2021)
        a += 1
        assert r.date(f"{b}-{c}-{d}")


def test_int():
    a = 0
    while not a == 10000:
        c = random.randint(1, 100000)
        a += 1
        assert r.int(str(c))


def test_float():
    a = 0
    while not a == 10000:
        c = random.uniform(1.0, 100000.0)
        a += 1
        assert r.int(str(c))


def test_timer():
    a = 0
    while not a == 10000:
        c = random.randint(1, 23)
        d = random.randint(1, 59)
        if d < 10:
            d = "0" + str(d)

        a += 1
        assert r.timer(f"{c}:{d}")


def test_ean():
    a = "5901234123457"
    assert r.ean(a)


def test_numberphone():
    a = 0
    while not a == 1000:
        d = random.randint(1, 99)
        d = '+' + str(d)
        c = random.randint(1000000, 999999999)
        a += 1
        assert r.numberphone(f"{d}{c}")


@pytest.mark.ip
def test_ip():
    a = 0
    while not a == 1000:
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        d = random.randint(1, 255)
        e = random.randint(1, 255)
        a += 1
        assert r.ip(f"{b}.{c}.{d}.{e}")
