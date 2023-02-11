import base64
import requests
import os
import json

CLIENT_ID=os.environ['CLIENT_ID']
CLIENT_SECRET=os.environ['CLIENT_SECRET']

async def auth():
  url = "https://accounts.spotify.com/api/token"
  encoded = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode())
  headers = {
    'Authorization': f'Basic {encoded.decode()}'
    }
  data = {'grant_type': 'client_credentials'}
  response = requests.post(
    url,
    headers=headers,
    data=data
  )
  return response.json()['access_token']

async def post(access_token: str):
  url = "https://api.spotify.com/v1/recommendations"
  seed_artists="4NHQUGzhtTLFvgF5SZesLK"
  seed_genres="classical,country"
  seed_tracks="0c6xIDDpzE81m2q797ordA"

  headers = {
    'Authorization': f'Bearer {access_token}'
  }

  params = {
    'seed_artists': seed_artists,
    'seed_genres': seed_genres,
    'seed_tracks': seed_tracks,
    'limit': 1
  }

  response = requests.get(
    url,
    headers=headers,
    params=params,
  )

  return response.json()