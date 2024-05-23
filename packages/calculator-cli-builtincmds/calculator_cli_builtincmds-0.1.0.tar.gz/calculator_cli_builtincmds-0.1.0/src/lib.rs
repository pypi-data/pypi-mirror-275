use minus::{dynamic_paging, ExitStrategy, MinusError, Pager};
use pyo3::{
    exceptions::{PyIOError, PyNotImplementedError},
    prelude::{pyfunction, pymodule, wrap_pyfunction, Bound, PyModule, PyResult},
};
use std::{fs::File, io::prelude::Read, thread::spawn};

/// Function to convert `MinusError` to PyErr
fn catch_err<T>(res: Result<T, MinusError>) -> PyResult<T> {
    match res {
        Ok(res) => Ok(res),
        Err(MinusError::Communication(_)) => {
            Err(PyIOError::new_err("Failed to send data to the pager"))
        }
        _ => Err(PyNotImplementedError::new_err("")),
    }
}

#[pyfunction]
pub fn show_file(file_name: &str, prompt: &str) -> PyResult<()> {
    let text = {
        let mut file = File::open(file_name)?;
        let mut text = String::new();
        file.read_to_string(&mut text)?;
        text
    };
    show_text(&text, prompt)
}

#[pyfunction]
pub fn show_text(text: &str, prompt: &str) -> PyResult<()> {
    let pager = Pager::new();
    let pager2 = pager.clone();
    let pager_thread = spawn(move || dynamic_paging(pager2));
    catch_err(pager.set_text(text))?;
    catch_err(pager.set_prompt(prompt))?;
    catch_err(pager.set_exit_strategy(ExitStrategy::PagerQuit))?;
    pager_thread.join().unwrap().unwrap();
    Ok(())
}

#[pymodule]
pub fn builtincmds(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(show_file, m)?)?;
    m.add_function(wrap_pyfunction!(show_text, m)?)?;
    Ok(())
}
