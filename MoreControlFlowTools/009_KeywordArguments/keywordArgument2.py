def cheeseShop(kind, *arguments, **keywords):
    print("DO you have any", kind, "?")
    print("I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 30)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseShop("Limburger", "it's very runny, sir", "it's very runny, sir", shopKeeper="Jack", client="Alex")
