
==============================================================================
collective.sgvizler
==============================================================================

SGVizler is a library that can directly question SPARQL endpoint to visualize opendat in your site.
This intregration of version 0.6 use dexterity type to be flexible with parameters.

Due to time limitation for the exercise this package is not done in the Plone 5 way.

Enjoy.

Features
--------

- SGVizler 0.6
- Dexterity type to make the rendering

See the SGVizler documentation and screenshot below to see examples.


Examples
--------

This add-on can be seen in action at the following sites:

- http://dev.data2000.no/sgvizler/wiki/Sgvizler#Screenshots
- http://doc.data2000.no/sgvizler/0.6/classes/sgvizler.html


Documentation
-------------

TODO
#Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar

Proxy Configuration
===================

SGVizler does AJAX request between domains. You need to configure your front 
proxy to accept data from domains where are SPARQL endpoints, id est you need 
to add a *connect-src* provider in the *Content-Security-Policy* HTTP 
header.

Example with NGinx:

.. code:: nginx

    add_header X-Frame-Options "SAMEORIGIN";
    add_header Strict-Transport-Security "max-age=15768000; includeSubDomains";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options "nosniff";
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' 'unsafe-inline'; font-src 'self' 'unsafe-inline'; object-src 'self'; connect-src 'self' http://endpoint.example.com";



Translations
------------

This product has been translated into

- French (TODO)


Installation
------------

Install collective.sgvizler by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.sgvizler


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.sgvizler/issues
- Source Code: https://github.com/collective/collective.sgvizler
- Documentation: http://dev.data2000.no/sgvizler/wiki/Sgvizler/0.6/Using


Support
-------

If you are having issues, please let us know.
You can contact the owner (don't abuse please): Gerard.Vidal@ens-lyon.fr 


License
-------

This work was planned and done with the courtesy of the IFÉ - École Normale 
Supérieure de Lyon.

The project is licensed under the BSD.
