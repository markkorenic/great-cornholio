from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as pl
from PIL import Image
import numpy as npy


def load_beavis():
 
    #load data
    txt_input = open("cornholio.txt", "r").read()
   
    # Load image mask
    beavis_bk = npy.array(Image.open("beavismask.jpg"))
    
    #set wordcloud params
    wc = WordCloud(font_path ='beavis_font.ttf', background_color = 'black', 
                   mask = beavis_bk, width = 800, height = 600, max_words = 60, min_word_length = 3)
    

    # generate the word cloud
    
    wc.generate(txt_input) 
    
    
    # Create Frame
    fig = pl.figure()
    fig.set_figwidth(16)
    fig.set_figheight(20)     
    
    #plot image
    pl.imshow(wc.recolor(colormap = 'hsv'), interpolation = 'nearest')

    pl.axis("off")
    pl.show()  
    
load_beavis()
