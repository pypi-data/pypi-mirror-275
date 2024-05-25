PacSpedd Base
=============

A Python Module, but written in Rust.

Advantages of PacSpedd Base
===========================

PacSpedd Base leverages the power of Rust to provide several key advantages over traditional Python modules:

1. **Fast Import Times**: 
    - Since the Rust code is compiled into a binary format, importing the module in Python is significantly faster compared to pure Python modules.

2. **Unified Codebase**:
    - **Simplified Maintenance**: By handling Windows and Linux specific code within a single function in Rust, there is no need for separate versions for each operating system. This makes the module easier to maintain and extend.
    - **Consistent Behavior**: A single code path for both operating systems ensures consistent results and reduces potential errors.

3. **Efficient System Resource Utilization**:
    - **Direct System Interaction**: Rust allows for more direct and efficient interaction with the system, making the execution of system commands more reliable and faster, especially for complex commands.

4. **Enhanced Security and Reliability**:
    - **Memory Safety**: Rust's guarantees around memory safety reduce the risk of memory-related errors, leading to more robust and stable software.
    - **Error Handling**: Rust's strong type system and error handling mechanisms help catch runtime errors early, ensuring more reliable execution.

Using these advantages, PacSpedd Base provides a powerful and efficient solution for executing system commands and other operations within your Python projects.

Installation
============

From PyPI (Stable)
------------------

To install the stable version from PyPI:

.. code-block:: bash

    pip install --no-cache-dir pacspeddbase

From GitHub (Newest)
--------------------

To install the newest version directly from GitHub:

Option 1: Using archive
_______________________

.. code-block:: bash

    pip install --no-cache-dir https://github.com/PacSpedd/pacspeddbase/archive/master.zip

Option 2: Cloning repository
____________________________

.. code-block:: bash

    git clone https://github.com/PacSpedd/pacspeddbase
    cd pacspeddbase
    pip install .

Requirements
============

You need to have Rust and Maturin installed. Follow the instructions below to set them up.

1. Install Rust
===============

Linux
-----

.. code-block:: bash

    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

Windows (winget)
----------------

.. code-block:: bash

    winget install rust

Windows (scoop)
---------------

.. code-block:: bash

    scoop install rust

Termux (Few Support)
--------------------

Using apt
_________

.. code-block:: bash

    apt-get update -qq
    apt-get install rust ldd binutils build-essential -y

Using pacman
____________

.. code-block:: bash

    pacman -Syy
    pacman -S --noconfirm rust ldd binutils build-essential

Using pkg (default)
___________________

.. code-block:: bash

    pkg up
    pkg in rust ldd binutils build-essential

Proot-Distro (Best Way)
_______________________

Install Proot-Distro
____________________

.. code-block:: bash

    pkg up
    pkg in proot-distro
    pd i ubuntu

Setup Proot-Distro
__________________

.. code-block:: bash

    apt-get update
    apt-get upgrade -y
    apt-get install sudo adduser neovim build-essential -y
    useradd -m -s /bin/bash userx
    echo "userx ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/userx
    chmod 0440 /etc/sudoers.d/userx
    su - userx
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

2. Install Maturin
==================

Attention to the Termux users, Maturin cannot always be successfully compiled on Termux, I will package successful Maturin builds as a .zip with a setup.sh which Maturin stores correctly and also package it as a .deb

.. code-block:: bash

    pip install maturin

3. Using Pacspedd Base
======================

Import the Module
-----------------

.. code-block:: python

    import pacspeddbase as psb

Hello World with PacSpedd Base
------------------------------

.. code-block:: python

    psb.print("Hello World")

How is it Working
_________________

The Thing is, the Module is full Rust Based, print called following Function

.. code-block:: rust

    #[pyfunction]
    fn print(text: &str) -> PyResult<()> {
        println!("{}", text);
    }

I mean with that, The Print Function in PacSpedd Base Called the Rust Print Line Function.

Get an Enviroment Variable
--------------------------

.. code-block:: python

    HOME = psb.get_env('HOME')

How is it Working
_________________

.. code-block:: rust

    #[pyfunction]
    fn get_env(var:&str) -> PyResult<Option<String>> {
        let value = env::var(var).ok()
        OK(value)
    }


System Class in Pacspedd Base
=============================

PacSpedd Base have a System Class

Setup
-----

.. code-block:: python

    system = psb.System()

Execute a Command
-----------------

.. code-block:: python
    
    command = "apt update"
    system.cmd(command)

Make a Once Directory
---------------------

.. code-block:: python

    import os
    HOME = psb.get_env('HOME')
    path = os.path.join(HOME, 'example')
    psb.mkdir(path)

Make More then One Directory
----------------------------

.. code-block:: python

    import os
    HOME = psb.get_env('HOME')
    path = os.path.join(HOME, 'example', '1', '2', '3')
    psb.makedirs(path)

Change Curent Directory
-----------------------

.. code-block:: python

    psb.cd(path)

How is it Working
_________________

.. code-block:: rust

    #[pymethods]
    impl System {
        #[new]
        fn new() -> Self {
            System
        }

        /// Execute a command
        ///
        /// Args:
        ///     command (str): The command to execute
        fn cmd(&self, command: &str) -> PyResult<()> {
            let output = if cfg!(target_os = "windows") {
                Command::new("cmd")
                    .arg("/C")
                    .arg(command)
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to execute command: {}", e)))?
            } else {
                Command::new("sh")
                    .arg("-c")
                    .arg(command)
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to execute command: {}", e)))?
            };

            if !output.status.success() {
                return Err(pyo3::exceptions::PyRuntimeError::new_err(format!("Command failed: {}", output.status)));
            }

            Ok(())
        }

        /// Create a directory
        ///
        /// Args:
        ///     path (str): The path of the directory to create
        fn mkdir(&self, path: &str) -> PyResult<()> {
            fs::create_dir(path)
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to create directory: {}", e)))?;
            Ok(())
        }

        /// Change the current working directory
        ///
        /// Args:
        ///     path (str): The path of the directory to change to
        fn cd(&self, path: &str) -> PyResult<()> {
            env::set_current_dir(path)
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to change directory: {}", e)))?;
            Ok(())
        }

        /// List files in the current directory
        ///
        /// Returns:
        ///     List[str]: A list of file names in the current directory
        fn list_files(&self) -> PyResult<Vec<String>> {
            let paths = fs::read_dir(".")
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to read directory: {}", e)))?;
            
            let mut files = Vec::new();
            for path in paths {
                let path = path.map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to read path: {}", e)))?;
                files.push(path.path().display().to_string());
            }
            Ok(files)
        }

        /// Clear the Terminal
        ///
        /// Args:
        ///     None:
        fn clear(&self) -> PyResult<()> {
            let _output = if cfg!(target_os = "windows") {
                Command::new("cls")
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Clear Terminal: {}", e)))?
            } else {
                Command::new("clear")
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Clear Terminal: {}", e)))?
            };
            Ok(())
        }

        /// Wget Interaction
        /// 
        /// Args:
        ///     url: The Download url
        fn wget(&self, url: &str) -> PyResult<()> {
            let _output = if cfg!(target_os = "windows") {
                Command::new("wget")
                    .arg(url)
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Download File: {}", e)))?
            } else {
                Command::new("wget")
                    .arg(url)
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Download File: {}", e)))?
            };
            Ok(())
        }

        /// Make Much Dirs
        /// 
        /// Args:
        ///     path: The path
        fn makedirs(&self, path: &str) -> PyResult<()> {
            let _output = if cfg!(target_os = "windows") {
                Command::new("mkdir")
                    .arg(path)
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Create Directorys: {}", e)))?
            } else {
                Command::new("mkdir")
                    .arg("-p")
                    .arg(path)
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Create Directorys: {}", e)))?
            };
            Ok(())
        }

        /// Copy files
        /// 
        /// Args:
        ///     path 1 (str): The Source Path
        ///     path 2 (str): The Dist Path
        fn copy(&self, srcpath: &str, despath: &str) -> PyResult<()> {
            let _output = if cfg!(target_os = "windows") {
                Command::new("cp")
                    .arg(srcpath)
                    .arg(despath)
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Copy files: {}", e)))?
            } else {
                Command::new("cp")
                    .arg("-rf")
                    .arg(srcpath)
                    .arg(despath)
                    .stdout(Stdio::inherit())
                    .stderr(Stdio::inherit())
                    .output()
                    .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Copy Files: {}", e)))?
            };
            Ok(())
        }

    }