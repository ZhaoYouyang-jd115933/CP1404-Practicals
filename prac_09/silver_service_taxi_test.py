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

main()