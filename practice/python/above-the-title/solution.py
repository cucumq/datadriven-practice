

def actor_genre_box_office(movies: list[dict], actors: list[dict], mapping: list[dict], genre: str, min_rating: float) -> dict:
    # df_movies = pd. DataFrame(movies)
    # df_actors = pd. DataFrame(actors)
    # df_mapping = pd. DataFrame(mapping)
    
    # df_movies_filtered = df_movies[(df_movies['genre']==genre) & (df_movies['rating']>=min_rating)]
    
    # df_merged = df_movies_filtered.merge(df_mapping, on='movie_id').merge(df_actors, on='actor_id')
    
    # df_result = df_result.groupby('name')['box_office'].sum()
    # return df_result.to_dict()
    
    qualified_movies = {}
    
    for movie in movies:
      if movie['genre'] == genre and movie['rating'] >=min_rating:
        qualified_movies[movie['movie_id']]=movie['box_office']
        
    actor_name = {actor['actor_id']:actor['name'] for actor in actors}
    result = {}
    for item in mapping:
      a_id = item['actor_id']
      m_id = item['movie_id']
      
      if m_id in qualified_movies:
        name = actor_name[a_id]
        box_office = qualified_movies[m_id]
        
        if name in result:
          result[name] +=box_office
        else:
          result[name] = box_office
    return result
         
     
    
    
