	•	main.py runs the agent
	•	Agent uses the tool ask_openai()
	•	The tool sends a prompt to OpenAI
	•	OpenAI thinks and responds
	•	Agent returns the response

	•	smolagents = agents + tools
	•	Tool = talks to OpenAI API
	•	Agent = focuses only on what it wants to do, not how OpenAI works
	•	Very reusable: if you change API later, you just fix the Tool, not the Agent

 smolagents + OpenAI = agent that uses a Tool to talk to AI and get smart answers!

We are building the structure exactly like smolagents style:
	•	Agent = smart decision maker
	•	Tool = helper function
	•	Main = runner that connects everything

smolagents = style of coding (not always a package)
-Agents are smart decision makers
-Tools are small simple helpers
-Together they create smart, modular, scalable projects
