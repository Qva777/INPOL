<h1>📍How to install: </h1>


<details><summary><h1>⬇Manual start:</h1></summary><br>
<h4>1 - Connect venv:</h4> 

```
python3 -m venv venv
```

<h4>2 - Activate it:</h4>
<p>For Windows</p>

``` 
.\venv\Scripts\activate
```

<p>For MacOS</p>

``` 
source venv/bin/activate 
```

<h4>3 - Install libraries:</h4>

```
pip install -r requirements.txt
```

<h4>4 - Create Your .env</h4>
In order to run the application, you need to set up a .env file with the following configuration:

Activate the telegram file and follow the link to read USER_ID
```
BOT_ID=...
USER_ID=...
USER_EMAIL=example@gmail.com
USER_PASSWORD=password
API_KEY=CAP....
```

<h4>5 - Run server:</h4>

```
python contacts_search_service.py
```

<h4>6 - If you get error:</h4>

<pre>if tuple(PIL__version__) < (6, 2, 1):
TypeError: '<' not supported between instances of 'str' and 'int</pre>

<a href="https://stackoverflow.com/questions/76361049/how-to-fix-typeerror-not-supported-between-instances-of-str-and-int-wh">solve</a>

<p>So you need to click into the reported error file. Replace this code:</p>
<pre class="lang-py s-code-block"><code class="hljs language-python"><span class="hljs-keyword">if</span> <span class="hljs-built_in">tuple</span>(PIL__version__) &lt; (<span class="hljs-number">6</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>):
</code></pre>
<p>with this code:</p>
<pre class="lang-py s-code-block"><code class="hljs language-python"><span class="hljs-keyword">if</span> <span class="hljs-built_in">tuple</span>(<span class="hljs-built_in">map</span>(<span class="hljs-built_in">int</span>, PIL__version__.split(<span class="hljs-string">"."</span>))) &lt; (<span class="hljs-number">6</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>):
</code></pre>

</details>