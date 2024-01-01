# M/M/1 model 

import random 
import simpy 
import matplotlib
import matplotlib.pyplot as plt
  
random_seed = 11 
running_time = 60*6
interarrival_time = 5
service_time = 5.5

class Customer(object): 
    def __init__(self,env,counter,identity,time):   
        self.env=env 
        self.counter = counter 
        self.arrival_time=time
        self.customer_id = identity 
        env.process(self.service())
   
    def service(self): 
        counter_request = self.counter.request()
        yield counter_request
        waiting_time = self.env.now - self.arrival_time # waiting time
        update_total_time(waiting_time) # update the total waiting time  
        update_num_customers(self.customer_id) # update the number of customers served  
        t = random.expovariate(1/ service_time)
        yield self.env.timeout(t) 
        self.counter.release(counter_request)
        
def customer_generator(env,counter):  
    n=0 # the first customer has number zero
    Customer(env,counter,n,env.now)
    while True:       
        n = n + 1 
        t = random.expovariate (1 / interarrival_time) # delay between arrivals 
        yield env.timeout(t)
        Customer(env,counter,n,env.now) 

def update_total_time(waiting_time):
    global total_time
    total_time += waiting_time

def update_num_customers(customer_id): 
    global num_customers 
    num_customers = customer_id+1

# main program 

random.seed(random_seed)

R=100
X = range(0,R)
Y = []

for i in X: 

    total_time = 0 # total waiting time for customers who entered service
    num_customers = 0 # the number of customers who entered service

    env=simpy.Environment()

    counter = simpy.Resource(env, capacity=1)

    env.process(customer_generator(env,counter))

    env.run(running_time)

    Y.append(total_time/num_customers)

plt.plot(X,Y,"-o")
plt.ylabel("Average waiting time")
plt.xlabel("Simulation runs")
plt.show()