# How do I install Coqui/TTS
GitHub :  https://github.com/coqui-ai/TTS.git

- I use WSL Ubuntu 22.04.3 LTS
- Using Conda environment with Python = 3.9
- Install command  from Github
    ```shell
    pip install TTS
    ```
    ```
    git clone https://github.com/coqui-ai/TTS
    pip install -e .[all,dev,notebooks]  
    ```
- Error Message 
    ```        
    error: command 'x86_64-linux-gnu-gcc' failed: No such file or directory
    [end of output]
    
    note: This error originates from a subprocess, and is likely not a problem with pip.
    ERROR: Failed building editable for TTS
    Failed to build TTS
    ERROR: Could not build wheels for TTS, which is required to install pyproject.toml-based projects
    ```
- Stack Overflow Link 
    https://stackoverflow.com/questions/26053982/setup-script-exited-with-error-command-x86-64-linux-gnu-gcc-failed-with-exit


- Using This Shell Command to install Build Tools 

    ``` Shell
    sudo apt install gcc
    sudo apt-get install python3-dev
    ```

- Try to install again and Installation became **Successful**




# How do I install ESPNet in my system

- I use WSL Ubuntu 22.04.3 LTS
- Using Conda environment with Python = 3.9
- Previous configuration is exacly same
- Install command  from Github
    ```shell
    pip install espnet
    ```
- Error Message 
    ```
    gcc: fatal error: cannot execute ‘cc1plus’: execvp: No such file or directory
    compilation terminated.
    error: command '/usr/bin/gcc' failed with exit code 1
    [end of output]

    note: This error originates from a subprocess, and is likely not a problem with pip.
    ERROR: Failed building wheel for pyworld
    ```
- Stack Overflow Link 
    https://stackoverflow.com/questions/11912878/gcc-error-gcc-error-trying-to-exec-cc1-execvp-no-such-file-or-directory

- Update Build Essential with this command 
    ```
    sudo apt-get update
    sudo apt-get install --reinstall build-essential
    ```

- Try To install again and became **Successful**


# How do I Tru to install TensorflowTTS

- I use WSL Ubuntu 22.04.3 LTS
- Using Conda environment with Python = 3.9
- Previous configuration is exactly same
- Install command using pip and from Github directly
    ```shell
    pip install TensorflowTTS
    ```
    ```
    git clone https://github.com/TensorSpeech/TensorFlowTTS.git
    cd TensorFlowTTS
    pip install .
    ```
    
- Error Message 
    ```
    ```

- Try To install again but It does not  work
