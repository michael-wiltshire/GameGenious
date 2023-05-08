import openai

API_KEY = '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'										
openai.api_key = API_KEY
model = "text-curie-001"

response = openai.Completion.create(
	model = model,
	prompt = 'What are 3 hard champions in league of legends?',
	max_tokens = 1000,
	temperature=0.9,
	n=3
	)

print(response)