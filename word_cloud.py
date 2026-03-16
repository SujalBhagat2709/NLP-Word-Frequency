from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "nlp nlp nlp ai machine learning deep learning language"

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()