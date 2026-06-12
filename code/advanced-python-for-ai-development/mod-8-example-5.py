from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
def call_api(endpoint):
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()