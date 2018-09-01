from pymemcache.client.hash import HashClient
import time, random

client = HashClient([
    ('127.0.0.1', 11211),
    ('127.0.0.1', 11212),
    ('127.0.0.1', 11213)
])

string = 'zxcvbnmasdfghjklqwertyuiop1234567890'
counter = 0
max_items = 100000
nodes = 3

def randomizer():
    data = ''.join(random.choice(string) for x in range(512))
    return data

start_time = int(time.time())

while counter != max_items:
    counter += 1
    value = randomizer()
    client.set(str(counter), value, expire=360)

end_time = int(time.time())

print("Took {} seconds to write {} using {} nodes".format(end_time - start_time, max_items, nodes))
