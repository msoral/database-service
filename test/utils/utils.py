import random
import string


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_ochlv_data() -> dict:
    return {
        "open": random.uniform(0.1, 1)*10000,
        "close": random.uniform(0.1, 1)*10000,
        "high": random.uniform(0.1, 1)*10000,
        "low": random.uniform(0.1, 1)*10000,
        "volume": random.uniform(0.1, 1)*100000
    }
