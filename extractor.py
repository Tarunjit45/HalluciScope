import spacy

nlp = spacy.load("en_core_web_sm")

def extract_claims(text):
    doc = nlp(text)
    claims = []
    
    # Day 1 Strategy: Only extract sentences with Entities (Dates, Orgs, Laws)
    for sent in doc.sents:
        if any(ent.label_ in ['DATE', 'GPE', 'ORG', 'CARDINAL', 'LAW', 'PERSON'] for ent in sent.ents):
            claims.append(sent.text.strip())
            
    return claims