estimation-at-the-extreme
=========================

Source code (Experiments_final.ipynb) and necessary files to reproduce the experimental results of the paper : **Estimating the Size and Average Degree of Online Social Networks at the Extreme**, which proposes network size and average degree estimators for online social networks under a limited data access model, which we call random neighbor access (RNA) model.

#####Requirements to run the source code (Experiments_final.ipynb)
---------------------
* python 2.7
* ipython (>= 2.0.0)
* networkx (>= 1.7)
* scipy (>= 0.13.3)
* numpy (>= 1.9.0)
* matplotlib (>= 1.3.1)
* pandas (>= 0.14.1)
* ipython-notebook

I suggest installing anaconda which is a completely free Python distribution. It includes 195+ of the most popular Python packages for science, math, engineering, data analysis.
Anaconda will install all required pacakages except ipython-notebook. You should install it seperately.

I assume that user has an experience on parallel computing with IPython as well as using ipython notebook. In order to run the source code the cluster should be up and ready; otherwise, you will get the following error "Ooops! Did you forget to start the cluster?".
For the tutorial on using IPython for parallel computing see [this](http://ipython.org/ipython-doc/dev/parallel).

###Sections of source code (Experiments_final.ipynb)
=========================
#####Estimating the Size and Average Degree of Online Social Networks at the Extreme
--------------
In this section, the abstract of the study is provided. It has nothing to do with the experimental sections; therefore, you do not need to run it.

###0.Initialize
-------------------------
This section is about the initialization of engines and local machine.

#####Initialize the Engines
----------------------
This cell prints out the process ids of engines in the cluster and more importantly imports the necessary libraries on engines. If you get an error on this cell, make sure that libraries are installed on the engines.

#####Load the required modules locally
--------------------------------
This cell imports the necessary libraries to be able to run the remaining cells successfully.

#####Set the plot properties
---------------------------
This cell sets the properties of the plots such as the fraction of the width you'd like the figure to occupy, inches per point, figure width and height in inches.     

#####Print progress for AsyncResult to stdout
---------------------------------------------
This cell has the necessary functions to print the progress of parallel experiments in a readable way.

#####Statistics of Real-world graphs
-------------------------------------
This cell prints the average, median, mode, and max degree of input graphs (given as a list of files in adjacency list format)

###1.Multiplicity based network size estimator
----------------------------------------------
This section is about the VCB (Vertex collusion based) and MB-VCB (Multiplicty-based vertex collusion) estimator.

#####MB-VCB (Multiplicty-based vertex collusion) estimator
----------------------------------------------------------
This cell implements the MB-VCB estimator and imports it on the engines. MB-VCB estimator is using vertex multiplicities as the vertex degree information is not available.

#####Monte carlo simulation for network size estimation
---------------------------------------------------------
This cell implements the function that performs a monte carlo simulation to estimate the network size. The function returns a list of dictionaries where a single dictionary keeps the parameters and the estimation of a single experiment.

#####Run the monte carlo simulation for network size estimation
----------------------------------------------------------------
This cell runs the experiments for network size estimation. You can play with the parameters of the experiments such as input graphs, values of margin parameters, number of simulations, and so on.

#####Plot the figures for network size estimations
--------------------------------------------------
This cell plots the results for network size estimation.

###2.Average degree estimator
----------------------------------------------
This section is about the GEN (generalized estimator) and GEN-AD(generalized estimator for average degree) estimator.

#####Monte carlo simulation for average degree estimation
---------------------------------------------------------
This cell implements the function that performs a monte carlo simulation to estimate the average degree. The function returns a list of dictionaries where a single dictionary keeps the parameters and the estimation of a single experiment.

#####Run the monte carlo simulation for average degree estimation
This cell runs the experiments for average degree estimation. You can play with the parameters of the experiments such as input graphs, values of m (it is \omega in the paper.), number of simulations, and so on.

#####Plot the figures for network size estimations
--------------------------------------------------
This cell plots the results for average degree estimation.

###3.Vertex degree estimation
---------------------------
This section is about the estimation of local vertex degrees.

#####Bar plot for degree estimation
-----------------------------------
This cell implements the functions for vertex degree estimation.

#####Run the experiment for vertex degree estimation
----------------------------------------------------
This cell runs the experiment for vertex degree estimations. Result is saved to a file named *bar_plot_degree_estimation.pickle*. 

#####Plot the figure for vertex degree estimation
-------------------------------------------------
This cell plots the figure for vertex degree estimation using the file generated in the previous cell.

#####Sample size required for a given precision and accuracy
------------------------------------------------------------
The next three cells implement the number of required sample size to get a given precision and accuracy in the estimation of a vertex degree.


