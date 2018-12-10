# List of assumptions I am making

* we want all descriptions that contain and, not just the 200 text blurb. This means i filter before truncating the values, and the word " and " does not end up in the final blurb, it is still valid

* we only want the word " and " not word that contain and, such as ampersand.

* I used the modern python solution for handling requirements. I used a package to fill out a generic requirements.txt

