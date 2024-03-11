import requests


def getDefinition(word: str):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    r = requests.get(url)
    res = r.json()

    if type(res) == dict:
        return False
    output = {}

    if 'phonetics' in res[0].keys() and len(res[0]['phonetics']) > 0:
        output['audio'] = res[0]["phonetics"][0]['audio']

    definitions = []
    for defs in res[0]['meanings'][0]['definitions']:
        definitions.append(f"👉 {defs['definition']}")

    output['definitions'] = "\n".join(definitions)
    return output


if __name__ == "__main__":
    from pprint import pprint as print

    print(getDefinition("memory"))
