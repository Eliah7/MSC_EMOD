import os
import json
import matplotlib.pyplot as plt

# open and parse InsetChart.json
ic_json = json.loads( open( os.path.join(  "../output", "InsetChart.json" ) ).read() )
ic_json_allchannels = ic_json["Channels"]
ic_json_birthdata = ic_json["Channels"]["Births"]

ic_json_death_data = ic_json["Channels"]["Disease Deaths"]
ic_json_cmp_cost_data = ic_json["Channels"]["Campaign Cost"]

fig, axs = plt.subplots(3, 1)
# plot "Births" channel by time step
axs[0].plot( ic_json_birthdata[  "Data"  ], 'b-' )
axs[0].set_title( "Births" )

axs[1].plot( ic_json_death_data[  "Data"  ], 'b-' )
axs[1].set_title( "Deaths" )

axs[2].plot( ic_json_cmp_cost_data[  "Data"  ], 'b-' )
axs[2].set_title( "Costs" )

plt.show()