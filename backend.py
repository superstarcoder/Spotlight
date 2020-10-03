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
from SpotipyBackend.test import songs
data = [
    {"songid": r"https://open.spotify.com/embed/track/229S6OjNPcJs7Xast1Lioy", "votes": 1, "name": "Player No More",
     "genre": "pop-rap", "artist": "Wassup Rocker", "who": "Danny"},
    {"songid": r"https://open.spotify.com/embed/track/1B5jLmBZ9p9CTCT0fiBmIx", "votes": 1, "name": "1100",
     "genre": "pop-rap", "artist": "tuxx", "who": "Danny"},
    {"songid": r"https://open.spotify.com/embed/track/2syCQpfGEttT4U2v8kVou7", "votes": 1, "name": "SoulEaters",
     "genre": "pop", "artist": "iceey.i, Lil Boom", "who": "Danny"}
]
data += songs()

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
        link = x["songid"]
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

        artist = x["artist"]
        inside.append("<ul><li>" + artist + "</li></ul>")

        genre = x["genre"]
        inside.append("<ul><li>" + genre + "</li></ul></div></div></div>\n\n\n")
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


genres = {"pop": "Pop", "pop-rap": "Pop Rap", "lo-fi": "Lo-fi", "metal": "Metal", "world": "World"}
"""
<li data-filter=".branding">Branding</li>
<li data-filter=".digital-marketing">Digital marketing</li>
<li data-filter=".web">Web</li>
<li data-filter=".photography">Photography</li>
<li data-filter=" .ecommerce">eCommerce</li>
"""
#def reloadGenres(genres):



reloadSongs(data, genres)
