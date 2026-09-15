from ddgs import DDGS

def web_search(query, max_results=5):

    results = []


    try:

        with DDGS() as search:

            search_results = search.text(
                query,
                max_results=max_results
            )


            for item in search_results:

                results.append({

                    "title": item.get("title"),

                    "url": item.get("href"),

                    "snippet": item.get("body")

                })


    except Exception as e:

        return {
            "error": str(e)
        }


    return results