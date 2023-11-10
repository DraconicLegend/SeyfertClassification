# SeyfertClassification

This repository reflects the data and analysis that stems from a study that aims to classify Seyfert Type 1 (Sy1) and Seyfert Type 2 (Sy2) galaxies by differences other than the ratio of the strengths of their emission lines. It contains queries and the datasets that result from those queries. 

That said, we searched SIMBAD for Seyfert galaxies and found 43029 Seyferts. We obtained equatorial coordinates, distance, redshift, morphological type, and color magnitudes for each Seyfert. We solely used the Python programming language and its libraries for data analysis. 

##[Morphological Type](https://github.com/DraconicLegend/SeyfertClassification/tree/main/Morphology)
We searched SIMBAD's Seyferts and obtained 2 datasets with different morphological classifications: Hubble Tuning Fork and Hubble Stage T classifications. We used Pandas to clean the data and organize the Seyferts by morphological type. We used MatPlotLib to make bar graphs on the basis of morphology. Unfortunately, both sets of data were so imbalanced in terms of Seyfert type that we could not draw any significant conclusions about a relationship between Seyferts and morphology based on SIMBAD dataset alone, causing us to conclude this difference as insignificant.

##[Redshift](https://github.com/DraconicLegend/SeyfertClassification/tree/main/Redshift)
We used Pandas to organize, clean, and graph the data. To graph the data, we used MatPlotLib to graph boxplots of the Seyfert redshifts. The difference was signifcant enough that it enabled us to include redshift data in our model.

##[Spatial Distribution](https://github.com/DraconicLegend/SeyfertClassification/tree/main/Spacial%20Distribution)
We used Pandas to clean the data and MatPlotLib to graph the data on boxplots and create an Aitoff Projection . But to make the interactive 3-D plot, we used Plotly and Astropy in addition to all the mentioned libraries. The results were not significnat enoguh for spatial distrubiton in the model

##[Luminosity](https://github.com/DraconicLegend/SeyfertClassification/tree/main/Luminosity)
For Luminosity, we used Pandas to clean and organize the data and MatPlotLib to graph the data on a histogram. We concluded no significant difference in Luminosity.


##[Color-Magnitude](https://github.com/DraconicLegend/SeyfertClassification/tree/main/Color%20Magnitude)
The color-magnitude was analyzed in two methods: the construction of diagrams and statistics. In both cases, data cleaning was accomplished with Pandas. To graph the raw statistics of B-V values in boxplots and color magnitude diagrams, we used NumPy to obtain subsets of that data and MatPlotLib to graph such diagrams. We concluded a significant enough difference in Color Magnitude.

##[Machine Learning Model](https://github.com/DraconicLegend/SeyfertClassification/tree/main/ClassificationModel)
We used Pandas and NumPy to clean the data and split it in training and testing sets. To create the models, we used Scikit-Learn and MatPlotLib to create the Confusion Matrix.

