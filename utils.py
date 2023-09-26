# This will handle getting all the needed info from the projects
def pretty_info(projects: dict, max_bid_count=50):
    """
    Filters and extracts specific information from a dictionary of projects.
    
    Args:
        projects (dict): A dictionary containing information about projects.
        max_bid_count (int, optional): The maximum bid count allowed for a project. Defaults to 50.
    
    Returns:
        list: A list of dictionaries containing the filtered and extracted information from the projects.
    """
    ps = list(filter(
        lambda x: x['bid_stats']['bid_count'] < max_bid_count,
        projects['projects']
    ))
    # Only keep the information needed
    info_needed = [
        "seo_url",
        "title",
        "preview_description",
        {        
            "bid_stats": [
                "bid_count",
                "bid_avg",
            ]
        }   
    ]
    # The projects that will be returned at the end
    rps = []
    for project in ps:
        p = {}
        # All info that is needed is saved in that variable
        for key in info_needed:
            # If we have a dictionary of information than for fucks sake nigga.
            if type(key) is dict:
                sk = list(key.keys())[0]
                for value in list(key.values())[0]:
                    p[value] = project[sk][value]
            else:
                # This one is easy
                p[key] = project[key]
        rps.append(p)

    return rps