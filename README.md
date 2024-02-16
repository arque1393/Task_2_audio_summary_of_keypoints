### Overview 
This Repository Contains a Notebook where I have experiment with various Text To speech Models. 
- My all work presented in [Note.ipynb](https://github.com/arque1393/Task_2_audio_summary_of_keypoints/blob/master/Note.ipynb) and note file
- Video Description Link
    - https://1drv.ms/u/s!Aj2Nbw_0FL8Hia4tQTFEtReMegDGSw?e=VcsWG1
### Models and library that I have Explored 
1. Library : Coqui TTS <br>
    + **Model** : "tts_models/multilingual/multi-dataset/xtts_v2" <br>
    + **Remark** : As Voice Cloning and TTS model it generate very good result but it takes longer time to generate output.

2. TensorflowTTS 
    + **Remark**: Cant explore due to installation Issue

3. ESPNet
    + **Model** :  'espnet/kan-bayashi_ljspeech_vits'
    + **Remark** : generate beautiful speech in very minimum time.
4. SpeechBrain 
    + **Model** : speechbrain/tts-fastspeech2-ljspeech
    + **Remark** : Voice are Quite Mechanical Not like original human voice 
4. Transformers, Datasets 
    + **Model** : "microsoft/speecht5_tts"
    + **Datasets** : "Matthijs/cmu-arctic-xvectors"
    + **Remarks** : Huge variate is available in datasets. Generate text to speech uding the dataset. can be fine tuned on custome data 
5. Transformers, Datasets 
    + **Model** : "suno/bark"
    + **Remark** : Very Good speech generation but all text are not processed properly.
6. Transformers, Datasets 
    + **Model**: facebook/mms-tts-eng 
    + **Remark** : Very Good speech generation. Accents are human like.
6. gtts 
    - Remark : Word to Word Text to speech
7. Google Cloud Text To Speech 
    - Remark : Unable to implement practically due to billing account required
8. Amazon Polly
    - Remark : Unable to implement practically due to billing account required

9. IBM Watson
    - Remark : Unable to implement practically due to billing account required

### Environment Information 
- I work on this note book on Two different Environment 
    Environment 1 Information 
    ```
    Operating System : Windows 10 
    Virtual Environment : Anaconda / conda 
    Python Version : 3.11
    Implemented Models :
        1. "microsoft/speecht5_tts"
        2. "suno/bark"
        3. gtts
    ```
    Environment 2 Information
    ```
    Operating System : WSL Ubuntu 22.04.3 LTS
    Virtual Environment : Anaconda / conda 
    Python Version : 3.9
    Implemented Models :
        1. Coqui TTS    "tts_models/multilingual/multi-dataset/xtts_v2"
        2. ESPNet   'espnet/kan-bayashi_ljspeech_vits'
    ```

### Web Interface 
- Create the interface using gradio library of python in WSL system by integrating ESPNet 'espnet/kan-bayashi_ljspeech_vits' model as a tts tools

### Installation Solution Log 
I have Created a [Installation_solution log](https://github.com/arque1393/Task_2_audio_summary_of_keypoints/blob/master/Installation_solution.md) in this repository to log my approach to install 
**Coqui TTS** and **ESPNet** library 
