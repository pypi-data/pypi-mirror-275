import requests

def image_ai(text, key):
    if not text:
        return {'error': 'No text provided'}, 400
    if not key:
        return {'error': 'Enter your key ?'}, 400

    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={
            'Authorization': f'Bearer {key}',
            'Content-Type': 'application/json'
        },
        json={
            'prompt': text,
            'n': 1,
            'size': '1024x1024'
        }
    )

    if response.status_code != 200:
        return {'error': 'Failed to generate image', 'details': response.json()}, response.status_code

    image_url = response.json()['data'][0]['url']
    return {'dev': 'by : @SaMi_ye', 'url': image_url}
