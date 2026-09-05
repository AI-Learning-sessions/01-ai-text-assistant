def add_prefix(text):
    return "AI: " + text


def make_uppercase(text):
    return text.upper()


def add_exclamation(text):
    return text + "!"


text = "hello python"

result = add_prefix(text)
result = make_uppercase(result)
result = add_exclamation(result)

print(result)