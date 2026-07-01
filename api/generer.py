from http.server import BaseHTTPRequestHandler
import json
import os
from groq import Groq


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)


class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        length = int(self.headers["Content-Length"])

        data = self.rfile.read(length)

        infos = json.loads(data)


        sujet = infos.get("theme")
        plateforme = infos.get("plateforme")
        style = infos.get("style")
        ton = infos.get("ton")
        duree = infos.get("duree")



        prompt = f"""

Tu es CreatorAI Engine.

Tu es un expert mondial en création de vidéos courtes virales.

Tu connais :
- TikTok
- YouTube Shorts
- Instagram Reels
- storytelling
- marketing
- rétention
- psychologie des spectateurs


Crée une vidéo complète.


Sujet :
{sujet}


Plateforme :
{plateforme}


Style :
{style}


Ton :
{ton}


Durée :
{duree}



Répond exactement dans cette structure :



TITRE:

HOOK:

SCRIPT:

PLANS:

MONTAGE:

DESCRIPTION:

HASHTAGS:

MINIATURE:

CONSEILS:





Ne fais pas une réponse générique.
Adapte tout au sujet.
Si le sujet est gaming parle comme un expert gaming.
Si le sujet est sport parle comme un coach.
Si le sujet est business parle comme un entrepreneur.


"""


        try:


            response = client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                messages=[

                    {
                    "role":"system",
                    "content":"Tu es CreatorAI Engine."
                    },


                    {
                    "role":"user",
                    "content":prompt
                    }

                ],


                temperature=0.8

            )


            resultat = response.choices[0].message.content



            self.send_response(200)

            self.send_header(
                "Content-type",
                "application/json"
            )

            self.end_headers()


            self.wfile.write(
                json.dumps({
                    "resultat":resultat
                }).encode()
            )



        except Exception as e:


            self.send_response(500)

            self.end_headers()


            self.wfile.write(

                json.dumps({

                    "erreur":str(e)

                }).encode()

            )
