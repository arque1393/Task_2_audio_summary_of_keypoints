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
     error: subprocess-exited-with-error                                                                                                                                                                                                             × python setup.py bdist_wheel did not run successfully.                                                                 │ exit code: 1                                                                                                          ╰─> [25 lines of output]                                                                                                    /home/aritrarc1/anaconda3/envs/TF_TTS/lib/python3.9/site-packages/setuptools/__init__.py:80: _DeprecatedInstaller: setuptools.installer and fetch_build_eggs are deprecated.                                                                    !!                                                                                                                                                                                                                                                      ********************************************************************************                                        Requirements should be satisfied by a PEP 517 installer.                                                                If you are using pip, you can try `pip install --use-pep517`.                                                           ********************************************************************************                                                                                                                                                        !!                                                                                                                        dist.fetch_build_eggs(dist.setup_requires)                                                                            running bdist_wheel                                                                                                     /home/aritrarc1/anaconda3/envs/TF_TTS/bin/python /tmp/pip-install-4qi47g5p/llvmlite_5a8a5ea1ff41419b8b39a24cb3eeab8d/ffi/build.py                                                                                                               LLVM version... 14.0.0                                                                                                                                                                                                                          Traceback (most recent call last):                                                                                        File "/tmp/pip-install-4qi47g5p/llvmlite_5a8a5ea1ff41419b8b39a24cb3eeab8d/ffi/build.py", line 168, in <module>            main()                                                                                                                File "/tmp/pip-install-4qi47g5p/llvmlite_5a8a5ea1ff41419b8b39a24cb3eeab8d/ffi/build.py", line 158, in main                main_posix('linux', '.so')                                                                                            File "/tmp/pip-install-4qi47g5p/llvmlite_5a8a5ea1ff41419b8b39a24cb3eeab8d/ffi/build.py", line 120, in main_posix          raise RuntimeError(msg)                                                                                             RuntimeError: Building llvmlite requires LLVM 7.0+ Be sure to set LLVM_CONFIG to the right executable path.             Read the documentation at http://llvmlite.pydata.org/ for more information about building llvmlite.                                                                                                                                             error: command '/home/aritrarc1/anaconda3/envs/TF_TTS/bin/python' failed with exit code 1                               [end of output]                                                                                                                                                                                                                             note: This error originates from a subprocess, and is likely not a problem with pip.                                    ERROR: Failed building wheel for llvmlite                                                                               Running setup.py clean for llvmlite                                                                                   Successfully built numba                                                                                                Failed to build llvmlite                                                                                                ERROR: Could not build wheels for llvmlite, which is required to install pyproject.toml-based projects
    ```


