import pandas as pd
import nltk
import arabic_reshaper
import os

    
def nlp(text):
    

    file_path = os.path.join('main', 'data2.xlsx')
    excel_data = pd.read_excel(file_path)
    data = pd.DataFrame(excel_data, columns=['word_arabic', 'word_english',])
    x=data['word_arabic']
    y=data['word_english']
    


    test_str=nltk.word_tokenize(text)
    if test_str[len(test_str)-1] != ".":
        text=text + " ."

    #for the three words
    
    result=[]
    for i in range(1,len(test_str)-1):
        data=''.join(test_str[t+i-1]+" " for t in range(3))
        result.append(data)
        result.append(data.replace("ال",""))
    # print(result)
    
    
    if len(result)==1:
        for j in range(len(x)-1):
            r=str(x[j])+" "
            if r in str(result[0]) :
                text=text.replace(r,str(y[j]))
        
    for i in range(len(result)):
        for j in range(len(x)-1):
            r=str(x[j])+" "
            if r in str(result[i]) :
                text=text.replace(r,str(y[j]))
    
    #for the two words
    
    result=[]
    for i in range(1,len(test_str)-1):
        data=''.join(test_str[t+i-1]+" " for t in range(2))
        result.append(data)
        result.append(data.replace("ال",""))
    # print(result)
    
    if len(result)==1:
        for j in range(len(x)-1):
            r=str(x[j])+" "
            if r == str(result[0]) :
                text=text.replace(r,str(y[j]))
        
    for i in range(len(result)):
        for j in range(len(x)-1):
            r=str(x[j])
            if r ==str(result[i]) :
                text=text.replace(r,str(y[j])+" ")
    # print(text)
    
     #for the one words
    
    result=[]
    for i in range(len(test_str)):
        data=''.join(test_str[t+i-1]+" " for t in range(1))
        result.append(data)
        result.append(data.replace("ال",""))
    # print(result)
    
        
    for i in range(len(result)):
        for j in range(len(x)-1):
            r=str(x[j])+" " 
            if r == str(result[i]) or r+"ال " == str(result[i]):
                
                text=text.replace(r,str(y[j])+" ")
                
    text=arabic_reshaper.reshape(text)
    return(text)
    
    
test_str=""
# nlp(test_str)