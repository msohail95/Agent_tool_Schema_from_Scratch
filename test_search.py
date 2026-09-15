from tools.search_tool import web_search


query = input(
    "Search: "
)


results = web_search(query)


for r in results:

    print("\nTITLE:")
    print(r["title"])

    print("URL:")
    print(r["url"])

    print("DESCRIPTION:")
    print(r["snippet"])