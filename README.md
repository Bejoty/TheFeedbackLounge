# The Feedback Lounge (mic.sexy)

This website is built for use by Zach Lobertini (aka "[Mic_Feedback](http://www.twitch.tv/mic_feedback)") for use as a [Twitch.tv](http://www.twitch.tv/) community hub. It features live broadcast data and other viewer resources, using responsive design practices for maximum accessibility.

### NOTICE:

This project is being retooled from the ground up due to client requests and knowledge gained since its conception, including best practices learned from the book [*Two Scoops of Django*](http://twoscoopspress.org/).

This transition is scheduled for Summer 2016, and will deploy via the URL: [mic.sexy](http://mic.sexy).

To see a current snapshot of development, please visit: [sexymic.bejoty.com](http://sexymic.bejoty.com).

### Back-end

* [Django 1.9.6](https://www.djangoproject.com/) Web framework
* [Twitch.tv API v3](https://github.com/justintv/Twitch-API) RESTful integration
* [Zinnia](http://django-blog-zinnia.com/) Weblog application

### Front-end

* [Bootstrap](http://getbootstrap.com/) front-end framework
* Responsive design for multiple platforms
* Components: collapse, glyphicon, modal, navbar
* Custom JavaScript and CSS

### Dependencies

The following Python packages should be installed prior to first migration:

```
Pillow
django-mptt
django-tagging
beautifulsoup4
mots-vides
django-contrib-comments
django-blog-zinnia
zinnia-wysiwyg-wymeditor
```

Each package may be installed via:

```
$ pip install [package-name]
```
