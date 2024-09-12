# Towards Extracting and Validating goal models using Large Language Models

This project consists of the code, the inputs, prompts, and outputs used in the paper titled "Towards Extracting and Validating goal models using Large Language Models". 
This paper presents early research proposing a technique using Large Language Models (LLMs), like GPT-4, to automatically generate goal models from user stories. The approach
employs Iterative Prompt Engineering to guide the LLM in extracting intentional elements and generating XML representations using the Goal-oriented Requirements Language (GRL), visualized with the jUCMNav tool.

## Repository Structure
1. 'Evaluation' folder is the root file for all th input and the output data. 
2. 'Inputs' folder consists of the user stories that were used to evaluate the approach.
3. 'Prompts' folder consists of the textual prompts used to generate responses.
4. 'Outputs' folder consists of responses from GPT-4.
5. 'utils.py' file consists of helper code for loading user stories and saving the LLM responses.
7. 'chatbot_api.py' consists of the driver code for goal model generation.
8. 'evaluator_report_generator.py' consists of the driver code for goal model evaluation.

## How to install?
Following are steps to be followed:
1. Create a Virtual Environment.
2. Install Python 3.9, Pandas, and Tensorflow.
3. PIP Install openai using the below command  <br />
   *pip install openai*
   *pip install streamlit*
5. Clone this project.
6. Procure an OPENAI API Key.
7. Paste the key in the .toml file in Streamlit installation folder without any double/single quotes.
8. Run the script - chatbot_api.py to generate a goal model
9. Run the script - evaluator_report_generator.py to evaluate an output

## How to tweak this project for your own uses?
Since this is a boilerplate version of the project, it has been tested only on User Stories as the input. I'd encourage you to clone and rename this project to test it on other forms of requirements.

## Find a bug?
If you found an issue or would like to submit an improvement to this project, please submit an issue using the 'Issues' tab. If you would like to submit a PR with a fix, reference the issue you created. 

## References
[1] M. van Zee, F. Bex, and S. Ghanavati, “Rationalgrl: A framework for argumentation and goal modeling,” Argument & Computation, vol. 12,
pp. 191–245, 2021. </br>
[2] T. Gunes and F. B. Aydemir, “Automated goal model extraction from user stories using nlp,” pp. 382–387, 2020. </br>
[3] M. Baslyman, B. Almoaber, D. Amyot, and E. M. Bouattane, “Activitybased process integration in healthcare with the user requirements
notation,” 05 2017, pp. 151–169. </br>
[4] D. Amyot, “Introduction to the user requirements notation: learning by example,” Computer Networks, vol. 42, no. 3, pp. 285–301, 2003. </br>
[5] G. v. Bochmann, “Goal modeling and grl,” https://www.site.uottawa.ca/∼bochmann/SEG3101/Notes/SEG3101-ch3-5%20-%20Goal%20modeling%20-%20GRL.pdf, 2009, accessed: 2023–12-06. </br>
[6] J. Horkoff and E. Yu, “Interactive goal model analysis for early requirements engineering,” Requirements Engineering, vol. 21, no. 1, pp. 29–61, 2016. [Online]. Available: https://doi.org/10.1007/s00766-014-0209-8
