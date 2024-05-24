from gitsint import *


async def profile(user, client, out,args):
    name = "aprofile"
    domain = "Github Profile"
    method="api"
    frequent_rate_limit=True
    
    """Check if the input is a valid username address

    Keyword Arguments:
    username       -- String to be tested

    Return Value:
    User     -- True if string is an username, False otherwise
    """
    headers = {}
    if args.token:
        headers['Authorization'] = f"Bearer {args.token[0]}"
    url = f"https://api.github.com/users/{user['login']}"
    r = requests.get(url.format(user['login']), headers=headers)
    res = r.json()

    out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
            "rateLimit": False,
            "exists": True,
            "data": res,
            "others": None})

