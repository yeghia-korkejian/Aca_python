market =  {"dairy": ["yogurt", "cheese"],"fruits": ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]}
print (market)
market["candies"] = ["mars", "kinder", "twix"]
print (market)
market["fruits"] = set(market["fruits"])
market["fruits"] = list(market["fruits"])
market["fruits"].sort()
print (market)