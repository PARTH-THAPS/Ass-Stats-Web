def urlparser(url):
    parsed_url = {
        "scheme": "",
        "host": "",
        "port": "",
        "path": "",
        "query": {},
        "fragment": ""
    }

    if "://" in url:
        scheme, remainder = url.split("://", 1)
        print(f"Remainder {remainder}")
        parsed_url["scheme"] = scheme
    else:
        remainder = url

    # ----- Fragment -----
    if "#" in remainder:
        remainder, fragment = remainder.split("#", 1)
        parsed_url["fragment"] = fragment

    # ----- Query -----
    if "?" in remainder:
        remainder, query_string = remainder.split("?", 1)
        query_pairs = query_string.split("&")

        query_dict = {}
        for pair in query_pairs:
            if "=" in pair:
                key, value = pair.split("=", 1)
                query_dict[key] = value
            else:
                query_dict[pair] = ""

        parsed_url["query"] = query_dict

    # ----- Host, Port, Path -----
    # Split path
    if "/" in remainder:
        host_port, path = remainder.split("/", 1)
        parsed_url["path"] = "/" + path
    else:
        host_port = remainder

    # Split port
    if ":" in host_port:
        host, port = host_port.split(":", 1)
        parsed_url["host"] = host
        parsed_url["port"] = port
    else:
        parsed_url["host"] = host_port

    return parsed_url


# ------------------ Testing ------------------

urls = [
    "https://www.example.com:8080/path/page?name=parth&age=22#section1",
    "http://testsite.org/blog/article?id=10"
]

for u in urls:
    print("URL:", u)
    print(urlparser(u))
    print()
