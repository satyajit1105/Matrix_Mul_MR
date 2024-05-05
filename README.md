<h1>1.Create a folder named MM_Py in the home Directory.</h1>
<p>Add reducer.py, mapper.py, matrix1.txt, matrix2.txt to this folder</p>
<h1>2.Run the following cmds</h1>
<p>1.  cd MM_Py<br>
   2.  cat *.txt | python3 mapper.py  <br>
   3.  cat *.txt | python3 reducer.py <br>
   4.  cat *.txt | python3 mapper.py | python3 reducer.py <br></p>
<h1>3.Give necessary permissions to mapper.py and reducer.py.</h1>
<p>1. chmod 777 mapper.py reducer.py <br>
   2. ls -la </p>
<h1>4.Start hadoop services </h1>
<p>1. start-all.sh</p>
<h1>5.Create a directory named Mat_Py over hdfs and copy the input matrices into it.</h1>
<p> 1. hadoop fs -mkdir /Mat_Py<br>
    2. hadoop fs -copyFromLocal /home/satya1105/MM_Py/matrix1.txt /Mat_Py<br>
    3. hadoop fs -copyFromLocal /home/satya1105/MM_Py/matrix2.txt /Mat_Py</p>
<h1>6.Create a jar file[hadoop version specific]</h1>
<p>1. /home/satya1105/hadoop/bin/hadoop jar /home/satya1105/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar     -mapper "python3 /home/satya1105/MM_Py/mapper.py"     -reducer "python3 /home/satya1105/MM_Py/reducer.py"     -input /Mat_Py     -output /Mat_Py/out_mat/
 </p>
