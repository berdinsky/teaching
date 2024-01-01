# M/M/1 model 
 
import random 
import simpy 

random_seed = 101 
running_time = 60*6
interarrival_time = 5
service_time = 5.5

class Customer(): 
    def __init__(self,env,counter,identity,time): 
        self.env=env 
        self.counter = counter 
        self.arrival_time=time
        self.customer_id = identity 
        print('Customer%s arrived at %0.2f' %(self.customer_id,self.arrival_time)) 
        env.process(self.service())
    
    def service(self): 
        counter_request = self.counter.request()
        yield counter_request
        print('Customer%s waited %0.2f minutes; started service at %0.2f' 
              %(self.customer_id, self.env.now-self.arrival_time,self.env.now))
        t = random.expovariate(1/ service_time)
        yield self.env.timeout(t) 
        print('Customer%s leaves the counter at %0.2f' %(self.customer_id,self.env.now))
        self.counter.release(counter_request)
        
def customer_generator(env,counter):  
    n=0 # the first customer has number zero
    Customer(env,counter,n,env.now)
    while True:       
        n = n + 1 
        t = random.expovariate (1 / interarrival_time) # delay between arrivals 
        yield env.timeout(t) # here we generate arrival of a new customer
        Customer(env,counter,n,env.now) 

random.seed(random_seed)       
           
env=simpy.Environment()

counter = simpy.Resource(env, capacity=1)

env.process(customer_generator(env,counter))

env.run(running_time)

