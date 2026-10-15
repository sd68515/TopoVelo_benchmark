# TopoVelo benchmark source fork

This fork supports [VelocityBenchmarking](https://github.com/vikkihuangkexin/VelocityBenchmarking) and is based on [welch-lab/TopoVelo](https://github.com/welch-lab/TopoVelo) commit `c0a684f2ce75ae770ec5753f70d2c09d78808b55`. Please cite the original TopoVelo work when using the method.

## Compatibility changes

| File and location | Change | Reason |
| --- | --- | --- |
| `topovelo/__init__.py`, package import | Restores `matplotlib.cbook.mplDeprecation` when absent. | Keeps scVelo 0.2.5 importable with newer Matplotlib. |
| `topovelo/model/model_util.py`, `_parallel_jobs`, `init_params_parallel`, `reinit_params_parallel`, `knnx0_index_parallel` | Uses a thread pool with at most eight workers by default; `TOPOVELO_N_JOBS` sets another positive limit. | Limits worker count and avoids process-level array copies during ODE initialization and KNN refinement. |
| `topovelo/model/training_data.py`, `SCGraphData.__init__` | Removes the unused dense `graph.A` copy; edge extraction remains unchanged. | Reduces peak memory for spatial graphs. |
| `topovelo/model/vae.py`, `_load_data` | Converts concatenated spliced and unspliced inputs to `float32`. | Matches model input precision and reduces retained array memory. |
| `topovelo/model/vae.py`, `train_epoch` and `train_spatial_epoch` | Enables DataLoader pinned memory only for CUDA devices. | Avoids unnecessary pinned memory on CPU. |
| `topovelo/model/vae.py`, configuration, `eval_model_batch`, `train_epoch`, `train_spatial_epoch` | Makes per-batch `torch.cuda.empty_cache()` optional through `empty_cache_each_batch` (default `False`). | Avoids repeated cache clearing during training and evaluation. |

The VAE architecture, kinetic equations, losses, and graph construction are unchanged. The `float32` conversion may affect numerical results. Dataset preparation, training parameters, and device selection belong to the separate benchmark runner.

## Environment

Reference versions: Python 3.9.21 and PyTorch 2.1.0+cu121. The retained package metadata does not define a complete environment lock.

## Installation

Install the retained `topovelo/` package from this checkout in an environment with compatible dependencies:

```bash
python -m pip install --no-deps -e .
```

Datasets, benchmark runners, notebooks, checkpoints, and results are not included.

## License

The upstream GPL-3.0 `LICENSE` is retained unchanged.
