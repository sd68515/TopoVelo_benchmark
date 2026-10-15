import warnings

import matplotlib.cbook as cbook

# scvelo 0.2.5 refers to this matplotlib alias during import. Matplotlib
# removed it in 3.8; restoring the warning class keeps imports working without
# changing TopoVelo's calculations.
if not hasattr(cbook, "mplDeprecation"):
    cbook.mplDeprecation = DeprecationWarning

from topovelo.model import VAE, sample_genes
from topovelo.model.model_util import get_spatial_tprior
from topovelo.simulation import simulate, to_low_res
from topovelo.analysis.evaluation import post_analysis
from topovelo.analysis.perf_logger import PerfLogger
from .plotting import (
    get_colors,
    compute_figsize,
    plot_sig,
    plot_phase,
    plot_cluster,
    plot_heatmap,
    plot_time,
    plot_time_var,
    plot_state_var,
    plot_train_loss,
    plot_test_loss,
    plot_phase_grid,
    plot_sig_grid,
    plot_time_grid,
    plot_velocity
)
from .preprocessing import (
    preprocess,
    build_spatial_graph
)

__all__ = [
    'VAE',
    'post_analysis',
    'PerfLogger',
    'get_colors',
    'compute_figsize',
    'preprocess',
    'build_spatial_graph',
    'simulate',
    'to_low_res',
    'sample_genes',
    'get_spatial_tprior'
]
