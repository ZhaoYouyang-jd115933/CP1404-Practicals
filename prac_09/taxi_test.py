from prac_09.taxi import Taxi

def main():
    """Test taxi class"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"The current fare: ${my_taxi.get_fare()}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"The current fare: ${my_taxi.get_fare()}")

main()