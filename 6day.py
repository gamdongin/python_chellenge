import requests

while True:
    movie_id = input("영화 id :")
    url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
    response = requests.get(url)
    data = response.json()
    
    title = data["title"]
    overview = data["overview"]
    vote_average = data["vote_average"]
    print(f"\ntitle : {title}\n\noverview : {overview}\n\nvote_average : {vote_average}\n")
    
    # id = 12
    # 'original_title': 'Finding Nemo', 'overview': "Nemo, an adventurous young clownfish, is unexpectedly taken from his Great Barrier Reef home to a dentist's office aquarium. It's up to his worrisome father Marlin 
    # 'title': 'Finding Nemo' // 'vote_average': 7.816
    

    
