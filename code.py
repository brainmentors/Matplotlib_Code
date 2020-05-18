import matplotlib.pyplot as plt
import numpy as np

data = {
    'movie_name' : ['avengers','thor','black panther','hulk','ironman'],
    'rating' : [4.5,4.0,5.0,3.5,4.0],
    'earnings' : [120,142,200,95,192]
    }

# bar
# plt.bar(data['movie_name'], data['rating'], color='red')
#plt.barh(data['movie_name'], data['earnings'], color='red')

# pie chart
plt.pie(data['rating'],labels = data['movie_name'], shadow=True,
        autopct=('%1.2f%%'), explode=(0,0,0.3,0,0))
plt.legend()
plt.title('Marvels Rating')

plt.show()
