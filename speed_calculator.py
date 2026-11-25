
def calculate_speed(distance_m, time_s):

    if distance_m < 0:
        raise ValueError("Distance cannot be negative")

    if time_s <= 0:
        raise ValueError("Time must be greater than zero")

    return distance_m / time_s


try:
    distance = float(input("Distance in metres: "))
    elapsed_time = float(input("Time in seconds: "))

    speed_mps = calculate_speed(distance, elapsed_time)

    speed_kmph = speed_mps * 3.6

    print(f"Average speed: {speed_mps:.2f} m/s")
    print(f"Average speed: {speed_kmph:.2f} km/h")

except ValueError as error:
    print("Input error:", error)
