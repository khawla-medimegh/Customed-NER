import builtins
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache(hash_funcs={builtins.tuple: lambda _: None})
# defining the function which will make the extraction using the data which the user inputs 
def extract(text):
    doc = classifier(text)
    ch=""
    for ent in doc.ents:
        ch= ch+ "\n" + str(ent.text) + " ===> " + str(ent.start_char) + " " + str(ent.end_char) + " " + str(ent.label_) + "\n" 
    return(ch)

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
        result = extract(str(raw_text))
        st.success('Named Entities are: \n {}'.format(result))
    
   

     
if __name__=='__main__': 
    main()