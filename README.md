<h1>
programs for convener screening 
</h1>
<----------
>
<p>
made for convener screening of WnCC, IIT Bombay<br/>
The sraping one was just out of fun<br/>
apparently azlyrics is not that bot friendly and stops responding if rate of requests crosses some limit<br/><br/>
</p>
<h2> Subtitle generator </h2><br/><br/>
<h3> run.py </h3><br/>
<pre>
    the python script to which arguments must be passed to initiate the Subtitle generator
    Ex : > python run.py  "Sherlock - 3x02 - The Sign of Three.srt"
    **NOTE** : this works only if the Indexing of the subtitles is proper, that is 1,2,3...


</pre>
<h3> run_threading.py </h3><br/>
<pre>
    this python script has the same usage as *run.py* but the implementation is different, 
    based on python threading library.
    not personally preffered by me as launching independent threads just to look at the time 
    is unwise.Nevertheless, it makes the code more structed, as a tradeoff for performance
    Ex : > python run_threading.py  "Sherlock - 3x02 - The Sign of Three.srt"


</pre>

<h2> Artist Strong Language check </h2><br/><br/>
<h3> core.py </h3><br/>
<pre>
    **Men at Work**
    works for only one artist uses threads to improve speed.
    but azlyrics catches it. 
    core_sync.py is its synchronous version
    And Believe me its wayyyyyy too slow
    second one works in reasonable time

    Ex : > python core.py eminem jerk
         > python core_sync.py "priyanka chopra" "in"

    **NOTE :** this has no way of handling a non 200 response code so it just adds 0 in its place
    so it is more like sampling of the limited set while core_sync gives the accurae figure
    **IT IS CASE INSENSITIVE** 

</pre>