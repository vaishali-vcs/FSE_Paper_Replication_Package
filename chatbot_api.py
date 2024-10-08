from openai import OpenAI
from flask import Flask, request, jsonify

client = OpenAI(api_key="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")

messages = []

intentional_elements_keys = ['Actors', 'Goals', 'Softgoals', 'Tasks', 'Resources']
intentional_elements = {}
index_key = 0

exampleuserstorytext_1 = f""" The objective of Traffic Simulator is to generate cars and the simulator should also focus on 
the following quality attributes: ease of use, realistic simulation and simple design. In order to generate cars, 
the simulation can either create new cars or keep the same cars. In order to run the simulation the system depends on 
resources are car objects.  The task of creating new cars contributes towards the following goals: Realistic 
simulation and Simple design"""

delimiter = "####"
context = f"""
You are a requirements engineer with with an eagle eye for understanding what stakeholders' requirements are and how they can be fulfilled . You "
                   "carefully analyse user stories with great detail and extract important elements from them. User stories are semi-structured pieces of text that express stakeholders' intention, role, and rationale for their need. A user story template takes the following form: as a [WHO], I want/need [WHAT], so that [RATIONALE].

                   Goal Modelling is employed to organize the user stories, and reveal how they are related to each other. 
                   A background of GRL (Goal-oriented Requirement Language) is provided below. 
GRL is a modeling language for specifying intentions, business goals, and non-functional requirements of multiple stakeholders. 
GRL can be used to specify alternatives that have to be considered, decisions that have been made, and rationales for making decisions. 
A GRL model is a connected graph of intentional elements. The model shows softgoals, goals, tasks and the relationship between the different intentional elements in the model. 
Here is a small description of intentional elements. 
'Actors':  An actor represents a stakeholder of a system or the system itself. Actors are holders of intentions; they are the active entities in the system or its environment who want goals to be achieved, 
tasks to be performed, resources to be available, and softgoals to be satisfied. 
'Goals': A goal is defined as something that the stakeholders hope to achieve as a result of the development of a software product. 
'SoftGoals': A softgoal is a condition or state of affairs in the world that the actor would like to achieve, but unlike in the concept of (hard) goal, there are no clear-cut criteria for whether the condition is achieved, and it is up to subjective judgement and interpretation of the developer to judge whether a particular state of affairs in fact achieves sufficiently the stated softgoal.
Softgoals are often related to non-functional requirements, whereas goals are related to functional requirements. Along with the SoftGoals mentioned in the user story you must include a set of specifications that describe the system’s operation capabilities and constraints and attempt to improve its 
functionality. These are basically the requirements that outline how well it will operate including things like speed, security, reliability, data integrity,etc. 
'Tasks': Tasks represent solutions to (or operationalizations of) goals and softgoals. Note tasks can be decomposed into subtasks that must be performed.
Different links connect the elements in a GRL model. AND, IOR (Inclusive OR), and XOR (eXclusive OR) decomposition links allow an element to be decomposed into sub-elements. 
Contribution links describe how softgoals, task, believes, or links contribute to others. Graphically, a contribution link describes how one intentional element contributes to the satisficing of another intentional element. A Contribution relationships can be of one of the following kinds-AND, OR, EQUAL, HURT, and HELP.  
Dependency links are relationships between intentional elements, which can model dependencies between actors.

An engineer is working on the below set of user stories: 

He created an initial goal model with the following elements:
"""
explain_system_message = {
    "role": "system",
    "content": context,
}

messages.append(explain_system_message)

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def Invoke_api():
    if request.method == 'POST':
        new_prompt_data = request.data

        response = client.chat.completions.create(
            model="gpt-4",
            temperature=0.8,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in messages
            ],
            stream=False,
        )
        # Get the assistant's reply
        reply = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": reply})

        return jsonify({
           "status": "success", "message": reply
        })


if __name__ == '__main__':
    Invoke_api()
