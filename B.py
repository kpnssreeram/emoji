def getDeployLabelByUniverse(universe):
    switch = {
        'ci': 'ci-agent',
        'cert': 'cert-agent',
        'anon': 'anon-agent',
        'uat': 'uat-agent',
        'bazaar': 'bazaar-agent'
    }
    return switch.get(universe, 'default-agent')

def getServiceNameByUniverse(universe):
    switch = {
        'ci': 'ci-service',
        'cert': 'cert-service',
        'anon': 'anon-service',
        'uat': 'uat-service',
        'bazaar': 'bazaar-service'
    }
    return switch.get(universe, 'default-service')

# This code will only run if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: B.py <function_name> <universe>")
        sys.exit(1)

    function_name = sys.argv[1]
    universe = sys.argv[2]

    if function_name == 'getDeployLabelByUniverse':
        result = getDeployLabelByUniverse(universe)
    elif function_name == 'getServiceNameByUniverse':
        result = getServiceNameByUniverse(universe)
    else:
        print(f"Invalid function name: {function_name}")
        sys.exit(1)

    print(result)