#!/usr/bin/env python
# coding: utf-8

# # EVA Interactive Example

# In[1]:


from eva.data.eva_interactive import EvaInteractive


# ### Load data collections for AMSU-A and Aircraft

# In[2]:


amsua_file = '${data_input_path}/ioda_obs_space.amsua_n19.hofx.2020-12-14T210000Z.nc4'
aircraft_file = '${data_input_path}/ioda_obs_space.aircraft.hofx.2020-12-14T210000Z.nc4'


# In[3]:


eva_amsua = EvaInteractive()
eva_aircraft = EvaInteractive()


# In[4]:


dc_amsua = eva_amsua.load_ioda(amsua_file)


# In[5]:


dc_aircraft = eva_aircraft.load_ioda(aircraft_file)


# ### Arithmetic demonstration with AMSU-A

# In[6]:


eva_amsua.arithmetic(new_name='ObsValueMinusGsiHofXBc', expression='ObsValue-GsiHofXBc')


# In[7]:


eva_amsua.arithmetic(new_name='ObsValueMinusHofX', expression='ObsValue-hofx')


# In[8]:


eva_amsua.scatter('ObsValueMinusGsiHofXBc::brightnessTemperature', 
                  'ObsValueMinusHofX::brightnessTemperature')


# ### Accept where demonstration with Aircraft

# In[9]:


eva_aircraft.accept_where(new_name='EffectiveErrorPassedQc', 
                          starting_field='EffectiveError',
                          where = ['EffectiveQC == 0'])


# In[10]:


eva_aircraft.accept_where(new_name='GsiFinalObsErrorPassedQc',
                          starting_field = 'GsiFinalObsError',
                          where = ['GsiEffectiveQC == 0'])


# In[11]:


eva_aircraft.scatter('GsiFinalObsErrorPassedQc::airTemperature', 
                     'EffectiveErrorPassedQc::airTemperature')

