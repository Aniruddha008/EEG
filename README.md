## EEG

Here lies my various adventures when dealing with EEG data.

#create csv
Usually, saving eeg data into columns is a hassel, but with pandas writerow you could tweak it to write column by column so that your samples are properly alligned to the number of channels in a BCI/BMI device.

#basic ML for eeg data.
This is a basic template for eeg data in terms of classification which uses kernel svm, logestic regression, and random forest.
