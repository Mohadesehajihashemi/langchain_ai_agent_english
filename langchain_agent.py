from langchain.agents import initialize_agent, Tool
from langchain.llms import Ollama
from datetime import datetime

# 1. Function to write generated code to a file with timestamp
def write_program_to_file(code: str) -> str:
    file_name = f"generated_program_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(code)
    return f"✅ Code successfully written to file `{file_name}` at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# 2. Define a Tool for the Agent
write_tool = Tool(
    name="WriteProgram",
    func=write_program_to_file,
    description="Generates and writes advanced Python code (loops, conditions, calculations) into a uniquely named file based on the current timestamp."
)

# 3. Initialize LLM on Ollama server
llm = Ollama(
    model="llama3.2",
    base_url="http://10.75.77.155:11434",
    timeout=30
)

# 4. Initialize Agent with Tool and LLM
agent = initialize_agent(
    tools=[write_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 5. Execute Agent with an advanced prompt
prompt = (
    "Write an advanced Python script that:\n"
    "- Defines a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\n"
    "- Uses a for loop to print even numbers and calculate their sum,\n"
    "- Prints 'Sum is high!' if the sum exceeds 20,\n"
    "- And saves the generated code using the WriteProgram tool."
)

result = agent.run(prompt)
print(result)
