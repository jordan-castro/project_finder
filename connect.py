from freelancersdk.session import Session


# Create a connection to the Freelancer api
def connect_api():
    # The api key
    ouath_token = "API_KEY"
    return Session(ouath_token)
