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

def getTags(tag_type):
    tags = {
        'team': 'emodb-dev@bazaarvoice.com',
        'datatype': 'client+personal',
        'service': 'emoji'
    }
    return tags.get(tag_type, 'default')




if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: B.py <function_name> <argument>")
        sys.exit(1)

    function_name = sys.argv[1]
    argument = sys.argv[2]

    functions = {
        'getVpcByUniverse': getVpcByUniverse,
        'getAccountIdByUniverse': getAccountIdByUniverse,
        'getTags': getTags
    }

    if function_name in functions:
        result = functions[function_name](argument)
        print(result)
    else:
        print(f"Invalid function name: {function_name}")
        sys.exit(1)