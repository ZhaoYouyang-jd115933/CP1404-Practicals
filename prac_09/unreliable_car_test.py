from unreliable_car import UnreliableCar
TEST_RUNS = 100
ATTEMPT_DISTANCE = 10
def main():
    """Test for UnreliableCar class with repeated drive attempts"""
    car = UnreliableCar(reliability=30, name="TestCar", fuel=1000)
    successful_drives = 0
    total_distance = 0
    for number in range(TEST_RUNS):
        distance = car.drive(ATTEMPT_DISTANCE)
        if distance > 0:
            successful_drives += 1
            total_distance += distance
    print(f"Tested car with 30% reliability over {TEST_RUNS} attempts:")
    print(f"Each attempt tried to drive {ATTEMPT_DISTANCE} km.")
    print(f"Successful drives: {successful_drives} out of {TEST_RUNS}")
    print(f"Total distance driven: {total_distance} km")

main()
