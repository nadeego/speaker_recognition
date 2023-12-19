### Development of an SVM Based Speaker Identification Model

**Nicholas O'Deegan**

### Executive summary
The primary goal of this capstone project is to develop a robust speaker identification system using a Support Vector Machine (SVM) model. The system aims to accurately identify individuals based on their unique voice characteristics captured in audio recordings.

### Rationale
Speaker identification technology has significant applications in various fields such as security systems, forensic analysis, and voice-controlled systems. With the advancement in machine learning and digital signal processing, it has become feasible to design systems that can identify speakers with high accuracy.

### Research Question
How effective is the Support Vector Machine (SVM) model in distinguishing unique voice characteristics for speaker identification?

### Data Sources
Four speakers were asked to record themselves speaking for 30 seconds in three different locations. These recordings were then split into 3, 2, 1, and half second segments. 

The SVM model was trained separately on the different segment intervals to determine what impact the recording length might have on model performance.

Key acoustic features were extracted from the segments, for example,  Mel Frequency Cepstral Coefficients (MFCCs), spectral contrast, pitch, bpm, zero-cross rate, etc. These features are known to help identify unique characteristics of a speaker's voice.

Given more time, more recordings would have been preferable to increase our data size. Cross Validation was employed to assist with the lack of data.

### Methodology
A Support Vector Machine was chosen given the high dimensionality of the data (70+ features), its ability to use the Kernel Trick to assist with non-linear classification and its focus on maximizing the margin between different classes, which is aligned with our desire to produce a robust classification system.

A Logistic Regression model was also trained for comparison.

### Results
The best model received an accuracy score of ~0.852.

**Best** Support Vector Machine
*  .5 Second Audio Segments
*  accuracy score : ~0.852
*  best kernel : linear
*  best gamma : 0.1
*  recordings pre-processed before segmentation to remove silences larger than 1s

**Second Best** Logistic Regression
*  .5 Second Audio Segments
*  accuracy score : ~0.839
*  best multi_class: l1
*  best multi_class: ovr
*  best class weight : None
*  fit intercept : True

Initially, successive grid searches produced very different model performance results. It's possible this was due to our relatively small dataset and the impact of randomness in our train/test data split. The following changes were introduced to partially account for this.

*  a random state of 22 was assigned for consistency
*  cross-validation was increased from 5 to 10
*  the source recordings were scrubbed of pauses lasting longer than one second
*  half second intervals were introduced to increase the volume of data points

These changes produced the best performing models. 

### Support Vector Machines
In all cases, the optimal hyperparameters for kernel and gamma were linear and .1 respectively. The selection of a linear kernel suggests the data might be linearly separable in higher dimensions. The Gamma value is not relevant to linear kernels, so it holds no significant in this case.

#### Logistic Regression
Logistic Regression with L1 regularization performed nearly as well as our SVM. Additional data pre-processing listed in Next Steps could further improve this. Logistic Regression is known to be less computationally demanding and its output is probalistic. There may be some practical applications of our model that favor these characteristic. 

#### Next steps
A score of ~0.852 is promising, but less than desirable if we were to deploy this for forensic of security purposes. Further work is needed to continue improving the model performance. A list of suggested next steps can be found below.

*  A deeper analysis of audio features that might be relevant to our model
*  Additional pre-processing to improve the quality of our sound recordings (e.g. exploring superior sample rates, removing background noise, etc.)
*  Adding to our dataset with additional recordings of each speaker in various settings and at various distances from the microphone


#### Outline of project

- [Link to notebook 1]()

