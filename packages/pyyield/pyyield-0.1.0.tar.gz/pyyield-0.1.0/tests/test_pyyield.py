from pyyield import pyyield
from time import time, sleep
from pytest import fail
import logging


def emptyFunc():
    # Nothing to see here
    return


def test_pyyield_call():
    try:
        pyyield()
    except Exception as e:
        fail(f"Failed to call 'pyyield()': {str(e)}")


# Purely for performance comparison. Seems to be very varying results, depending on setup.
def test_pyyield_speed():
    try:
        sleepTime = 0
        pyyieldTime = 0
        emptyTime = 0
        for i in range(3):
            t0 = time()
            for i in range(50000):
                pyyield()
            t1 = time()
            for i in range(50000):
                sleep(0)
            t2 = time()
            for i in range(50000):
                emptyFunc()
            t3 = time()
            pyyieldTime = t1 - t0
            sleepTime = t2 - t1
            emptyTime = t3 - t2
            if pyyieldTime < sleepTime and pyyieldTime > emptyTime:
                # All good!
                return
        assert pyyieldTime > emptyTime, "pyyield is faster than emptyFunc()!"
        assert pyyieldTime < sleepTime, "pyyield is not faster than sleep()!"
    except Exception as e:
        # fail(f"Failed to at speed test: {str(e)}")
        logging.info(
            f"Failed to at speed test, pyyieldTime: {pyyieldTime}, sleepTime: {sleepTime}, emptyTime: {emptyTime}, error: {str(e)}"
        )
