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
#embed link
#name of song
#by who
#genre

data = [
    {"songid":r"https://open.spotify.com/embed/track/229S6OjNPcJs7Xast1Lioy", "votes": 1, "name":"Player No More", "genre": "rap pop", "artist":"Wassup Rocker", "who":"Danny"},
    {"songid":r"https://open.spotify.com/embed/track/1B5jLmBZ9p9CTCT0fiBmIx", "votes": 1, "name": "1100", "genre" : "rap pop", "artist" : "tuxx", "who" : "Danny"}
]


def dataToHtml(data):
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
        inside.append("<iframe src=\"%s\" width=\"%s\" height=\"%s\" frameborder=\"0\" allowtransparency=\"true\" allow=\"encrypted-media\"></iframe>" % (link, w, h))
        inside.append("</div>")
        inside.append("<br>")
        inside.append("<div class=\"portfolio__item__text\">")

        songName = x["name"]
        inside.append("<h4>"+songName+"</h4>")

        artist = x["artist"]
        inside.append("<ul><li>"+artist+"</li></ul>")

        genre = x["genre"]
        inside.append("<ul><li>"+genre+"</li></ul></div></div></div>\n\n\n")
    return inside

lines = []
with open('templates/discoverTemplate.html') as f:
    for x in f.readlines():
        lines += x
        if "<!-- backend: songs -->" in x:
            lines += dataToHtml(data)


open('templates/discover.html', 'w').close()

with open("templates/discover.html", "w") as f:
    table_foot = f.writelines(lines)
