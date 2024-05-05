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
<h1>Start hadoop services </h1>
<p>1. start-all.sh
</p>
