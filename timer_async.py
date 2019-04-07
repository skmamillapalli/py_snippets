# Date - 06/04/2019
r"""Ref - https://www.youtube.com/watch?v=iG6fr81xHKA
          https://docs.python.org/3/library/asyncio-task.html#coroutines
          https://gist.github.com/miguelgrinberg/f15bc03471f610cfebeba62438435508
          https://blog.miguelgrinberg.com"""
import time
import asyncio
loop = asyncio.get_event_loop()

@asyncio.coroutine
def async_timer():
        print("Before async sleep")
        yield from asyncio.sleep(3)
        print("After async sleep")


def sync_timer():
    for i in range(10):
        print("Before sleep")
        time.sleep(3)
        print("After quick nap.")
    
if __name__=='__main__':
    t1 = time.time()
    sync_timer()
    t2 = time.time()
    print('Total running time sync way, {} seconds.'.format(t2-t1))
    t1 = time.time()
    loop.run_until_complete(asyncio.gather(async_timer(), async_timer(), async_timer(), async_timer(), async_timer(), async_timer() ,async_timer()))
    t2 = time.time()
    print('Total running time async way, {} seconds'.format(t2-t1))



