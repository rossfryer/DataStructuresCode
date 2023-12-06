import tkinter as tk
import queue
import random

SIMULATION_TIME = 60
ARRIVAL_PROB = 0.4
QUEUE_THRESHOLD = 5
MAX_CHECKOUTS = 5


class Shopper:

    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.service_time = random.randint(1,5)


class Checkout:

    def __init__(self, id):
        self.id = id
        self.current_shopper = None
        self.service_remaining = 0

    def is_busy(self):
        return self.current_shopper is not None

    def start_service(self, shopper, minute):

        self.current_shopper = shopper
        self.service_remaining = shopper.service_time

        wait = minute - shopper.arrival_time
        log(f"Minute {minute}: Checkout {self.id} serving "
            f"(wait {wait}, service {self.service_remaining})")

        return wait

    def process(self, minute):

        if self.current_shopper is None:
            return False

        self.service_remaining -= 1

        if self.service_remaining == 0:
            log(f"Minute {minute}: Checkout {self.id} finished")
            self.current_shopper = None
            return True

        return False


# ----------------------
# GUI Functions
# ----------------------

def log(message):
    output.insert(tk.END, message + "\n")
    output.see(tk.END)


def start_simulation():

    output.delete(1.0, tk.END)

    shopping_queue = queue.Queue()
    checkouts = [Checkout(1)]

    total_wait = 0
    served = 0
    max_queue = 0

    for minute in range(SIMULATION_TIME):

        if random.random() < ARRIVAL_PROB:
            shopper = Shopper(minute)
            shopping_queue.put(shopper)
            log(f"Minute {minute}: Shopper arrived")

        if shopping_queue.qsize() > max_queue:
            max_queue = shopping_queue.qsize()

        if (shopping_queue.qsize() > QUEUE_THRESHOLD and
            len(checkouts) < MAX_CHECKOUTS):

            new_id = len(checkouts) + 1
            checkouts.append(Checkout(new_id))
            log(f"Minute {minute}: Checkout {new_id} opened")

        for checkout in checkouts:

            if not checkout.is_busy() and not shopping_queue.empty():

                shopper = shopping_queue.get()
                wait = checkout.start_service(shopper, minute)
                total_wait += wait

        for checkout in checkouts:

            if checkout.process(minute):
                served += 1

        root.update()
        root.after(100)

    if served > 0:
        avg_wait = total_wait / served
    else:
        avg_wait = 0

    log("\nSimulation Results")
    log("------------------")
    log(f"Customers served: {served}")
    log(f"Average wait time: {round(avg_wait,2)} minutes")
    log(f"Maximum queue length: {max_queue}")
    log(f"Checkouts opened: {len(checkouts)}")


# ----------------------
# GUI Layout
# ----------------------

root = tk.Tk()
root.title("Supermarket Queue Simulation")

title = tk.Label(root, text="Supermarket Queue Simulation", font=("Arial",16))
title.pack(pady=10)

start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
start_button.pack(pady=5)

output = tk.Text(root, height=20, width=70)
output.pack(padx=10, pady=10)

root.mainloop()