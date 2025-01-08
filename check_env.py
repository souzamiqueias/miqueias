from decouple import config

groq_api_key = config('GROQ_API_KEY')
huggingface_api_key = config('HUGGINGFACE_API_KEY')
waha_api_url = config('WAHA_API_URL')

print(f"GROQ_API_KEY: {groq_api_key}")
print(f"HUGGINGFACE_API_KEY: {huggingface_api_key}")
print(f"WAHA_API_URL: {waha_api_url}")
