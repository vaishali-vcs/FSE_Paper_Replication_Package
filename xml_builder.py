from yattag import Doc, indent
import re
import random
import pickle


class IntentionalObject(object):
    def __init__(self, name, id, parentid, type):
        self.name = name.strip()
        self.id = id
        self.parent_id = parentid
        self.type = type


def find_Parent_id(lst_intentional_objects: list, key: str) -> int:
    for obj in lst_intentional_objects:
        if obj.name == key:
            return obj.id
        else:
            return -1


def generate_id(lst_intentional_objects: list) -> int:
    seed = random.randint(1, 100)
    for int_object in lst_intentional_objects:
        if int_object.id != seed:
            continue
        else:
            seed = random.randint(1, 100)

    return seed


def return_Tasks(intentional_element: str) -> dict:
    # Splitting the string based on the main categories
    main_categories = re.split(r'\n-\s', intentional_element.strip())
    main_categories = [cat for cat in main_categories if cat]

    # Further splitting each category into its title and sub-items
    structured_data = {}
    for category in main_categories:
        parts = category.split(':\n  - ')
        if len(parts) == 2:
            title = parts[0].strip()
            sub_items = parts[1].split('\n  - ')
            structured_data[title] = sub_items

    return structured_data


def build_XML(intentional_elements: dict) -> None:
    list_intentional_elements = []
    # Section for creating XML
    doc, tag, text = Doc().tagtext()
    doc.asis("""<?xml version='1.0' encoding='ISO-8859-1'?>""")
    # print(intentional_elements)

    with tag('grl-catalog', ("catalog-name", "URNspec"), description=""):
        with tag('actor-def'):
            # Add Actors
            if 'Actors' in intentional_elements.keys():
                actors = intentional_elements['Actors']
                actors_list = actors.split("\n- ")
                actors_list[0] = actors_list[0].replace("- ", "")

                # print(actors_dict)
                for actor in actors_list:
                    objid = generate_id(list_intentional_elements)
                    list_intentional_elements.append(IntentionalObject(name=actor, id=objid, parentid=-1, type='actor'))
                    doc.stag('actor', id=objid, name=actor)

        with tag('element-def'):
            # Add Goals
            if 'Goals' in intentional_elements.keys():
                goals = intentional_elements['Goals']
                goals_list = goals.split("\n- ")
                goals_list[0] = goals_list[0].replace("- ", "")

                # print(goals_list)
                for goal in goals_list:
                    objid = generate_id(list_intentional_elements)
                    list_intentional_elements.append(
                        IntentionalObject(name=goal, id=objid, parentid=-1, type='goal'))
                    doc.stag('intentional-element', id=objid, name=goal, type="Goal", decompositiontype='AND')

            # Add Goal_Tasks
            if 'Goals_Tasks' in intentional_elements.keys():
                Goals_Tasks = intentional_elements['Goals_Tasks']
                structured_goal_tasks = return_Tasks(Goals_Tasks)

                for Goaltitle, sub_Tasks in structured_goal_tasks.items():

                    parent_objid = find_Parent_id(list_intentional_elements, Goaltitle)
                    for task in sub_Tasks:
                        objid = generate_id(list_intentional_elements)
                        list_intentional_elements.append(
                            IntentionalObject(name=task, id=objid, parentid=parent_objid, type='Task'))
                        doc.stag('intentional-element', id=objid, name=task, type="Task")

            # Add Soft Goals
            if 'Softgoals' in intentional_elements.keys():
                sf_goals = intentional_elements['Softgoals']
                sf_goals_list = sf_goals.split("\n- ")
                sf_goals_list[0] = sf_goals_list[0].replace("- ", "")

                for sf_goal in sf_goals_list:
                    objid = generate_id(list_intentional_elements)
                    list_intentional_elements.append(
                        IntentionalObject(name=sf_goal, id=objid, parentid=-1, type='Softgoal'))
                    doc.stag('intentional-element', id=objid, name=sf_goal, type="Softgoal")

            # Add Soft_Goals_Tasks
            if 'Softgoals_Tasks' in intentional_elements.keys():
                Softgoals_Tasks = intentional_elements['Softgoals_Tasks']
                Softgoals_Tasks_list = Softgoals_Tasks.split("\n- ")
                Softgoals_Tasks_list[0] = Softgoals_Tasks[0].replace("- ", "")

                # print(goals_list)
                for Task in Softgoals_Tasks_list:
                    doc.stag('intentional-element', id=1, name=Task, type="Task")

            # Add Soft_Goals_Tasks
            if 'Softgoals_Tasks' in intentional_elements.keys():
                Softgoals_Tasks = intentional_elements['Softgoals_Tasks']
                structured_softgoal_tasks = return_Tasks(Softgoals_Tasks)

                for sgGoaltitle, sub_Tasks in structured_softgoal_tasks.items():

                    parent_objid = find_Parent_id(list_intentional_elements, sgGoaltitle)
                    for task in sub_Tasks:
                        objid = generate_id(list_intentional_elements)
                        list_intentional_elements.append(
                            IntentionalObject(name=task, id=objid, parentid=parent_objid, type='Task'))
                        doc.stag('intentional-element', id=objid, name=task, type="Task")

                print(list_intentional_elements)
    text_contents = ''

    text_contents = indent(
        doc.getvalue(),
        indentation=' ' * 4,
        newline='\r\n'
    )
    # print(text_contents)
    return text_contents


if __name__ == '__main__':
    build_XML({'Actors': '- superuser\n- admin\n- user\n- recyclingfacility\n- recyclingfacility representative\n- '
                         'administrators'})
