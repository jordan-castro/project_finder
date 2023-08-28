from search import search, pretty_info
from connect import connect_api
import json


if __name__ == "__main__":
    api = connect_api()
    # TODO: specific queries and entries into the projects.json file.
    # I.E. Android: {}, iOS: {}, Python: {}, ...
    android_ps = search(api, "Android")
    # ps = search(connect_api(), "Android")
    # ps = pretty_info(ps, 10)
    # if ps:
    #     with open("projects.json", "w") as file:
    #         json.dump(ps, file, indent=4)