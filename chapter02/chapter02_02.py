'''
@author：KongWeiKun
@file: chapter02_02.py
@time: 18-2-8 上午9:12
@contact: 836242657@qq.com
'''
'''
20世纪90年代末到21世纪初MovieLens用户提供的电影评分数据
'''
import pandas as pd

unames = ['user_id','gender','age','occupation','zip']
users  = pd.read_table('./data/movielens/users.dat',sep='::',header=None,names=unames,engine='python')
rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('./data/movielens/ratings.dat',sep='::',header=None,names=rnames,engine='python')
mnames = ['movie_id','ttile','genres']
movies = pd.read_table('./data/movielens/movies.dat',sep='::',header=None,names=mnames,engine='python')
# print(users[:5])
# print(ratings[:5])
# print(movies[:5])
# print(ratings.info())#数据的信息
data = pd.merge(pd.merge(ratings,users),movies)
# print(data.info())
print(data[:5])
print(data.ix[0])
mean_ratings = data.pivot_table('rating',rows='title',cols='gender',aggfunc=
                               'mean')