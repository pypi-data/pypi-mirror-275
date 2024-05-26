1. Install via pip 
``` pip install crewai-logging-patch```
2. Add import into your main crewai file - This needs to be above any other crewai imports
``` from logger_patch import apply_monkey_patch```
3. Add the patch method to your code - This needs to be above any other crewai imports
```apply_monkey_patch()```
4. Add the following directly below your agent instances - You must use your agent names in place of <placeholder_name>
```<placeholder_name>._logger = crewai.utilities.Logger(verbose_level=<placeholder_name>.verbose)```
5. And the same below your crew instance, again you must use your crew name in place of <placeholder_name>
```<placeholder_name>._logger = crewai.utilities.Logger(verbose_level=<placeholder_name>.verbose)```
6. Ensure that verbose=True is set in your agent and crew instances
7. Below is an example crewfile with all of this implemented
```python
import os
from logger_patch import apply_monkey_patch

# Apply the monkey patch
apply_monkey_patch()

# Now use crewai and other imports as usual
from crewai import Agent, Crew, Task, Process
import crewai.utilities

# Setup LM Studio environment variables
os.environ['OPENAI_API_BASE'] = 'http://localhost:1234/v1'
os.environ['OPENAI_API_KEY'] = 'sk-111111111111111111111111111111111111111111111111'
os.environ['OPENAI_MODEL_NAME'] = 'Meta-Llama-3-8B-Instruct-imatrix'

# Create the agent
try:
    researcher = Agent(
        role='Researcher',
        goal='Research the topic',
        backstory='As an expert in the field of {topic}, you will research the topic and provide the necessary information',
        max_iter=3,
        max_rpm=100,
        verbose=True,
        allow_delegation=False,
    )

    # Manually set the logger to ensure it's the patched logger
    researcher._logger = crewai.utilities.Logger(verbose_level=researcher.verbose)

    # Create the task
    research_task = Task(
        description='Research the topic',
        agent=researcher,
        expected_output='5 paragraphs of information on the topic',
        output_file='research_result.txt',
    )


    # Create the crew
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        process=Process.sequential,
        verbose=True,
        memory=False,
        cache=False,
        max_rpm=100,
    )

    # Manually set the logger for crew to ensure it's the patched logger
    crew._logger = crewai.utilities.Logger(verbose_level=crew.verbose)

    # Start the crew
    result = crew.kickoff(inputs={'topic': '70s, 80s and 90s Australian rock bands'})

except Exception as e:
    print(f"An error occurred: {e}")
```
