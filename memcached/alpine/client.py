from pymemcache.client.base import Client
import time, random

client = Client(('localhost', 11211))

string = 'zxcvbnmasdfghjklqwertyuiop1234567890'
counter = 0
max_items = 100000

def randomizer():
    data = ''.join(random.choice(string) for x in range(512))
    return data

start_time = int(time.time())

while counter != max_items:
    counter += 1
    value = randomizer()
    client.set(str(counter), value, expire=360)

end_time = int(time.time())

print("Took {} seconds to write {} using 1 node".format(end_time - start_time, max_items))

# return a random key:
print(client.get(str(random.randint(1,10000))))
