from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.resources.projects.exceptions import ProjectsNotFoundException
from freelancersdk.resources.projects.helpers import (
    create_search_projects_filter,
)


def search_projects():
    pass


# Search for some projects
# def search(session, query:str):
#     # The filter for the search
#     search_filter = create_search_projects_filter(
#         sort_field='time_updated',
#         or_search_query=True,
#         languages=['en', 'es'],

#     )

#     try:
#         projects = search_projects(
#             session,
#             query=query,
#             search_filter=search_filter,
#         )
#     except ProjectsNotFoundException as e:
#         print(f"Error message in search function: {e.message}")
#         print(f"Server response: {e.error_code}")
#         return None
#     else:
#         return projects
