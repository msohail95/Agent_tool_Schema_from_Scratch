from tools.distance_tool import calculate_distance


source = input(
    "From: "
)


destination = input(
    "To: "
)


result = calculate_distance(
    source,
    destination
)


print(result)