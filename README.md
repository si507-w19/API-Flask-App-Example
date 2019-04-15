# API & Flask Example

A former SI 364 course homework assignment by Brendan Paul (@bdpaul99)

### The original task assigned (part 1 of 2)

See HW3_Part1 directory for results.

Edit the `SI364_HW3.py` file inside the `HW3Part1` directory to add routes to the basic Flask application that will match the templates in the `templates` subdirectory inside the `HW3Part1` folder.

When you are done, you should have the following four routes which render each of the corresponding templates with reasonable data:

* `http://localhost:5000/artistform` -> `artistform.html`
* `http://localhost:5000/artistinfo` -> `artist_info.html`
* `http://localhost:5000/artistlinks` -> `artist_links.html`
* `http://localhost:5000/specific/song/<artist_name>` -> `specific_artist.html`

Each of the templates should be rendered with actual data when those routes are reached when the Flask application runs. 

Check out the action on forms and end-locations of links in order to ensure that you send the correct data to templates and that the templates get the correct data!

You may edit the templates (only slightly, you may not edit their structure), but you should not need to do so in any significant way.

