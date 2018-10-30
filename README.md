A twitter bot that generates, renders and posts images of tile patterns in the style of NYC Subway tile art for non-existant stations.

A continuation from my [Fake MTA Subway Station](https://github.com/heavyimage/Fake-NYC-Subway-Stations) Generator bot.

Here's a roadmap the rendering pipeline:

* Generate names
    * Excecute name generation code in Blender or passin?
    * Choose representation based on multiple sign conventions (fort --> ft; boulevard --> blvd.etc)

* Decide some properties of the mosaiac
    * age of "station"
    * color scheme w/ variations
        * inherit from original station options?
        * 2 - 5 colors max but a "color" can have slight variantions in tiles of that color
* Build scene:
    * Create regionmap:
        * block but not also ---____---- sorta stuff
        * always mirrored on x, not nessisarily on y
        * inner most region must fit stationname
        * assign depth
        * ??? clip corners of regionmap or join with others?
        * Add tiny accent regions that are diamons or other shapes
    * Create tiles within each region
        * rules:
            * outer tiles are either  4 3/8" x 4 3/8" or 6x3 (NOT ALWAYS WHITE but OFTEN)
            * each inner tile region has an integer scale on tiles
            * white text, white walls
            * each tile should draw it's own grout
            * clip tiles to region
        * options:
            * staggered tiles
    * Color tiles:
        * checkboard
        * random w/ differnt weights
        * solid colors
    * Add name of station:
        * cushing?
    * "render" scene (2d image, layering regions)
* Export tile positions
* Geo generation
    * varying depths?
    * roundess?
    * add materials to geo
        * colors
        * aged vs. shiny
    * missing / damaged tiles?
* Displace / warp geo
* Render
* Comp
    * lens distortion?
    * chromab
    * instagram-esque filters?
* Post on twitter

### Resources
* [Incredible NYC subway station tile resource](http://nytrainproject.com/)
* [NYC Subway font analysis](https://www.aiga.org/the-mostly-true-story-of-helvetica-and-the-new-york-city-subway)
* [Subway tile design resources](http://www.nysubwaymosaics.com/design.html)
* [Tile Shading](https://www.youtube.com/watch?v=NDIZvJyMj1o)
* [Procedural Tile Material](https://www.youtube.com/watch?v=PobPKHuX8pM)
* [Dead Easy Tiles](https://www.youtube.com/watch?v=H-quCLfoHbk)
* [Stations with show-stopping tile art](https://ny.curbed.com/maps/new-york-subway-tile-public-art)
