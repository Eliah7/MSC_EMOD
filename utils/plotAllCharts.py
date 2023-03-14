#!/usr/bin/python

#import pymongo
import argparse
import matplotlib.pyplot as plt
import numpy as np
import json
import sys
import os
import pylab
from math import sqrt, ceil

#mc = pymongo.Connection("ingolstadt").test.things

def plotOneFromDisk():
    #random_sim = mc.find()[mc.find().count()-1]
    #ref_sim = open( "/tmp/ic.new_regress.1.old.json" )
    with open( sys.argv[1] ) as ref_sim:
        ref_data = json.loads( ref_sim.read() )

    num_chans = ref_data["Header"]["Channels"]
    #print( num_chans )
    idx = 0
    for chan_title in sorted(ref_data["Channels"]):
        #idx_x = idx%5
        #idx_y = int(idx/3)
        #print( str(idx_x) + "," + str(idx_y) )
        try:
            #subplot = plt.subplot2grid( (5,3), (idx_x,idx_y)  ) 
            subplot = plt.subplot( 4,5, idx  ) 
            subplot.plot( ref_data["Channels"][chan_title]["Data"], 'r-' )
            plt.title( chan_title )
        except Exception as ex:
            print( str(ex) + ", idx = " + str(idx) )
        if idx == 4*5:
            break

    plt.show()

def plotCompareFromMongo():
    #random_sim = mc.find()[mc.find().count()-1]
    random_sim = mc.find_one( { "sim.sim_id" : "2011_11_09_06_09_22_418000" } )
    icj_data = json.loads( random_sim["sim"]["inset_chart_data"] )

    with open( "regression.vectorgarki.reference.json" ) as handle:
        ref_sim = json.loads( handle.read() )
        ref_data = ref_sim["sim"]["inset_chart_data"]

    num_chans = ref_data["Header"]["Channels"]
    
    idx = 0
    for chan_title in sorted(ref_data["Channels"]):
        idx_x = idx%4
        idx_y = int(idx/4)
        #print( str(idx_x) + "," + str(idx_y) )
        try:
            subplot = plt.subplot2grid( (4,4), (idx_x,idx_y)  ) 
            subplot.plot( ref_data["Channels"][chan_title]["Data"], 'r-', icj_data["Channels"][chan_title]["Data"], 'b-' )
            plt.title( chan_title )
        except Exception as ex:
            print( str(ex) )
        if idx == 15:
            break

    plt.show()

def plotCompareFromDisk( reference, comparison, label = "" ):
    with open( reference ) as ref_sim:
        ref_data = json.loads( ref_sim.read() )

    with open( comparison ) as test_sim:
        test_data = json.loads( test_sim.read() )

    num_chans = ref_data["Header"]["Channels"]

    square_root = ceil(sqrt(num_chans))

    n_figures_x = square_root
    n_figures_y = ceil(float(num_chans)/float(square_root)) #Explicitly perform a float division here as integer division floors in Python 2.x

    if label == "unspecified":
        label = sys.argv[1]
    figure = plt.figure(label.split('/')[-1])   # label includes the full (relative) path to the scenario, take just the final directory
    #figure = plt.figure(label.split('/')[-1],figsize=(80,60))   # label includes the full (relative) path to the scenario, take just the final directory
    F = pylab.gcf()
    DefaultSize = F.get_size_inches()
    #F.set_size_inches( (DefaultSize[0]*3, DefaultSize[1]*2 ) )
    #Figure.set_figsize_inches( ( 120,80) )

    ref_tstep = 1
    if( "Simulation_Timestep" in ref_data["Header"] ):
        ref_tstep = ref_data["Header"]["Simulation_Timestep"]

    tst_tstep = 1
    if( "Simulation_Timestep" in test_data["Header"] ):
        tst_tstep = test_data["Header"]["Simulation_Timestep"]

    idx = 1
    for chan_title in sorted(ref_data["Channels"]):
        if chan_title not in test_data["Channels"]:
            print( "title on in test. ignore." )
            continue

        try:
            subplot = plt.subplot( n_figures_x, n_figures_y, idx ) 
            ref_x_len = len( ref_data["Channels"][chan_title]["Data"] )
            tst_x_len = len( test_data["Channels"][chan_title]["Data"] )
            ref_tstep = 1
            tst_tstep = 1
            if "Simulation_Timestep" in ref_data["Header"].keys():
                ref_tstep = ref_data["Header"]["Simulation_Timestep"]
                if "Simulation_Timestep" in test_data["Header"].keys():
                    tst_tstep = test_data["Header"]["Simulation_Timestep"]
            ref_x_data = np.arange( 0, ref_x_len*ref_tstep, ref_tstep )
            tst_x_data = np.arange( 0, tst_x_len*tst_tstep, tst_tstep )
            subplot.plot( ref_x_data, ref_data["Channels"][chan_title]["Data"], 'r-', tst_x_data, test_data["Channels"][chan_title]["Data"], 'b-' )
            plt.setp( subplot.get_xticklabels(), fontsize='5' )
            plt.title( chan_title, fontsize='6' )
            idx += 1
        except Exception as ex:
            print( "Exception: " + str(ex) )

    if reference==comparison:
        plt.suptitle( label + " " + reference)
    else:
        plt.suptitle( label + " reference(red)=" + reference + "  \n test(blue)=" + comparison )
    plt.subplots_adjust( bottom=0.05 )
    mng = plt.get_current_fig_manager()
    #mng.full_screen_toggle()
    #if os.name == "nt":
    #    mng.window.state('zoomed')
    #else:
        #mng.frame.Maximize(True)
    if "savefig" in sys.argv:
        path_dir = label.split( os.path.sep )[0]
        plotname = label.split( os.path.sep )[1]
        pylab.savefig( os.path.join( path_dir, plotname ) + ".png", bbox_inches='tight', orientation='landscape' ) #, dpi=200 )
    plt.show()

def plotBunchFromMongo():
    mysims = mc.find( { "parameters.ConfigName":"Polio Bihar Regression Test", "user":"jbloedow", "sim.status":"Finished", "parameters.Run_Number":{ "$gt":40 }} )
# calculate mean of first 10 and mean of second 10: later!
    all_data = []
    for sim in mysims: #[0:9]:
        icj_data = json.loads( sim["sim"]["inset_chart_data"] )
        all_data.append( icj_data )
    plotBunch( all_data )

def plotBunch( all_data, plot_name, baseline_data=None ):
    num_chans = all_data[0]["Header"]["Channels"]
    plt.suptitle( plot_name )
    square_root = 4
    if num_chans > 30:
        square_root = 6
    elif num_chans > 16:
        square_root = 5
    plots = []
    labels = []

    idx = 0
    for chan_title in sorted(all_data[0]["Channels"]):
        idx_x = idx%square_root
        idx_y = int(idx/square_root)

        try:
            subplot = plt.subplot2grid( (square_root,square_root), (idx_y,idx_x)  ) 
            colors = [ 'b', 'g', 'c', 'm', 'y', 'k' ]

            if baseline_data is not None:
                tstep = 1
                if( "Simulation_Timestep" in baseline_data["Header"] ):
                    tstep = baseline_data["Header"]["Simulation_Timestep"]
                x_len = len( baseline_data["Channels"][chan_title]["Data"] )
                x_data = np.arange( 0, x_len*tstep, tstep )
                plots.append( subplot.plot( x_data, baseline_data["Channels"][chan_title]["Data"], 'r-', linewidth=2 ) )

            for sim_idx in range(0,len(all_data)):
                labels.append(str(sim_idx))

                x_len = len( all_data[sim_idx]["Channels"][chan_title]["Data"] )

                tstep = 1
                if( "Simulation_Timestep" in all_data[sim_idx]["Header"] ):
                    tstep = all_data[sim_idx]["Header"]["Simulation_Timestep"]

                x_data = np.arange( 0, x_len*tstep, tstep )

                plots.append( subplot.plot( x_data, all_data[sim_idx]["Channels"][chan_title]["Data"], colors[sim_idx%len(colors)] + '-' ) )

            plt.title( chan_title )
        except Exception as ex:
            print( str(ex) )
        if idx == (square_root*square_root)-1:
            break

        idx += 1

    #plt.legend( plots, labels )

    #plt.set_size( 'xx-small' )
    plt.subplots_adjust( left=0.04, right=0.99, bottom=0.02, top =0.9, wspace=0.3, hspace=0.3 )
    pylab.savefig( plot_name.replace( " ", "_" ) + ".png", bbox_inches='tight', orientation='landscape' )
    plt.show()
    # print( "Exiting from plotBunch.\n" )

def main( reference, comparison, label ):
    #print( str( len( sys.argv ) ) )
    #plotOneFromDisk()

    plotCompareFromDisk( reference, comparison, label )
    #plotBunch()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('reference', help='Reference chart(s) filename')
    parser.add_argument('comparison', default=None, nargs='?', help='Comparison chart(s) filename')
    parser.add_argument('label', default='', nargs='?', help='Plot label')
    args = parser.parse_args()

    main(args.reference, args.comparison if args.comparison else args.reference, args.label)
