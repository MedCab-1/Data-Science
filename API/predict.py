import basilica
import numpy as np
import pandas as pd
from scipy import spatial
from .models import DB, Strain

def predict_strains(user_input):
    '''Returns top 5 strains based on desired characteristics'''
    embedded_df = pd.read_pickle("static/medembedv2.pkl")

    # Embed the user input
    with basilica.Connection('36a370e3-becb-99f5-93a0-a92344e78eab') as c:
        user_input_embedding = list(c.embed_sentence(user_input))
    
    # Score each strain's similarity to the user input
    scores = []
    for i in range(2351):
        stored_embed = embedded_df[0][i]
        score = 1 - spatial.distance.cosine(stored_embed, user_input_embedding)
        scores.append(score)
    
    #get the strain id of top 5 scores
    top_scores = sorted(scores, reverse=True)[:5]
    strain_ids = [scores.index(x) for x in top_scores]

    #return top 5 strain names
    names=[]
    for i in strain_ids:
        strain = Strain.query.filter(Strain.id==i).one()
        names.append(strain.name)
    return names
    