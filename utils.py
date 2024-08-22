dict_criteriaprompts = {"criteria text1": "Prompt1",
                        "criteria text2": "Prompt2",
                        "criteria text3": "Prompt3"}


def getCriteria() -> list:
    return ["Criteria Text1", "Criteria Text2", "Criteria Text3"]


def getPrompt_text(query_prompt: str) -> str:
    print(query_prompt.lower())
    try:
        print(dict_criteriaprompts[query_prompt.lower()])
        return dict_criteriaprompts[query_prompt.lower()]
    except:
        print("no text")
        return ""