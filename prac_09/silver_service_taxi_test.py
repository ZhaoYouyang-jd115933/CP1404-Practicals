from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi"""
    hummer = SilverServiceTaxi(fanciness=4, name="Hummer", fuel=200)
    standard = SilverServiceTaxi(fanciness=2, name="Standard", fuel=100)

    # Test initial state
    print("Initial state:")
    print(hummer)
    print(standard)
    print()

    # Test fare calculation
    print("Fare tests:")
    hummer.drive(10)
    print(f"Hummer runs 10km: {hummer}")
    print(f"Fare: ${hummer.get_fare():.2f}")

    standard.drive(18)
    print(f"Standard runs 18km: {standard}")
    print(f"Fare: ${standard.get_fare():.2f}")
    print()

main()