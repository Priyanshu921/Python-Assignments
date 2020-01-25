"""Batsmen={1:{'Type of Player':'Right Handed Batsmen','Name of Batsmen':'Sachin Tendulkar','Matches':900,'Runs':40000,'Average':51.00,'Highest Score':200},
         2:{'Type of Player':'Right Handed Batsmen','Name of Batsmen':'Rohit Sharma','Matches':251,'Runs':,'Average':48.00,'Highest Score':264},
         3:{'Type of Player':'Right Handed Batsmen','Name of Batsmen':'Mahendra Singh Dhoni','Matches':300,'Runs':7352,'Average':45.00,'Highest Score':183}}
for p_id,p_info in Batsmen.items():
    print("\nBatsmen Id:",p_id)
    for key in p_info:
        print(key+":",p_info[key])"""

import pandas as pd
squad={'Batsmen':{1:{'Type of Player':'Right Handed Batsmen','Name of Batsmen':'Sachin Tendulkar','Matches':900,'Runs':40000,'Average':51.00,'Highest Score':200},
         2:{'Type of Player':'Right Handed Batsmen','Name of Batsmen':'Rohit Sharma','Matches':251,'Runs':8010,'Average':48.00,'Highest Score':264},
         3:{'Type of Player':'Right Handed Batsmen','Name of Batsmen':'Virat Kohli','Matches':277,'Runs':10843,'Average':59.58,'Highest Score':183}}}
"""df=pd.DataFrame(squad['Batsmen'])
print(df)"""
print(squad['Batsmen'][3]['Runs'])
runs=[]
for i in range(1,4):
    runs.append([squad['Batsmen'][i]['Runs']])
print(max(runs))
print(squad['Batsmen'][(runs.index(max(runs)))+1]['Name of Batsmen'])
