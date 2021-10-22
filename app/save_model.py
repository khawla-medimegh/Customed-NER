# saving the model 
import pickle
import spacy
def load_model(model_path):
    ''' Loads a pre-trained model for prediction on new test sentences
   
    model_path : directory of model saved by spacy.to_disk
    '''
    #nlp = spacy.load("fr_core_news_md")
    nlp = spacy.blank('fr')
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    ner = nlp.from_disk(model_path)
    return ner

ner = load_model("C://Users//khawl//Desktop//final work//spacy_trainedModel")

pickle_out = open("classifier.pkl", mode = "wb") 
pickle.dump(ner, pickle_out) 
pickle_out.close()