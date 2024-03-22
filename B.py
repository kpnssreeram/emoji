def getVpcByUniverse(universe):
    switch = {
        'ci': 'qa',
        'cert': 'qa',
        'anon': 'qa',
        'uat': 'prod',
        'bazaar': 'prod'
    }
    return switch.get(universe, 'default')

# This code will only run if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: B.py <universe>")
        sys.exit(1)

    universe = sys.argv[1]
    vpc = getVpcByUniverse(universe)
    print(vpc)