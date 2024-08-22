dict_criteriaprompts = {"criteria text1": "Prompt1",
                        "criteria text2": "Prompt2",
                        "criteria text3": "Prompt3"}


def getCriteria() -> set:
    return ("Criteria Text1", "Criteria Text2", "Criteria Text3")


def getPrompt_text(query_prompt: str) -> str:

    try:
        return dict_criteriaprompts[query_prompt.lower()]
    except:
        return ""