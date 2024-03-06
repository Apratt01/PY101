def greetings(name, status):
    name = (" ").join(name)
    return (f"Hello, {name}! Nice to have a {status['title']} "
        f"{status['occupation']}")


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.