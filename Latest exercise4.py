# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置字体为SimHei（黑体），需确保系统中已安装此字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

imdb_df = pd.read_csv("imdb_top250.csv")
douban_df = pd.read_csv("douban_top250.csv")

# 简单查看数据
print("IMDb数据预览:")
print(imdb_df.head())
print("Douban数据预览:")
print(douban_df.head())

# 1. 比较平均评分
mean_imdb_rating = imdb_df['rating'].mean()
mean_douban_rating = douban_df['rating'].mean()

plt.figure(figsize=(6,4))
sns.barplot(x=['IMDb','Douban'], y=[mean_imdb_rating, mean_douban_rating])
plt.title('Average Ratings Comparison')
plt.ylabel('Average Rating')
plt.show()

# 2. 找到同时出现在两个榜单中的电影

common_movies = pd.merge(imdb_df, douban_df, on='title', suffixes=('_imdb','_douban'))
print("Number of movies in both lists:", len(common_movies))

# 可视化两个平台对这些共同电影的评分差异（散点图）
plt.figure(figsize=(6,6))
sns.scatterplot(data=common_movies, x='rating_imdb', y='rating_douban')
plt.title('Rating Comparison for Common Movies')
plt.xlabel('IMDb Rating')
plt.ylabel('Douban Rating')
plt.show()

# 分析共同电影的评分分布
# 我们可以对共同出现的电影的评分做一个对比箱线图或小提琴图
plt.figure(figsize=(8,4))
sns.boxplot(data=common_movies[['rating_imdb','rating_douban']])
plt.title('Boxplot of Ratings for Common Movies')
plt.xticks([0,1], ['IMDb','Douban'])
plt.ylabel('Rating')
plt.show()

# 3. 分析评价人数与评分之间的关系（对IMDb、Douban分别来一张散点图）
plt.figure(figsize=(8,4))
sns.scatterplot(data=imdb_df, x='vote', y='rating')
plt.title('IMDb: Rating vs Number of Votes')
plt.xlabel('Number of Votes')
plt.ylabel('Rating')
plt.show()

plt.figure(figsize=(8,4))
sns.scatterplot(data=douban_df, x='vote', y='rating')
plt.title('Douban: Rating vs Number of Votes')
plt.xlabel('Number of Votes')
plt.ylabel('Rating')
plt.show()

# 如果需要查看最高评分电影
top10_imdb = imdb_df.nlargest(10, 'rating').sort_values('rating', ascending=True)
plt.figure(figsize=(8,4))
sns.barplot(x='rating', y='title', data=top10_imdb, orient='h')
plt.title("IMDb Top 10 Highest Rated Movies")
plt.xlabel("Rating")
plt.ylabel("Movie Title")
plt.show()

top10_douban = douban_df.nlargest(10, 'rating').sort_values('rating', ascending=True)
plt.figure(figsize=(8,4))
sns.barplot(x='rating', y='title', data=top10_douban, orient='h')
plt.title("Douban Top 10 Highest Rated Movies")
plt.xlabel("Rating")
plt.ylabel("Movie Title")
plt.show()
