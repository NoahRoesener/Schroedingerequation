.. schroedinger documentation master file, created by
   sphinx-quickstart on Sun Sep 16 10:25:05 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2

####################
Schroedingerequation
####################

************
Introduction
************

This program solves the onedimensional schroedingerequation with given values from the input file
*schroedinger.inp*. The input file includes given potentials, coordinates, the interpolation type, minimal
and maximal coordinate values, specifications for the eigenvalues and the mass of the object. The program
inclues the solver, which can be started from the main modul and the plotter, which plots the calculated values
which are saved in files afterwards.


****************
Input and Output
****************

The program looks for the inputfile *schroedinger.inp*. If it is not there the program asks for the path of it.
The inputfile has to have this syntax.

::

	4.0           # Mass
	-5.0 5.0 1999 # xMin xMax nPoint
	1 5           # first and last eigenvalue to include in the output
	polynomial    # interpolation type
	3             # # nr. of interpolation points and xy declarations
	-1.0 0.5
	0.0 0.0
	1.0 0.5


The calculations of the solver module are saved in files with this syntax. Afterwards the files are used in the plot-modul to plot it.

* *potential.dat*

  interpolated potential in XY-Format:

  ::

     x1 V(x1)
     x2 V(x2)
     :    :

* *energies.dat*

  calculated eigenvalues

  ::

     E1
     E2
     E3
     : 

* *wavefuncs.dat*

  calculated wavefunctions in NXY-Format

  ::

     x1 wf1(x1) wf2(x1) wf3(x1) ...
     x2 wf1(x2) wf2(x2) wf3(x2) ...
     :

* *expvalues.dat*

  expectation values and standard deviation

  ::

     exp_1 qexp_1
     exp_2 qexp_2
     :   

****************
Starting Options
****************
Implemented starting options for the main modul and the plot modul

-------------------
Optional Parameters
-------------------

* directory: -d [path]

  Used to specify the path of the input file *schroedinger.inp*

* scale: -s [float]

  Scales the wavefunctions.

*******
Modules
*******
--------------
main.py
--------------
Main module which, when started calculates the values and saves them in files.

-----------------
datainput.py
-----------------
.. automodule:: datainput
   :members:

---------------------
solver.py
---------------------
.. automodule:: solver
   :members:

------------------------
plot.py
------------------------
.. automodule:: plot
   :members:

--------------------------
inputtests.py
--------------------------
.. automodule:: inputtests
   :members:

