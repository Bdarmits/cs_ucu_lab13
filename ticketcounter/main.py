# Module to test simulation
from ticketcounter import TicketCounterSimulation

print("Welcome to the simulation of ticket counter")

minutes = int(input("Number of minutes to simulate: "))
agents = int(input("Number of ticket agents: "))
service_time = int(input("Average service time per passenger: "))
between_time = float(input("Average time between passenger arrival: "))

# def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
simulation = TicketCounterSimulation(agents, minutes, between_time, service_time)

simulation.run()
simulation.printResults()
