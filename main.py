from agent import run_agent



request = input(
    "Request: "
)



answer = run_agent(
    request
)



print("\nFINAL ANSWER")
print(answer)