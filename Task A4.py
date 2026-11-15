import time
import logging

logging.basicConfig(level=logging.INFO)

def calculate():

    start = time.perf_counter()

    values = [10, 20, 30, 40, 50]

    total = 0

    for value in values:
        assert value >= 0
        total += value

    average = total / len(values)

    logging.info("Calculation completed")

    end = time.perf_counter()

    print("Total:", total)
    print("Average:", average)
    print("Execution Time:", end - start)

calculate()
