from spacy import displacy
import spacy
import pickle
import builtins
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache(hash_funcs={spacy.tokens.doc.Doc: lambda _: None, builtins.tuple: lambda _: None})
# defining the function which will make the extraction using the data which the user inputs 
def extract(text):
    doc = classifier(text)
    return(doc)

# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:grey;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Custom NER App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""  
    # following lines create boxes in which user can enter data required to make prediction 
    
    docx_file = st.file_uploader("Upload File",type=['txt'])
    if docx_file is not None:
        #file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
        #st.write(file_details)
        raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for futher processing
        st.write(raw_text) # works

     #message = st.text_area("Enter Text","Type Here ..")
     # when 'Extract' is clicked, make the extraction and store it

  
    if st.button("Extract"):
          doc = extract(str(raw_text)) 
          html = displacy.render(doc, style="ent")
          html = html.replace("\n", " ")
          st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)      

     
if __name__=='__main__': 
    main()