# ARC_shiny

This repository is a pilot project exploring Python shiny for visualization of malaria case counts for a selected district in Loreto Peru alongside hydrometeorological (HM) data, where a lag can be set in terms of weeks between HM data and case counts. 

This is a work in progress.

## Notes on getting the shiny page working

Source: https://pypi.org/project/shinylive/

* Install `shinylive` in the Conda environment
  * Note: has to be done using `pip` as there is no Conda package  
    `pip install shinylive`
* Create a folder to hold the Shiny app and data files, e.g. `myapp`
* Create the `app.py` in the folder created above
* From the Conda command prompt:
  * Navigate to the project root folder
  * Publish the `app.py` Shiny app to the `docs` folder  
    `shinylive export myapp docs`
* Check the app:  
  `python -m http.server --directory site --bind localhost 8008`
* If all good, publish the app as a GitHub page