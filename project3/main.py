from crewai import Agent, Task, Crew, LLM
import random
import json
import re
#from json_repair import repair

# Initialize the Ollama LLM
llm = LLM(model="ollama/phi3:3.8b")

# Create the Fact-Checking Agent
fact_check_agent = Agent(
    role="Fact-Checker",
    goal="""Verify the claims in a given tweet and provide their accuracy with evidence.""",
    backstory="""You are a highly accurate fact-checker trained to evaluate statements and provide verified and unverified claims with evidence.""",
    llm=llm
)

# Create the Sentiment Analysis Agent
sentiment_agent = Agent(
    role="Sentiment Analyzer",
    goal="""Analyze the sentiment of the given tweet and provide tone, emotional triggers, and the potential impact.""",
    backstory="""You are a sentiment analysis expert who accurately identifies the tone and emotional context of statements.""",
    llm=llm
)

tweet_gen_agent = Agent(
    role="Creative Content Writer",
    goal="""Generate a compelling tweet based on trending topics, ensuring it is engaging, relevant, and concise.""",
    backstory="""You are a creative writer with expertise in crafting tweets that engage a broad audience while staying relevant to current trends.""",
    llm=llm
)

# Define the task to analyze the tweet
tweet_text = "AI has increased productivity by 500% in 2024"
fact_check_task = Task(
    description=f"""Fact-check the following tweet: "{tweet_text}" """,
    expected_output="""A JSON object containing accuracy_score, verified_claims, unverified_claims, and evidence.""",
    agent=fact_check_agent
)

sentiment_task = Task(
    description=f"""Analyze the sentiment of the following tweet: "{tweet_text}" """,
    expected_output="""A JSON object containing score, tone, emotional_triggers, and potential_impact.""",
    agent=sentiment_agent
)

# Task: Generate tweets from trending topics
trending_topics = ["AI advancements", "Climate Change", "Space Exploration", "Mental Health Awareness"]
selected_topic = random.choice(trending_topics)

tweet_gen_task = Task(
    description=f"""Generate a compelling tweet based on the trending topic: "{selected_topic}" """,
    expected_output="""A short, engaging tweet related to the selected topic.""",
    agent=tweet_gen_agent
)

# Initialize the Crew with both agents and tasks
crew = Crew(
    agents=[sentiment_agent],
    tasks=[sentiment_task],
    verbose=True
)

def clean_response(response):
    # Function to parse and remove redundancy from the response
    try:
        # Convert response to string if it's not already
        if not isinstance(response, str):
            response = str(response)
        
        # Remove comments from the JSON string
        cleaned_response = re.sub(r'//.*', '', response)
        
        # Remove any extra whitespace and ensure proper JSON formatting
        cleaned_response = re.sub(r'\s+', ' ', cleaned_response).strip()
        
        # Parse the cleaned JSON string
        parsed = json.loads(cleaned_response)
        return parsed
    except json.JSONDecodeError as e:
        print(f"Error parsing response: {e}")
        print(f"Failed to decode JSON: {cleaned_response}")
        return response  # Return raw response if JSON parsing fails

# Execute the tasks
result = crew.kickoff()

# Print the results
print(clean_response(result))