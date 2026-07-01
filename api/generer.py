import os
import json
from groq import Groq

def handler(request):

    try:
        key = os.environ.get("GROQ_API_KEY")

        if not key:
            return {
                "statusCode": 500,
                "body": json.dumps({
                    "error": "Clé GROQ absente"
                })
            }

        client = Groq(api_key=key)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": "Dis bonjour"
                }
            ]
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "result": response.choices[0].message.content
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
