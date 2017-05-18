#Please change file pathname for u.data and u.item before running the demo
import pandas as panda

r_cols = ['user_id', 'movie_id', 'rating']
#Change path to run 
ratings = panda.read_csv('/home/akkhilaysh/Documents/Akkhi DS/DataMining/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))

m_cols = ['movie_id', 'title']
#Change path to run
movies = panda.read_csv('/home/akkhilaysh/Documents/Akkhi DS/DataMining/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2))

ratings = panda.merge(movies, ratings)

ratings.head(10)
#ratings.tail(10)

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()

corrMatrix = userRatings.corr()
corrMatrix.head()

corrMatrix = userRatings.corr(method='pearson', min_periods=50)
corrMatrix.head()

myRatings = userRatings.loc[0].dropna()
myRatings

simCandidates = panda.Series()
for i in range(0, len(myRatings.index)):
    print "adding sims for " + myRatings.index[i] + "..."
    sims = corrMatrix[myRatings.index[i]].dropna()
    sims = sims.map(lambda x: x * myRatings[i])
    simCandidates = simCandidates.append(sims)
    
print "sorting in decreasing order of similarity score: "
simCandidates.sort_values(inplace = True, ascending = False)
print simCandidates.head(10)

simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
print "\n"
print "---Adding up the similarity scores of duplicate values:---"
print simCandidates.head(10),

filteredSims = simCandidates.drop(myRatings.index, errors='ignore')
print "\n"
print "---Filtering the result to remove already rated movies:---"
print filteredSims.head()