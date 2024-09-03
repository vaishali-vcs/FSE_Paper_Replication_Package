import json
import os
import pandas as pd
import openai

dict_criteriaprompts = {"duplicate names of intentional elements": "In the XML enclosed using triple back ticks, do "
                                                                   "you see duplicate values for"
                                                                   "'name' attribute? Answer using yes or no only. Do not include any explanation.",

                        "duplicate identifiers of intentional elements": "In the XML enclosed using triple back ticks,"
                                                                         " do you see duplicate "
                                                                         "values for"
                                                                         "'id' attribute? Answer using yes or no only. Do not include any explanation.",

                        "empty intentional element": "In the XML enclosed using triple back ticks, "
                                                     "do you see empty string as a value for "
                                                     "'name' attribute? Answer using yes or no only. Do not include any explanation.",

                        "compare model modified and created dates": "In the XML enclosed using triple back ticks, "
                                                                    "if you see the attributes 'modified' and "
                                                                    "'created', convert the values of both the"
                                                                    "attributes to Date and compare them. Is value of "
                                                                    "'modified' attribute greater than the value of "
                                                                    "'created' attribute?  Answer Yes, or No if the "
                                                                    "attributes 'modified' and 'created' are present. "
                                                                    "Otherwise answer Not Applicable. Do not include any explanation.",

                        "empty goal model": "In the XML enclosed using triple back ticks, do you see that the element "
                                            "named 'grl-catalog' is empty? Answer yes or no only. Do not include any explanation.",

                        "intentional elements contained outside grlspec": "In the XML enclosed using triple back "
                                                                          "ticks, do you see any content outside of "
                                                                          "the section named 'grl-catalog'? Answer yes or no only. Do not include any explanation.",

                        "intentional element has name, id, and type": "In the XML enclosed using triple back ticks, "
                                                                      "do you find an element with name "
                                                                      "'intentional-element' with missing the"
                                                                      "following attributes missed- name, id, type? Answer yes or no only. Do not include any explanation.",

                        "actors section found in the model": "Does the XML have a section with title 'actor-def'?Yes or No?",

                        "actors used in links": "In the given XML, each actor element has an 'id' attribute, do you see the value of 'id' "
                            "attribute of an actor element used as the value for 'srcid' or 'destid' attributes "
                            "within the section named 'link-def'?Answer yes or no only. Do not include any explanation.",


                        "section for linked actors and intentional elements found in the model": "Does the XML have a section with title "
                                                                                                 "'actor-IE-link-def'? Answer using yes or no only? Do not include any explanation.",

                        "multiple actors for one intentional element": "In the XML enclosed using triple back ticks, within the section with name "
                            "'actor-IE-link-def', do you see any element with same value for 'ie' attribute, "
                            "but different value for 'actor' attribute? Answer Yes or No? Do not include any explanation.",

                        "intentional element category": "In the XML enclosed using triple back ticks, for an element "
                                                        "with name 'intentional-element', is the value for 'type' "
                                                        "attribute of the tag one of the following values - Task, Goal, Softgoal, Resource, Belief? Answer yes or no only. Do not include any explanation.",

                        "intentional element default decomposition type": "In the XML enclosed using triple back "
                                                                          "ticks, for an element with name "
                                                                          "'intentional-element', is the value of "
                                                                          "attribute 'decompositiontype' of the tag one of the following "
                                                                          "values - AND, OR, XOR? Answer yes or no only. Do not include any explanation.",

                        "contribution type category": "In the XML enclosed using triple back ticks, if you see an "
                                                      "element with name 'contribution', is the value for the attribute "
                                                      "'contributiontype'"
                                                      " of the tag one of the following values- Make, Help, Break, Hurt?  Answer Yes, "
                                                      "or No if element with name 'contribution' is present. Otherwise answer Not Applicable. Do not include any explanation.",

                        "contribution link validation": "In the XML enclosed using triple back ticks,, if you see an "
                                                        "element with name 'contribution', are the values for srcid "
                                                        "and destid"
                                                        "attributes in each tag different? Answer Yes, or No if element with name "
                                                        "'contribution' is present. Otherwise answer Not Applicable. Do not include any explanation.",

                        "contribution link without source": "In the XML enclosed using triple back ticks, if you see "
                                                            "an element with name 'contribution', is the "
                                                            "value for srcid empty string, or is element with name "
                                                            "'contribution' missing attribute 'srcid'? Answer yes or no only. Do not include any explanation.",

                        "contribution link without destination": "In the XML enclosed using triple back ticks, if you "
                                                                 "see a element with name 'contribution',"
                                                                 "is the value for destid empty string, or is element "
                                                                 "with name 'contribution' missing attribute 'destid? "
                                                                 "Answer yes or no only. Do not include any explanation.",

                        "decomposition link without source": "In the XML enclosed using triple back ticks, if you see "
                                                             "an element with name 'decomposition', is the "
                                                             "value for srcid empty string, or is element with name "
                                                             "'decomposition' missing attribute 'srcid'? Answer yes or no only. Do not include any explanation.",

                        "decomposition link without destination": "In the XML enclosed using triple back ticks, "
                                                                  "if you see an element with name 'decomposition',"
                                                                  "is the value for destid empty string, "
                                                                  "or is element with name 'contribution' missing "
                                                                  "attribute 'destid? Answer yes or no only. Do not include any explanation.",

                        "decomposition link validation": "In the XML enclosed using triple back ticks, if you see an "
                                                         "element with name 'decomposition', are the values for srcid "
                                                         "and destid"
                                                         "attributes for the tag different? Answer Yes, or No if element with name "
                                                         "'decomposition' if present. Otherwise answer Not Applicable. Do not include any explanation."
                        }


def load_config(config_file: str) -> dict:
    """
    Loads the JSON configuration and sets the OpenAI API key.
    @param config_file:  Path to the JSON configuration file.
    @returns config: dictionary of the parsed configuration
    """
    with open(config_file) as json_file:
        config = json.load(json_file)
    # sets the OpenAI key
    openai.api_key = config["OPEN_AI_KEY"]
    return config


def load_userstories(input_dir: str) -> list:
    stories = []

    # iterate over files in
    # that directory
    for filename in os.listdir(input_dir):
        stories_file = os.path.join(input_dir, filename)

        # checking if it is a file
        if os.path.isfile(stories_file):

            # Opening file
            file1 = open(stories_file, 'r')
            file_content = ''

            for line in file1:
                file_content = file_content + line

            # Closing files
            file1.close()

        stories.append(file_content)
    return stories


def save_generated_model(output_dir: str, output_filename: str, contents: str) -> None:
    with open(os.path.join(output_dir,
                           output_filename), 'w') as generated_goalmodel:
        generated_goalmodel.write(contents)


def save_execution_results(output_dir: str, output_filename: str, results_lst: list) -> None:
    # Calling DataFrame constructor on the zipped lists, with columns specified
    results_df = pd.DataFrame(results_lst,
                              columns=['Stories', 'Status'])
    # save the contents as a csv
    results_df.to_csv(os.path.join(output_dir, output_filename))


def load_prompt_text(file_dir: str, textfile: str) -> str:
    # checking if it is a file
    # Opening file
    file1 = open(os.path.abspath(os.path.join(file_dir,
                                              textfile)))
    prompt_content = ''

    for line in file1:
        prompt_content = prompt_content + line

    # Closing files
    file1.close()

    return prompt_content


def getCriteria() -> list:
    return ["Actors section found in the model",
            "Actors used in links",
            "Compare model modified and created dates",
            "Contribution link validation",
            "Contribution link without source",
            "Contribution link without destination",
            "Contribution type category",
            "Decomposition link validation",
            "Decomposition link without source",
            "Decomposition link without destination",
            "Duplicate Identifiers of intentional elements",
            "Duplicate names of intentional elements",
            "Empty goal model",
            "Empty intentional element",
            "Intentional elements contained outside GRLspec",
            "Intentional element has name, id, and type",
            "Intentional element category",
            "Intentional element default decomposition type",
            "Multiple actors for one intentional element",
            "Section for linked actors and intentional elements found in the model"]


def getPrompt_text(query_prompt: str) -> str:
    # print(query_prompt.lower())
    try:
        # print(dict_criteriaprompts[query_prompt.lower()])
        return dict_criteriaprompts[query_prompt.lower().strip()]
    except:
        print(query_prompt)
        print("no text")
        return ""