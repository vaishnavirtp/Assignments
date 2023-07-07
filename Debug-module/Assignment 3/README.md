## Working with Environments, PyPI and Pip


<li>
Setting up an virtual environment allows the program to work in isolation.We can install the packages as per the requirement of the project and they will be available in that particular virtual environment.We can configure different environments for different project settings. This gives us the freedom of customization as per the needs.
</li>

<li>Steps to install virtual environment on Conda

<br/>
<ol>
<li>Install Anaconda and Anaconda Navigator on your OS</li>
<li>The default environment is base, we can create new using terminal or on GUI.</li>
<li>For GUI simply click on the environments tab on Anaconda Navigator and click on create. We can see the list of environments created and the package it contains.</li>

<li>
For terminal use
<br/>
conda create --envname 
</li>

<li>
The environment can be activated using 
<br/>
conda activate envname

</li>
</ol>
</li>


<li>
Pip is a python package installer.
Pip already exists with the latest python versions, but we can also install it manually.
</li>

<li>
Pip uses PyPI( Python Package Index ) which is a repository for all the python packages.
</li>

<li>
We can install almost any python package using simple pip command.
<br/>
For example:pip install Django==4.2.3
</li>
<li>

For using the python package requests, which is used for handling the API calls and data tranfers use:
<br/>

pip install requests
</li>

