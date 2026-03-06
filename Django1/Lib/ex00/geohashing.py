import sys, antigravity


def run_geohash(lat_str, lon_str, date_dow_str):
    try:
        # 1. Validation & Conversion
        lat = float(lat_str)
        lon = float(lon_str)
        date_dow = date_dow_str.encode('utf-8')

        # 2. Execution
        antigravity.geohash(lat, lon, date_dow)

    except ValueError:
        print("Error: Latitude and Longitude must be numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    if len(sys.argv) != 4:
        print("Error: Wrong number of arguments.")
        print("Usage: python3 geohashing.py <lat> <lon> <date-dow>")
    else:
        run_geohash(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()