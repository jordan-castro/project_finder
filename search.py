from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.resources.projects.exceptions import ProjectsNotFoundException
from freelancersdk.resources.projects.helpers import (
    create_search_projects_filter,
    create_get_projects_project_details_object,
    create_get_projects_user_details_object
)

# Search for some projects
def search(session, query:str):
    # The filter for the search
    search_filter = create_search_projects_filter(
        sort_field='time_updated',

        or_search_query=True,
    )

    try:
        projects = search_projects(
            session,
            query=query,
            search_filter=search_filter,
        )
    except ProjectsNotFoundException as e:
        print(f"Error message in search function: {e.message}")
        print(f"Server response: {e.error_code}")
        return None
    else:
        return projects


# This will handle getting all the needed info from the projects
def pretty_info(projects: dict, max_bid_count=50):
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