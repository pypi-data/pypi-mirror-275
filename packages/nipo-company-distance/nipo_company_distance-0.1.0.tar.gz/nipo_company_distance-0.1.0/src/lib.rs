use pyo3::{exceptions::PyValueError, prelude::*};
use edit_distance::edit_distance;

/// Calculates the levenshtein distance between two lists of strings.
#[pyfunction]
fn find_best_match_levenshtein(company_names: Vec<String>, patent_applicant_names: Vec<String>, threshold: f32) -> PyResult<Vec<String>> {
    if threshold < 0.0 || threshold > 1.0 {
        return Err(PyValueError::new_err("threshold must be between 0 and 1"));
    }
    if company_names.is_empty() {
        return Err(PyValueError::new_err("Company names list must not be empty"))
    }

    if patent_applicant_names.is_empty() {
        return Err(PyValueError::new_err("Patent applicants names list must not be empty"))
    }
    let mut valid_matches: Vec<String> = vec![];
    for pa_name in patent_applicant_names.iter() {
        let mut best_match: (usize, String) = (100, "".to_string());
        for company_name in company_names.iter() {
            let levenshtein_distance: usize = edit_distance(&pa_name.to_lowercase(), &company_name.to_lowercase());
            if levenshtein_distance == 0 {
                valid_matches.push(pa_name.to_string());
                break
            }
            if levenshtein_distance <= best_match.0 {
                best_match = (levenshtein_distance, pa_name.to_string());
            }
        }
        if (best_match.0 as f32 / best_match.1.len() as f32) <= 1.0-threshold {
            valid_matches.push(best_match.1);
        }
    }
    Ok(valid_matches)
}

/// A Python module implemented in Rust.
#[pymodule]
fn nipo_company_distance(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(find_best_match_levenshtein, m)?)?;
    Ok(())
}
