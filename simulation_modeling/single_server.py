# this program makes one simulation run of a single-server queueing system 

import gc
import random

running_time = 60*6
interarrival_time = 5
service_time = 5

class Customer:
    def __init__(self, arrival_time, customer_id):
        self.arrival_time = arrival_time
        self.customer_id=customer_id
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_customer(self,new_customer):
        if self.tail==None: 
            self.head=new_customer 
            self.tail=new_customer  
        else:    
            self.tail.next=new_customer
            self.tail=new_customer

    def remove_customer(self):
        self.head = self.head.next    
        if self.head==None: self.tail=None
        gc.collect()

def pop_nearest_event(future_events):
    j=0 
    for i in range(0,len(future_events)): 
        if future_events[i][0]<future_events[j][0]: j=i     
    nearest_event=future_events[j]
    future_events.pop(j)
    return nearest_event[0], nearest_event[1]

def add_future_event(time,type,future_events):
    future_events.append((time,type)) 

def customer_arrival(queue,time,future_events,counter):
    # generate the next arrival event
    time_next_arrival=time+random.expovariate(1/interarrival_time)
    add_future_event(time_next_arrival,'arrival',future_events)
    # if the queue is empty we also have to generate the departure event 
    if not queue.head: 
        time_departure=time+random.expovariate(1/service_time) 
        add_future_event(time_departure,'departure',future_events)
    
    new_customer=Customer(time,counter)          
    queue.add_customer(new_customer)
    # print a message 
    print('Customer N',counter,' arrived at ',round(time,2))

def customer_departure(queue,time,future_events): 
    # print a message 
    print('Customer N',queue.head.customer_id,' waited ',
           round(time-queue.head.arrival_time,2),'and departed at ',
           round(time,2))
    queue.remove_customer() 
    if queue.head: # generate the next departure event
        time_next_departure=time+random.expovariate(1/service_time) 
        add_future_event(time_next_departure,'departure',future_events)    
   
def simulation_run(running_time): 
    time=0 
    type='arrival' 
    counter=0 # customer counter 
    # arrival of the first customer at time 0 is not added to 
    # the list of future events 
    future_events=[] 
    queue=Queue()    
    while time<=running_time:
        if type=='arrival':
            customer_arrival(queue,time,future_events,counter)
            counter = counter + 1
        elif type=='departure':
            customer_departure(queue,time,future_events)

        time, type = pop_nearest_event(future_events)   

def main():
    simulation_run(running_time)

main()             