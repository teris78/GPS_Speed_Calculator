import math
import csv
import statistics
input_csv = "input_file.csv"
output_csv ="output_speeds.csv"

def haversine(lon1, lat1, lon2, lat2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c * 1000

def calculate_speeds(input_file, output_file):
    data = []
    speeds = []
    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            time, lon, lat = map(float, row)
            data.append([time, lon, lat])

            for i in range(1, len(data)):
      t1, lon1, lat1 = data[i - 1]
      t2, lon2, lat2 = data[i]
        distance = haversine(lon1, lat1, lon2, lat2)
         timediff = t2 - t1
                if timediff > 0:
                    speed = (distance / timediff) * 3.6
                    speeds.append(speed)

                    with open(output_file, mode='w', newline='') as file:
                 writer = csv.writer(file)
                 writer.writerow(['Segment', 'speed km/h'])
              for i, speed in enumerate(speeds):
                            writer.writerow([i + 1, speed])

                 average_speed: float | int = sum(speeds) / len(speeds) if speeds else 0
                 median_speed = statistics.median(speeds) if speeds else 0
                print(f'Average speed: {average_speed} km/h')
                 print(f'Median speed: {median_speed} km/h')
calculate_speeds(input_csv, output_csv)