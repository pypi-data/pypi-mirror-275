use pyo3::prelude::*;
use std::env;
use std::fs;
use std::process::{Command, Stdio};
use pyo3::types::PyString;

#[pyclass]
/// A class for printing colors in RGB style in Python
pub struct Color {
    #[pyo3(get, set)]
    red: u8,
    #[pyo3(get, set)]
    green: u8,
    #[pyo3(get, set)]
    blue: u8,
}

#[pymethods]
impl Color {
    #[new]
    /// Create a new Color
    ///
    /// Args:
    ///     red (int): The red component (0-255).
    ///     green (int): The green component (0-255).
    ///     blue (int): The blue component (0-255).
    fn new(red: u8, green: u8, blue: u8) -> Self {
        Color { red, green, blue }
    }

    /// Get the hex representation of the color
    ///
    /// Returns:
    ///     str: The hex representation of the color
    fn hex(&self) -> String {
        format!("#{:02X}{:02X}{:02X}", self.red, self.green, self.blue)
    }

    /// Get the ANSI escape code for the color
    ///
    /// Returns:
    ///     str: The ANSI escape code for the color
    fn ansi(&self) -> String {
        format!("\x1b[38;2;{};{};{}m", self.red, self.green, self.blue)
    }
}

/// Print a normal message to STDOUT
///
/// Args:
///     text (str): The message to print
#[pyfunction]
fn print(text: &str) -> PyResult<()> {
    println!("{}", text);
    Ok(())
}

/// Print a colored message to STDOUT
///
/// Args:
///     text (str): The message to print
///     color (Color, optional): The color for the text
#[pyfunction]
fn cprint(text: &str, color: Option<&Color>) -> PyResult<()> {
    if let Some(color) = color {
        let ansi_color = color.ansi();
        println!("{}{}{}", ansi_color, text, "\x1b[0m");
    } else {
        println!("{}", text);
    }
    Ok(())
}

/// Get the value of an environment variable
///
/// Args:
///     var (str): The name of the environment variable
///
/// Returns:
///     str: The value of the environment variable, or None if it is not set
#[pyfunction]
fn get_env(var: &str) -> PyResult<Option<String>> {
    let value = env::var(var).ok();
    Ok(value)
}

#[pyclass]
pub struct System;

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

    /// List Files in Dir, but in Better output
    /// 
    /// Args:
    ///     path: The Path That you want Show
    fn listdir(&self, path: &str) -> PyResult<()> {
        let _output = if cfg!(target_os = "windows") {
            Command::new("dir")
                .arg(path)
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .output()
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to List Files: {}", e)))?
        } else {
            Command::new("ls")
                .arg("-A")
                .arg(path)
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .output()
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to List Files: {}", e)))?
        };

        Ok(())
    }

    /// Source/Call files
    /// 
    /// Args:
    ///  Path (str): The Path to Source
    fn source(&self, path: &str) -> PyResult<()> {
        let _output = if cfg!(target_os = "windows") {
            Command::new("call")
                .arg(path)
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .output()
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Call File: {}", e)))?
        } else {
            Command::new("source")
                .arg(path)
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .output()
                .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to Source File: {}", e)))?
        };

        Ok(())
    }

}

#[pyclass]
struct Args {}

#[pymethods]
impl Args {
    #[new]
    fn new() -> Self {
        Args {}
    }

    fn get(&self, position: usize) -> PyResult<Option<String>> {
        let args: Vec<_> = std::env::args().skip(1).collect();
        if position < args.len() {
            Ok(Some(args[position].clone()))
        } else {
            Ok(None)
        }
    }

    fn get_from(&self, position: usize) -> PyResult<Vec<String>> {
        let args: Vec<_> = std::env::args().skip(1).collect();
        if position < args.len() {
            Ok(args[position..].to_vec())
        } else {
            Ok(vec![])
        }
    }
}

#[pyfunction]
fn argv(position: usize) -> PyResult<Option<String>> {
    let args: Vec<_> = std::env::args().skip(1).collect();
    if position < args.len() {
        Ok(Some(args[position].clone()))
    } else {
        Ok(None)
    }
}

#[pyfunction]
fn argv_from(position: usize) -> PyResult<Vec<String>> {
    let args: Vec<_> = std::env::args().skip(1).collect();
    if position < args.len() {
        Ok(args[position..].to_vec())
    } else {
        Ok(vec![])
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn pacspeddbase(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(print, m)?)?;
    m.add_function(wrap_pyfunction!(get_env, m)?)?;
    m.add_class::<System>()?;
    m.add_class::<Color>()?;
    m.add_class::<Args>()?;
    m.add_function(wrap_pyfunction!(cprint, m)?)?;
    m.add_function(wrap_pyfunction!(argv, m)?)?;
    m.add_function(wrap_pyfunction!(argv_from, m)?)?;
    Ok(())
}
