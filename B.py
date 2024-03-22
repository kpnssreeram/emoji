def getVpcByUniverse(universe):
    switch = {
        'ci': 'qa',
        'cert': 'qa',
        'anon': 'qa',
        'uat': 'prod',
        'bazaar': 'prod'
    }
    return switch.get(universe, 'default')

def getAccountIdByUniverse(universe):
    switch = {
        'ci': '549050352176',
        'cert': '549050352176',
        'anon': '549050352176',
        'uat': '468552248569',
        'bazaar': '468552248569'
    }
    return switch.get(universe, 'default')

# This code will only run if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: B.py <function_name> <universe>")
        sys.exit(1)

    function_name = sys.argv[1]
    universe = sys.argv[2]

    functions = {
        'getVpcByUniverse': getVpcByUniverse,
        'getAccountIdByUniverse': getAccountIdByUniverse
    }

    if function_name in functions:
        result = functions[function_name](universe)
        print(result)
    else:
        print(f"Invalid function name: {function_name}")
        sys.exit(1)