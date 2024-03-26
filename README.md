# Movie-Recommendation-System
Initially started as a mini-project, it was extended for my grad school final Project at UMass submitted April, 2018.


Title: 
Speed-Enhanced Recommender System based on Pareto Dominance Concept  

Technologies/Tools:
Python, pandas, matplotlib, numpy, Jupyter Notebook

The previous work(first commit) was extended to conduct research and analysis on extracting popular movies based on different metrics to extract dominant data objects (movies).

Abstract:
New content is being added exponentially every day and it would not be efficient to analyze the entire dataset at once, of users and/or items to make recommendations. There is a need to increase the speed of making recommendations by processing part of the data that is representative of a large dataset. With an implementation that uses the Pareto's principle, which is based on the observation that most of the results in any situation are determined by a small number of causes, we have tried to address analyzing data to make movie recommendations. The idea behind this is that most users largely consume small part of items in the dataset. The aim of this project is to find a set of non-dominated items and make recommendations based that small set of data and compare it with recommendations based on the entire dataset. The non-dominated items are based on features such as average rating, number of voters and genres.  Hence, initially, recommendations for a movie are obtained from 100% items of the dataset. Then those results are compared with recommendations from top 20% items in the dataset from each genre-pair. Time taken for both cases are also recorded to be compared. Also, the algorithm is applied to find items that have gained popularity among few voters which tells us that these items are new and rising in popularity.


This research points out a way to categorize a large dataset and narrows it down to a partial dataset that can be reliable to provide recommendations in less time with a few trade-offs. The use of pair-wise genres helps to get the pareto dominant items for each genre-pair. This makes sure that we're recommending the dominant items from every genre pair and not generalizing movies. This extraction is based on the Pareto Principle or Pareto Dominance concept from which we deduce that most users consume only part of the dataset which contains superior or most popular data items.

*Anyone interested to extend this research or request a more complete/finished code can contact me stating your research/goal and I'd happy to share by reserach pn this topic and related conclusions.

As part of my Data Mining course project in Spring 17 at UMass; I have implemented a recommender system that suggests movies to any user based on user ratings. The dataset used is MovieLens 100k dataset. The items(movies) are correlated to each other based on user ratings given to them by users in system.

Recommender System using Item-based Collaborative Filtering Method using Python. Used “Pandas” python library to load MovieLens dataset to recommend movies to users who liked similar movies using item-item similarity score.

Machine learning python libraries and others like pandas, numpy, matplotlib.pyplot, scipy, operator are required to run this program.

Repository contains 2 implementations. First file is a .py file and another is an IPython Notebook. The IPython notebook implementation gives step-by-step output of the application.

The dataset used is by GroupLens Research that has collected and made available rating data sets from
the MovieLens web site (http://movielens.org). The data sets were collected over various periods of time,
depending on the size of the set.

In this experiment we have used the MovieLens 100K Dataset. It is available at the website linked here:
https://grouplens.org/datasets/movielens/100k/

Reference(s):
1.	Pareto Principle: https://en.wikipedia.org/wiki/Pareto_principle; https://www.investopedia.com/terms/p/paretoprinciple.asp#ixzz57Es8gewo
2.	Characterization of Pareto dominance: https://www.sciencedirect.com/science/article/pii/S016763770200189X
3.	Recommendation System: https://en.wikipedia.org/wiki/Recommender_system
4.	Pazzani M ˊA framework for collaborative, content-based, and demographic filtering. Artificial Intelligence Review, 1999, 13(5-6): 393-408.
5.	Recommendation System Algorithms
https://blog.statsbot.co/recommendation-system-algorithms-ba67f39ac9a3
6.	G. Adomavicius and A. Tuzhilin, “Towards the next generation of recommender systems: a survey of the state-of-the-art and possible extensions,” IEEE Trans. on Data and Knowledge Engineering 17:6, pp. 734–749, 2005.
7.	The Pareto Envelope-based Selection Algorithm for Multi objective Optimization - https://pdfs.semanticscholar.org/9511/17b91bb0221dc2f513f82660be4b1739551e.pdf
8.	 A Fast Algorithm for Finding the Non Dominated Set in Multi objective Optimization K.K.Mishra and Sandeep Harit 2010 
9.	Jun Du, Zhihua Cai and Yunliang Chen,” A Sorting Based Algorithm for Finding NonDominated Set in Multi-Objective Optimization” Third International Conference on Natural Computation (ICNC 2007)
10.	K. Deb, S. Agrawal, A. Pratap, and T. Meyarivan. A fast elitist non-dominated sorting genetic algorithm for multi-objective optimization: NSGA-II. In Proceeding of the 6th International Conference on Parallel Problem Solving from Nature, Pages 849-858, 2000.  
11.	L. Ding. S.Zeng. and L. Kang, “A fast algorithm on finding the non-dominated set in multi-objective optimization.”, In Proceedings of International Conference on Evolutionary Computation, pages 2565-2571, 2003
12.	E. Zitzler, M. Laumanns, and L. Thiele,”Spea2: Improving the strength Pareto evolutionary algorithm for multiobjective optimization.”, In Proceedings of the Evolutionary Methods for Design, Optimization, and Control, 19-26, Barcelona, Spain, 2002. 
13.	 C. Anderson, The Long Tail: Why the Future of Business is Selling Less of More, Hyperion Books, New York, 2006.
14.	 Using pareto-optimality for solving multi-objective unequal area facility layout problem - https://dl.acm.org/citation.cfm?id=2001670
15.	Y. Koren, “The BellKor solution to the Netflix grand prize,” www.netflixprize.com/assets/GrandPrize2009 BPC BellKor.pdf 2009
16.	G. Linden, B. Smith, and J. York, “Amazon.com recommendations: item-to-item collaborative filtering,” Internet Computing 7:1, pp. 76–80, 2003
17.	M. Piotte and M. Chabbert, ”The Pragmatic Theory solution to the Netflix grand prize,” www.netflixprize.com/assets/ GrandPrize2009 BPC PragmaticTheory 2009
18.	A. Toscher, M. Jahrer, and R. Bell, “The BigChaos solution to the Netflix grand prize,” www.netflixprize.com/assets/GrandPrize2009 BPC BigChaos.pdf 2009. 
19.	Incorporating Contextual Information in Recommender Systems Using a Multidimensional Approach - http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.423.5495&rep=rep1&type=pdf
20.	A KNN Research Paper Classification Method Based on Shared Nearest Neighbor: https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/#what-is-knn

21.	B. Sarwar, G. Karypis, J. Konstan and John Riedl, “Item-Based Collaborative Filtering Recommendation Algorithms”, Proceedings o the 10th international conference on World Wide Web 2001: 285-295.
22.	Knn - https://medium.com/@adi.bronshtein/a-quick-introduction-to-k-nearest-neighbors-algorithm-62214cea29c7.
23.	 Andrew Ng, CS229 Lecture Notes.
24.	Methods for Boosting Recommender Systems http://www.cs.tau.ac.il/~boim/publications/icde11-phd-workshop.pdf
25.	kNN - https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
26.	Pareto Dominance-Based Algorithms With Ranking Methods for Many-Objective Optimization VIKAS PALAKONDA AND RAMMOHAN MALLIPEDDI 2017
27.	 K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, ‘‘A fast and elitist multiobjective genetic algorithm: NSGA-II,’’ IEEE Trans. Evol. Comput., vol. 6, no. 2, pp. 182–197, Apr. 2002.
28.	Q. Zhang and H. Li, ‘‘MOEA/D: A multiobjective evolutionary algorithm based on decomposition,’’ IEEE Trans. Evol. Comput., vol. 11, no. 6, pp. 712–731, Dec. 2007.
29.	P. J. Bentley and J. P. Wakefield, ‘‘Finding acceptable solutions in the Pareto-optimal range using multiobjective genetic algorithms,’’ in Soft Computing in Engineering Design and Manufacturing. Springer, 1998, pp. 231–240. 
30.	 D. W. Corne, N. R. Jerram, J. D. Knowles, and M. J. Oates, ‘‘PESA-II: Region-based selection in evolutionary multiobjective optimization,’’ in Proc. 3rd Annu. Conf. Genetic Evol. Comput., 2001, pp. 283–290.
31.	Weight Based KNN Recommender System: Bin Wang, Qing Liao, Chunhong Zhang Beijing Key Laboratory of Network System Architecture and Convergence 2013
32.	Cold start problem - http://www.yusp.com/blog/cold-start-problem-recommender-systems/
32a. Frank Kane, Sundog Education
33.	Hill W, Stead L, Rosenstein M, Furnas G. Recommending and evaluating choices in a virtual community of use. Proceedings of the CHI’95.1995,Pages 194~201.
34.	Sarwar B, Karypis G, Konstan J, Riedl J. Item-Based collaborative filtering recommendation algorithms. Proceedings of the 10th International World Wide Web Conference .2001, Pages 285~295.
35.	 Pazzani M ˊA framework for collaborative, content-based, and demographic filtering. Artificial Intelligence Review,1999, 13(5-6): 393-408.

