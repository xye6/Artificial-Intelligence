READ ME
Work is done with python 3For four python files:
1) Run them in terminal;(python file.py)
2) Make sure that python files and XML files are under same folder;
3) Input format (the order is important, one sentence every time): for exact inference, type the name of file which has information about variables and probability, the query variable, names and values of evidence variables (examples are shown below). For approximate inference, type the name of file which has information about variables and probability, the sampling times, the query variable, names and values of evidence variables (examples are shown below). 
4) The program will show the probability distribution of the query variable given evidence variables and running time.
5) If there are is no more problem, type ¡°END¡± to exit.  Queries:
For Exact inference(exact-inference.py):

aima-alarm.xml B J true M true

aima-wet-grass.xml R S true



For approximate inference(three algorithms have same input format, rejection/likelihood/gibbs.py):

aima-alarm.xml 5000 B J true M true

aima-wet-grass.xml 1000 R S true


Parser part for dog-problem.xml is completed by java with the help of my teammate (Yanhao Ding), So in my report, the value of dog-problem.xml inference part is coming from my teammate

Notes: my program has no problem in reading aima-alarm and aima-wet-grass examples, but will have problem to read dog example, since its conditional probability table has no information about their parents¡¯ value (it just shows numbers without indicating what their parents¡¯ values are under that probability).I try to debug and fail to find out the error when I construct CPT in my dog-problem.xml parser for this specific format before the due.

I thinks the algorithms are most important in this homework. Thanks
