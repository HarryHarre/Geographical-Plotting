
# coding: utf-8

# In[1]:


import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True) 


# In[2]:


import pandas as pd


# In[3]:


df1 = pd.read_csv('2014_World_Power_Consumption')


# In[4]:


df1.head()


# In[35]:


data = dict(type = 'choropleth',
           locations = df1['Country'],
            colorscale = 'Viridis',
            reversescale = True,
            locationmode = 'country names',
           z = df1['Power Consumption KWH'],
           text = df1['Country'],
            colorbar = {'title':'Power Consumption KWH'}
           )


# In[36]:


layout = dict(title = '2014 World Power Consumption',
             geo = dict(showframe= False,
                       projection = {'type':'natural earth'}))


# In[37]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# In[18]:


df2 = pd.read_csv('2012_Election_Data')


# In[19]:


df2.head()


# In[44]:


data = dict(type = 'choropleth',
            colorscale='Viridis',
            reversescale=True,
           locations = df2['State Abv'],
           z = df2['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
           text = df2['State'],
            colorbar = {'title':'Voting-Age Population (VAP)'}
           )


# In[45]:


layout = dict(title='2012 Election Data',
             geo = dict(scope='usa',showlakes=True,lakecolor='rgb(85,173,240)'))


# In[46]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)

