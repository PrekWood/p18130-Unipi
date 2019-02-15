print("--RANDOM TEXT MAKER!--\n")


def text_splitter(text):
    #Making a list of each individual word,igoring the punctuation!
    words=[]
    word=''
    counter=1
    for i in range(len(text)):
        if text[i]!='.' and text[i]!=',' and text[i]!='?' and text[i]!='':
            if text[i]==' ' and i!=0:
                    words.append(word)
                    word=''
            else:
                word=word+text[i]

    #Making another list of these words divided in groups of three
    sentence=''
    sentences=[]
    i=0
    counter=0
    while (i<len(words)):
        if counter%3==0 and counter!=0:
            i=i-2
            sentences.append(sentence)
            sentence=''+words[i]+' '
        else:
            if (counter+1)%3==0:#Making sure that there's no space at the end of each sentence
                sentence=sentence+words[i]
            else:
                sentence=sentence+words[i]+' '
        i=i+1
        counter=counter+1

    #Returning that list
    return(sentences)

def text_maker(list,num):
    #printing the wanted number of words
    #Provided that the words are being kept in groups of 3 we should divide the wanted number by 3
    import random
    for i in range(num/3):
        r=random.randint(0,len(list)-1)
        print list[r],

f=open('exc11.txt','r')#Opening the file
x=f.read()
f.close()
print(x)
y=text_splitter(x)
print("\n->Please insert the number of words you want your random text to have.(the number must be divided by 3)")
z=input()
if type(z)==int:
    text_maker(y,z)
else:
    print("Wrong input!")
print("\n")
