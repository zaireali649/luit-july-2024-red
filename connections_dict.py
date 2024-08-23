# List of connections, each represented as a dictionary
connections = [
    {'departure': 'Amsterdam', 'destination': 'Dublin', 'flight_time': 100},
    {'departure': 'Amsterdam', 'destination': 'Rome', 'flight_time': 140},
    {'departure': 'Rome', 'destination': 'Warsaw', 'flight_time': 130},
    {'departure': 'Minsk', 'destination': 'Prague', 'flight_time': 95},
    {'departure': 'Stockholm', 'destination': 'Rome', 'flight_time': 190},
    {'departure': 'Copenhagen', 'destination': 'Paris', 'flight_time': 120},
    {'departure': 'Madrid', 'destination': 'Rome', 'flight_time': 135},
    {'departure': 'Lisbon', 'destination': 'Rome', 'flight_time': 170},
    {'departure': 'Dublin', 'destination': 'Rome', 'flight_time': 170},
]

# Initialize variables for storing total flight time to Rome, number of flights to Rome, and lists for specific details
flight_time = 0
num_flights = 0
rome_flights = []  # List to store flight times to Rome
departure_cities_to_rome = []  # List to store departure cities with flights to Rome
all_destinations = set()  # Set to store all unique destination cities

# Loop through each connection in the list
for connection in connections:
    destination = connection['destination']  # Get the destination city
    flight_duration = connection['flight_time']  # Get the flight time in minutes
    all_destinations.add(destination)  # Add the destination city to the set of all destinations
    
    # Check if the destination city is Rome (case-insensitive check)
    if destination.lower() == 'rome':
        num_flights += 1  # Increment the number of flights to Rome
        flight_time += flight_duration  # Add the flight time to the total flight time
        rome_flights.append(flight_duration)  # Add flight time to the Rome flights list
        departure_cities_to_rome.append(connection['departure'])  # Add departure city to the list

# Calculate the average flight time to Rome
average_flight_time_to_rome = flight_time / num_flights if num_flights > 0 else 0

# Find the longest and shortest flights to Rome
longest_flight_to_rome = max(rome_flights) if rome_flights else None
shortest_flight_to_rome = min(rome_flights) if rome_flights else None

# Sort the flights to Rome by duration
rome_flights_sorted = sorted(rome_flights)

# Calculate total flight time for all connections
total_flight_time = sum([connection['flight_time'] for connection in connections])

# Print out all the gathered information
print(f'{num_flights} connections lead to Rome with an average flight time of {average_flight_time_to_rome:.2f} minutes.')
print(f'The longest flight to Rome is {longest_flight_to_rome} minutes.')
print(f'The shortest flight to Rome is {shortest_flight_to_rome} minutes.')
print(f'Flights to Rome sorted by time: {rome_flights_sorted}')
print(f'Departure cities with direct flights to Rome: {departure_cities_to_rome}')
print(f'Total flight time for all connections: {total_flight_time} minutes.')
print(f'All unique destination cities: {all_destinations}')
