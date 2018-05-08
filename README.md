---- Data Structures Final Project ----
--  Wikipedia Network Analysis Tool --

========================================

Team Memeber:

Nick Marcopoli (nmarcopo) 
Andy Shin (ashin1)
Austin Sura (asura)
Tina Wu (ywu6)

===============================================================

Contribution:

Nick and Andy mainly worked on the visualization part of the project: 
creating the graph and adding user-interaction features
Tina and Austin mainly worked on the python code that gets the weblinks
from each wikipedia page

Everyone contributed equally to the completion of this project.

================================================================

Video Demonstration:

https://www.youtube.com/watch?v=-WMY3JJ0s_I

================================================================

Execution of the programs:

To run the backend: ./wikiCrawler.py or ./wikiCrawler.py -h
To run the visualization: open the program in Jupyter Notebook

================================================================

Test Suite:

We made a test script (timememory.py) to benchmark the runtime and 
memory usage of varying #links and #layers. 
A sample of output is shown below:

Wikipedia Article URL: https://en.wikipedia.org/wiki/Fortnite
 
|   #LINKS    |   #LAYERS   |  Time Usage  | Memory Usage |
|-------------|-------------|------------- |------------- |
| 1           | 1           | 1.008846     | 36.476562    |
| 2           | 1           | 1.318799     | 38.101562    |
| 3           | 1           | 1.509769     | 38.398438    |
| 4           | 1           | 1.751732     | 40.304688    |
| 5           | 1           | 2.036690     | 42.351562    |
| 1           | 2           | 1.308800     | 38.660156    |
| 2           | 2           | 2.553611     | 48.914062    |
| 3           | 2           | 3.889408     | 52.621094    |
| 4           | 2           | 5.636142     | 54.152344    |
| 5           | 2           | 7.903798     | 54.449219    |
| 1           | 3           | 1.542764     | 40.953125    |
| 2           | 3           | 4.384332     | 54.925781    |
| 3           | 3           | 11.133306    | 60.109375    |
| 4           | 3           | 24.119331    | 61.691406    |
| 5           | 3           | 45.060150    | 76.214844    |
| 1           | 4           | 1.743734     | 42.371094    |
| 2           | 4           | 9.182603     | 63.675781    |
| 3           | 4           | 39.776951    | 66.445312    |
| 4           | 4           | 112.903831   | 72.882812    |
| 5           | 4           | 259.600525   | 107.906250   |
|-------------|-------------|--------------|--------------|

To run the test script: ./timememory.py

As mentioned in our video, it is not possible to test the output every time 
because wikipedia pages are constantly changing. Therefore, we manually tested 
the outputs by clicking into the web pages and seeing what links are the most 
relevant. 

Since we used python and did not manually allocate memories, we did not have a 
memory issue (we tested by running valgrind, but making a sperate script for that
did not seem necessary).
