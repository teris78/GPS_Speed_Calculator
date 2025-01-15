import math
import csv
import statistics

# Define input and output CSV file paths
input_csv = "input_file.csv"
output_csv = "output_speeds.csv"

def haversine(lon1, lat1, lon2, lat2):
    # Calculate the great-circle distance between two points on the Earth's surface
    R = 6371  # Radius of Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c * 1000  # Convert kilometers to meters

def calculate_speeds(input_file, output_file):
    # Calculate speeds from GPS data and write results to a CSV file
    data = []  # List to store the time, longitude, and latitude data
    speeds = []  # List to store calculated speeds

    # Open the input CSV file for reading
    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Read data and store in the list
        for row in reader:
            time, lon, lat = map(float, row)  # Convert data to float and store
            data.append([time, lon, lat])

        # Calculate speeds between successive data points
        for i in range(1, len(data)):
            t1, lon1, lat1 = data[i - 1]
            t2, lon2, lat2 = data[i]
            distance = haversine(lon1, lat1, lon2, lat2)
            timediff = t2 - t1

            # Only calculate speed if the time difference is positive
            if timediff > 0:
                speed = (distance / timediff) * 3.6  # Convert m/s to km/h
                speeds.append(speed)

    # Write calculated speeds to the output CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Segment', 'Speed (km/h)'])
        for i, speed in enumerate(speeds):
            writer.writerow([i + 1, speed])

    # Calculate and print average and median speeds
    average_speed = sum(speeds) / len(speeds) if speeds else 0
    median_speed = statistics.median(speeds) if speeds else 0

    print(f'Average speed: {average_speed:.2f} km/h')
    print(f'Median speed: {median_speed:.2f} km/h')

# Call the function to calculate speeds
calculate_speeds(input_csv, output_csv)
