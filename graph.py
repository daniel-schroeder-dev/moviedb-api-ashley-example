from urllib.request import urlopen
from urllib.parse import urlencode
from json import loads, dumps, dump


# Example request: https://api.themoviedb.org/3/movie/550?api_key=YOUR_API_KEY


class Graph:
    API_KEY = "YOUR_API_KEY"
    BASE_API_URL = "https://api.themoviedb.org/3"
    SEARCH_PERSON_ENDPOINT = "/search/person"

    def search_for_person(self, person_name):
        query_params = {
            "api_key": self.API_KEY,
            "query": person_name,
        }
        encoded_query_params = urlencode(query_params)
        request_url = (
            f"{self.BASE_API_URL}{self.SEARCH_PERSON_ENDPOINT}?{encoded_query_params}"
        )

        response_data = []
        with urlopen(request_url) as response:
            response_data = loads(response.read())

        return response_data["results"]


if __name__ == "__main__":
    graph = Graph()
    search_results = graph.search_for_person("George Clooney")
    print(dumps(search_results, indent=4))

    with open("search-results.json", mode="wt", encoding="utf-8") as json_file:
        dump(search_results, json_file, indent=4)
