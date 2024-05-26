use crate::{
    metronome::{Beat, MaybeMetronome},
    nodes::instrument::Tone,
    notation::Item,
    pitch::MaybePitchStandard,
    resolve_index, resolve_index_for_insert,
};
use libdaw::{metronome::Beat as DawBeat, notation::Overlapped as DawOverlapped};
use pyo3::{
    exceptions::PyIndexError, pyclass, pymethods, Bound, IntoPy as _, Py, PyResult,
    PyTraverseError, PyVisit, Python,
};
use std::{
    ops::Deref as _,
    sync::{Arc, Mutex},
};

#[pyclass(module = "libdaw.notation")]
#[derive(Debug, Clone)]
pub struct Overlapped {
    pub inner: Arc<Mutex<DawOverlapped>>,
    pub items: Vec<Item>,
}

impl Overlapped {
    pub fn from_inner(py: Python<'_>, inner: Arc<Mutex<DawOverlapped>>) -> Py<Self> {
        let items = inner
            .lock()
            .expect("poisoned")
            .items
            .iter()
            .cloned()
            .map(move |item| Item::from_inner(py, item))
            .collect();
        Self { inner, items }
            .into_py(py)
            .downcast_bound(py)
            .unwrap()
            .clone()
            .unbind()
    }
}

#[pymethods]
impl Overlapped {
    #[new]
    pub fn new(py: Python<'_>, items: Option<Vec<Item>>) -> Self {
        let items = items.unwrap_or_default();
        Self {
            inner: Arc::new(Mutex::new(DawOverlapped {
                items: items.iter().map(move |item| item.as_inner(py)).collect(),
            })),
            items,
        }
    }

    #[staticmethod]
    pub fn loads(py: Python<'_>, source: String) -> crate::Result<Py<Self>> {
        Ok(Self::from_inner(py, Arc::new(Mutex::new(source.parse()?))))
    }

    #[pyo3(
        signature = (
            *,
            offset=Beat(DawBeat::ZERO),
            metronome=MaybeMetronome::default(),
            pitch_standard=MaybePitchStandard::default(),
        )
    )]
    pub fn tones(
        &self,
        offset: Beat,
        metronome: MaybeMetronome,
        pitch_standard: MaybePitchStandard,
    ) -> Vec<Tone> {
        let metronome = MaybeMetronome::from(metronome);
        let pitch_standard = MaybePitchStandard::from(pitch_standard);
        self.inner
            .lock()
            .expect("poisoned")
            .tones(offset.0, &metronome, pitch_standard.deref())
            .map(Tone)
            .collect()
    }

    pub fn length(&self) -> Beat {
        Beat(self.inner.lock().expect("poisoned").length())
    }

    pub fn duration(&self) -> Beat {
        Beat(self.inner.lock().expect("poisoned").duration())
    }

    pub fn __repr__(&self) -> String {
        format!("{:?}", self.inner.lock().expect("poisoned"))
    }
    pub fn __str__(&self) -> String {
        format!("{:#?}", self.inner.lock().expect("poisoned"))
    }

    pub fn __len__(&self) -> usize {
        self.items.len()
    }

    pub fn __getitem__(&self, index: isize) -> PyResult<Item> {
        let index = resolve_index(self.items.len(), index)?;
        Ok(self.items[index].clone())
    }
    pub fn __setitem__(&mut self, py: Python<'_>, index: isize, value: Item) -> PyResult<()> {
        let index = resolve_index(self.items.len(), index)?;
        self.inner.lock().expect("poisoned").items[index] = value.as_inner(py);
        self.items[index] = value;
        Ok(())
    }
    pub fn __delitem__(&mut self, index: isize) -> PyResult<()> {
        self.pop(Some(index)).map(|_| ())
    }

    pub fn __iter__(&self) -> OverlappedIterator {
        OverlappedIterator(self.items.clone().into_iter())
    }

    pub fn append(&mut self, py: Python<'_>, value: Item) -> PyResult<()> {
        self.inner
            .lock()
            .expect("poisoned")
            .items
            .push(value.as_inner(py));
        self.items.push(value);
        Ok(())
    }

    pub fn insert(&mut self, py: Python<'_>, index: isize, value: Item) -> PyResult<()> {
        let index = resolve_index_for_insert(self.items.len(), index)?;
        self.inner
            .lock()
            .expect("poisoned")
            .items
            .insert(index, value.as_inner(py));
        self.items.insert(index, value);
        Ok(())
    }

    pub fn pop(&mut self, index: Option<isize>) -> PyResult<Item> {
        let len = self.items.len();
        if len == 0 {
            return Err(PyIndexError::new_err("Pop from empty"));
        }
        let index = match index {
            Some(index) => resolve_index(self.items.len(), index)?,
            None => len - 1,
        };

        self.inner.lock().expect("poisoned").items.remove(index);
        Ok(self.items.remove(index))
    }

    pub fn __getnewargs__(&self) -> (Vec<Item>,) {
        (self.items.clone(),)
    }

    fn __traverse__(&self, visit: PyVisit<'_>) -> Result<(), PyTraverseError> {
        for item in &self.items {
            visit.call(item)?
        }
        Ok(())
    }

    pub fn __clear__(&mut self) {
        self.inner.lock().expect("poisoned").items.clear();
        self.items.clear();
    }
}

#[derive(Debug, Clone)]
#[pyclass(sequence, module = "libdaw.notation")]
pub struct OverlappedIterator(pub std::vec::IntoIter<Item>);

#[pymethods]
impl OverlappedIterator {
    pub fn __iter__(self_: Bound<'_, Self>) -> Bound<'_, Self> {
        self_
    }
    pub fn __repr__(&self) -> String {
        format!("OverlappedIterator<{:?}>", self.0)
    }
    pub fn __next__(&mut self) -> Option<Item> {
        self.0.next()
    }
}
