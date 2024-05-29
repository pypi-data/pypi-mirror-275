import random
import time
from morpheuscypher import Cypher

url = "https://morpheus.tryfan.duckdns.org"
token = "47a53897-bfd7-4be0-bb24-c07988fc2ab4"

c = Cypher(url=url, token=token)
print(c.get("secret/test-morpheus-user"))
