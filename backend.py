"""
                <div class="col-lg-4 col-md-6 col-sm-6 mix ecommerce">
                    <br>
                    <div class="portfolio__item">
                        <div class="portfolio__item__video set-bg">
                            <iframe src="https://open.spotify.com/embed/track/229S6OjNPcJs7Xast1Lioy" width="240" height="304" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
                        </div>
                        <br>
                        <!--
                        <div class="portfolio__item__video set-bg" data-setbg="img/portfolio/portfolio-1.jpg">
                            <a href="https://www.youtube.com/watch?v=LXb3EKWsInQ" class="play-btn video-popup"><i
                                    class="fa fa-play"></i></a>
                        </div>
                        -->
                        <div class="portfolio__item__text">
                            <h4>Name of Song by someone</h4>
                            <ul>
                                <li>by this guy</li>
                                <li>and this guy</li>
                            </ul>
                            <ul>
                                <li>pop</li>
                                <li>rap</li>
                            </ul>
                        </div>
                    </div>
                </div>
"""

"""
<iframe src="https://open.spotify.com/embed/track/229S6OjNPcJs7Xast1Lioy" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
"""

"""
"""
# embed link
# name of song
# by who
# genre
#import SpotipyBackend.main
data = [
    {"songLink": r"https://open.spotify.com/embed/track/229S6OjNPcJs7Xast1Lioy", "votes": 1, "name": "Player No More",
     "genre": "pop-rap", "artist": "Wassup Rocker", "who": "Danny"},
    {"songLink": r"https://open.spotify.com/embed/track/1B5jLmBZ9p9CTCT0fiBmIx", "votes": 1, "name": "1100",
     "genre": "pop-rap", "artist": "tuxx", "who": "Danny"},
    {"songLink": r"https://open.spotify.com/embed/track/2syCQpfGEttT4U2v8kVou7", "votes": 1, "name": "SoulEaters",
     "genre": "pop", "artist": "iceey.i, Lil Boom", "who": "Danny"}
]
#data += SpotipyBackend.main.a
def songsToHtml(data):
    inside = []
    for x in data:
        inside.append("<div class=\"col-lg-4 col-md-6 col-sm-6 mix %s\">" % x["genre"])
        s = """
        <br>
        <div class="portfolio__item">
        <div class="portfolio__item__video set-bg">
        """
        inside += s.splitlines()
        link = x["songLink"]

        w = "240"
        h = "304"
        inside.append(
            "<iframe src=\"%s\" width=\"%s\" height=\"%s\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>" % (
            link, w, h))
        inside.append("</div>")
        inside.append("<br>")
        inside.append("<div class=\"portfolio__item__text\">")

        songName = x["name"]
        inside.append("<h4>" + songName + "</h4>")

        author = x["author"]
        inside.append("<ul><li>" + author + "</li></ul>")

        genre = x["genre"]
        inside.append("<ul><li>" + genre + "</li></ul>")

        try:
            votes = x["votes"]
        except:
            votes = 0
        #inside.append("votes: "+str(votes))
        inside.append("<ul><li>" + "votes: "+str(votes) + "</li></ul>")
        inside.append("""
        <div class="wrap">
        <!-- <div class="votes">138</div> -->
        <div class="button"><i class="fa fa-arrow-up"></i>Vote this up now</div>
        </div>
        """)
        #inside.append("<button class=\"button button1\">Green</button>")
        inside.append("</div></div></div>\n\n\n")
    inside.append("""<style>
.button {
  background-color: black; /* Green */
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}


.button {
  background-color: blacck; 
  color: white; 
  border: 0px solid #f44336;
}

.button:hover {
  background-color: #f44336;
  color: black;
}


}
</style>""")
    return inside

"""

reload songs and add code to html
"""
def reloadSongs(data, genres):
    lines = []
    with open('templates/discoverTemplate.html') as f:
        for x in f.readlines():
            lines += x
            if "<!-- backend: songs -->" in x:
                lines += songsToHtml(data)

            elif "<!-- backend: genres -->" in x:
                for key, value in genres.items():
                    lines += "<li data-filter=\"."+key+"\">"+value+"</li>"


    open('templates/discover.html', 'w').close()

    with open("templates/discover.html", "w") as f:
        f.writelines(lines)
    f.close()



"""

reload songs and add code to html
"""
def editSuggestForm1(userid, vars):
    lines = []
    with open('templates/suggestFormTemplate.html') as f:
        for x in f.readlines():
            lines += x
            if "<!-- backend: suggestForm1 -->" in x:
                for x in vars.suggestForm[userid]["searchResults"]:
                    lines += "<li>"+x['name']+" - by "+x["author"]+"</li>"

    open('templates/suggestForm.html', 'w').close()

    with open("templates/suggestForm.html", "w") as f:
        f.writelines(lines)
    f.close()


"""

reload songs and add code to html
"""
def editSuggestForm2(userid, vars):
    lines = []
    with open('templates/suggestForm2Template.html') as f:
        for x in f.readlines():
            lines += x
            if "<!-- backend: suggestForm2 -->" in x:
                #for x in vars.suggestForm[userid]:
                #    lines += "<li>"+x['name']+" - by "+x["artist"]+"</li>"
                for key,value in vars.genres.items():
                    lines += "<li>"+value+"</li>"
                    #chosenSong = x[]
                    #lines += "<li>"+x['name']+" - by "+x["artist"]+"</li>"
            if "<!-- backend: suggestForm2Embed -->" in x:
                chosenSong = vars.suggestForm[userid]["chosenSong"]
                for x in vars.suggestForm[userid]["searchResults"]:
                    if x["name"]+" - "+x["author"] == chosenSong:
                        w = "240"
                        h = "304"
                        link = x["songLink"]
                        lines.append(
                            "<iframe src=\"%s\" width=\"%s\" height=\"%s\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>" % (
                        link, w, h))


    open('templates/suggestForm2.html', 'w').close()

    with open("templates/suggestForm2.html", "w") as f:
        f.writelines(lines)
    f.close()

genres = {"pop": "Pop", "pop-rap": "Pop Rap", "lo-fi": "Lo-fi", "metal": "Metal", "world": "World"}
"""
<li data-filter=".branding">Branding</li>
<li data-filter=".digital-marketing">Digital marketing</li>
<li data-filter=".web">Web</li>
<li data-filter=".photography">Photography</li>
<li data-filter=" .ecommerce">eCommerce</li>
"""
#def reloadGenres(genres):



#reloadSongs(data, genres)
