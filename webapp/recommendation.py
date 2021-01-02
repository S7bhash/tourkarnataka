import numpy as np
import pandas as pd
import sqlite3 as sql
import os


def find_relation(name):
	basedir = os.path.abspath(os.path.dirname(__file__))
	database = os.path.join(basedir,"data.sqlite")
	conn = sql.connect(database)


	df = pd.read_sql_query("SELECT * FROM ratings",conn)


	dfr=pd.DataFrame(df.groupby('place')['rating'].mean())


	dfr['Count']=pd.DataFrame(df.groupby('place')['rating'].count())

	places=df.pivot_table(index='user_id',columns='place',values='rating')

	place_ratings = places[name]
	related_places = places.corrwith(place_ratings)
	recommendations = pd.DataFrame(related_places,columns=['relation'])
	recommendations.dropna(inplace=True)

	recommendations=recommendations.sort_values('relation',ascending=False)
	final_recommendations  = []

	for i in range(1,len(recommendations)):
		final_recommendations.append(recommendations.index[i])


	return final_recommendations