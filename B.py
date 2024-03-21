# B.py

def get_deploy_label_by_universe(universe):
    if universe == 'ci':
        return 'ci-agent'
    elif universe == 'cert':
        return 'cert-agent'
    elif universe == 'anon':
        return 'anon-agent'
    elif universe == 'uat':
        return 'uat-agent'
    elif universe == 'bazaar':
        return 'bazaar-agent'
    else:
        return 'default-agent'

# Example usage: get_deploy_label_by_universe('ci')
