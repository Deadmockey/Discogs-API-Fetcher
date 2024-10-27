from dotenv import load_dotenv
import discogs_client
import os


def main():
    load_dotenv()
    TOKEN = os.environ["TOKEN"]
    client = discogs_client.Client("TestApp", user_token=TOKEN)
    test_search = client.search("luv(sic)")
    print(test_search[0].artists[0])


main()
