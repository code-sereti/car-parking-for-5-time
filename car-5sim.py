import simpy

def car(env):
    while True:
        print(f"Start parking at {env.now}")
        parking_duration = 5
        yield env.timeout(parking_duration)

        print(f"Start driving at {env.now}")
        driving_duration = 2
        yield env.timeout(driving_duration)

# Create a SimPy environment
env = simpy.Environment()

# Start the car process in the environment
car_process = env.process(car(env))

# Run the simulation for a total of 20 time units
env.run(until=20)
