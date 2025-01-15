# GPS Speed Calculation Project

This project calculates speed from GPS coordinates using the Haversine formula. The Python script processes a CSV file containing latitude, longitude, and timestamps, calculating the speed for each segment and saving the results to a CSV file.

## Features
- Calculates speed using the Haversine formula.
- Input and output are handled via CSV files.
- Outputs speed in kilometers per hour (km/h).

## Requirements
- Python 3.x
- Pandas

## File Structure
- `code.py`: Main Python script for speed calculation.
- `input_file.csv`: Input CSV file containing GPS data.
- `output_speeds.csv`: Output CSV containing calculated speeds.

## Usage

1. Place your input file in the project directory and name it `input_file.csv`.
2. Run the script:
   ```bash
   python code.py
   ```
3. The results will be saved in `output_speeds.csv`.

## Example Output
The output CSV contains the segment number and calculated speed:

```csv
Segment,Speed (km/h)
1,19.71
2,19.71
3,24.16
```

## How It Works
- The script uses the Haversine formula to calculate the distance between consecutive GPS points.
- Speed is calculated using the distance traveled divided by the time difference.


