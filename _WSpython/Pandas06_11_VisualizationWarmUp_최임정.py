
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
df=pd.read_csv('../data/gapminder.tsv','\t')


# In[4]:


global_yearly_life_expectancy=df.groupby('year')['lifeExp'].mean()


# In[5]:


global_yearly_life_expectancy


# In[6]:


global_yearly_life_expectancy.plot()


# In[7]:


#global_yearly_life_expectancy.hist()

