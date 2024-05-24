### Welcome to PWS_AI
-------------------
This code is ready for a soft release. The user now has ability to input their analysis name as well as their thresholding value. Preview of results can be done via PWSPY software. For any questions or bug suggestions please slack me - Nico

#### Tutorial 
As it stands, you will go through 5 main steps. 

Step 0) Run analysis on dataset of interest, that means running it on the pws 
	 analysis software as is normally done

Step 1) Select folder with cell data where you just ran your analysis (same way its
	done on the pwspy software) 

Step 2) Access rms images from analysis. This is done automatically when you click
	the button "Get RMS Images" after entering the analysis name (e.g p0) 

Step 3) Use PWS_AI to generate the ROIs automatically and save them as TIF File in
        Corresponding Folder after entering the desired threshold value, default is 0.6

Step 4) Conver the PWS_AI output into the pwspy compatible format. Done by clicking 
	"Push ROI TO PWSPY" 


Once this is done you can go to the pws analysis software where you can now use the 
AI generated ROIs. This is a beta version and not ready for release but thank you for 
testing it out! 

#### Installation instructions
The gui is now available throuogh PyPi so you can install it as you would any python package. Please follow stepes below or see Guide folder for more guidance. The follownig steps assume you already have python on your machine, and you should if you do PWS analysis.  

1. Create a Python environment using `conda create --name desired_name_here python==3.8`
2. Once python environment has been created install pwsAI by `pip install pwsAI`

If this does not work, please reach out to me and I can send you further instructions on how to install directly from wheel file.

#### Building (For dev purpoes)
PIP can be used to build a "wheel" for distribution by navigating to the root directory (where "setup.py" is located) and running `python -m build`. The produced files will be placed into the "dist" folder. You can distribute the .whl file yourself and install using PIP or you can upload the .whl to the PyPi repository online for easy download access (`pip install pwsAI`). To upload to PyPi you will need "twine" (`pip install twine`) and you will need to configure twine with the proper credentials to log into your PyPi account. Then upload with `python -m twine upload ./dist/*`.

Once pwsAI has been installed you can run the GUI either by running `python -m pwsAI` or by using the `PwsAiGui` alias.