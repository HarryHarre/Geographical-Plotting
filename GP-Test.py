
# coding: utf-8

# In[43]:


import plotly.plotly as py
import plotly.graph_objs as go


# In[44]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[45]:


init_notebook_mode(connected=True)


# In[46]:


data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
           colorscale = 'Jet',
           text = ['Arizona','Cali','New York'],
           z = [1.0,2.0,3.0],
           colorbar = {'title':'Colorbar Title Goes Here'})


# In[47]:


layout = dict(geo={'scope':'usa'})


# In[48]:


choromap = go.Figure(data = [data],layout=layout)


# In[49]:


iplot(choromap)


# In[50]:


import pandas as pd
df = pd.read_csv('2011_US_AGRI_Exports')


# In[51]:


df.head()


# In[52]:


data = dict(type='choropleth',
           colorscale = 'YlOrRd',
           locations = df['code'],
           locationmode = 'USA-states',
           z = df['total exports'],
           text = df['text'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width=2)),
            colorbar = {'title':'Millions USD'}
           )


# In[53]:


layout = dict(title = '2011 US Agriculture Exports by State',
             geo = dict(scope='usa',showlakes = True,lakecolor='rgb(85,173,240)'))


# In[54]:


layout


# In[55]:


choromap2 = go.Figure(data = [data],layout=layout)


# In[56]:


iplot(choromap2)


# In[57]:


df = pd.read_csv('2014_World_GDP')


# In[58]:


df.head()


# In[59]:


data = dict(type = 'choropleth',
           locations = df['CODE'],
           z = df['GDP (BILLIONS)'],
           text = df['COUNTRY'],
            colorbar = {'title':'GDP in Billions USD'}
           )


# In[72]:


layout = dict(title = '2014 GLOBAL GDP',
             geo = dict(showframe= False,
                       projection = {'type':'natural earth'}))


# In[73]:


choromap3 = go.Figure(data=[data],layout=layout)


# In[74]:


iplot(choromap3)

