import numpy as np
import pandas as pd
import scanpy as sc
from numba import njit, prange
from gseapy import Msigdb

def get_df_from_gmt(categories, version, genes, min_gene_ratio=0.5, min_gene_count=5):
    """
    Retrieve gene sets from MSigDB and return a DataFrame.

    Args:
        categories (list or str): Categories of gene sets to retrieve.
        version (str): Version of the MSigDB database.
        genes (list): List of genes present in the adata.var_names.
        min_gene_ratio (float): Minimum ratio of genes present in the gene set to the total genes in the gene set.
        min_gene_count (int): Minimum number of genes present in the gene set.

    Returns:
        pandas.DataFrame: DataFrame containing gene sets and their associated genes.
    """
    
    msig = Msigdb()
    if isinstance(categories, str):
        categories = [categories]
    dfs = []
    for category in categories:
        gmt = msig.get_gmt(category=category, dbver=version)
        df = pd.DataFrame(gmt.items(), columns=['gene_set', 'genes'])
        dfs.append(df)
    if len(dfs) > 1:
        df = pd.concat(dfs, ignore_index=True)
    else:
        df = dfs[0]

    df['gene_present'] = df['genes'].apply(lambda x: len(set(x).intersection(set(genes))))
    df['total_genes'] = df['genes'].apply(lambda x: len(x))
    df['gene_names_present'] = df['genes'].apply(lambda x: list(set(x).intersection(set(genes))))
    df = df[(df['gene_present'] > min_gene_ratio * df['total_genes']) & (df['gene_present'] > min_gene_count)]
    df = df[df['gene_set'].str.startswith(('GO', 'KEGG', 'REACTOME'))]
    df.reset_index(drop=True, inplace=True)
    return df

@njit(parallel=True)
def get_rank_numba(X, axis=0):
    """
    Calculate the ranks of elements in a matrix along a specified axis using Numba.

    Args:
        X (numpy.ndarray): Input matrix.
        axis (int): Axis along which to calculate the ranks (0 for rows, 1 for columns).

    Returns:
        numpy.ndarray: Matrix of ranks.
    """
    if axis == 0:
        n_rows, n_cols = X.shape
        result = np.zeros_like(X, dtype=np.int64)
        for i in prange(n_rows):
            result[i] = np.argsort(np.argsort(-X[i]))
    else:
        n_rows, n_cols = X.shape
        result = np.zeros_like(X, dtype=np.int64)
        for i in prange(n_cols):
            result[:, i] = np.argsort(np.argsort(-X[:, i]))
    return result

def get_rank(adata, axis=0):
    """
    Calculate the ranks of elements in an AnnData object along a specified axis.

    Args:
        adata (scanpy.AnnData): Input AnnData object.
        axis (int): Axis along which to calculate the ranks (0 for rows, 1 for columns).

    Returns:
        scanpy.AnnData: AnnData object with ranks calculated.
    """
    adata = adata.copy()
    if not isinstance(adata.X, np.ndarray):
        adata.X = np.array(adata.X.todense())
    adata.X = get_rank_numba(adata.X, axis=axis)
    return adata

@njit
def calc_auc_numba(x_vals, gene_indices, axis=0):
    """
    Calculate the area under the curve (AUC) using Numba.

    Args:
        x_vals (numpy.ndarray): Input values.
        gene_indices (numpy.ndarray): Indices of genes.
        axis (int): Axis along which to calculate the AUC (0 for rows, 1 for columns).

    Returns:
        float: AUC value.
    """
    if axis == 0:
        y_vals = np.zeros(len(x_vals))
        indices = x_vals[gene_indices]
        for i in range(0, len(x_vals)):
            if i > 0:
                y_vals[i] = y_vals[i - 1]
            if i in indices:
                y_vals[i] += 1 / len(indices)
        return np.trapz(y_vals)
    else:
        y_vals = np.zeros(len(x_vals))
        x_vals = np.argsort(np.argsort(x_vals))
        indices = x_vals[gene_indices]
        for i in range(0, len(x_vals)):
            if i > 0:
                y_vals[i] = y_vals[i - 1]
            if i in indices:
                y_vals[i] += 1 / len(indices)
        return np.trapz(y_vals)

def get_auc(adata, df, axis=0):
    """
    Calculate the area under the curve (AUC) for gene sets in an AnnData object.

    Args:
        adata (scanpy.AnnData): Input AnnData object.
        df (pandas.DataFrame): DataFrame containing gene sets and their associated genes.
        axis (int): Axis along which to calculate the AUC (0 for rows, 1 for columns).

    Returns:
        scanpy.AnnData: AnnData object with AUC values calculated.
    """
    matrix = np.zeros((adata.shape[0], len(df)))
    old_adata = adata.copy()
    adata = get_rank(adata, axis=axis)
    var_names = adata.var_names.tolist()
    for i in range(len(df)):
        genes = df.iloc[i]['genes']
        gene_indices = np.array([var_names.index(gene) for gene in genes if gene in var_names])
        for j in range(adata.shape[0]):
            matrix[j, i] = calc_auc_numba(adata.X[j], gene_indices, axis=axis)
    new_adata = sc.AnnData(matrix)
    new_adata.obs = adata.obs
    new_adata.var = pd.DataFrame(df['gene_set'])
    new_adata.var_names = df['gene_set']
    new_adata.obs_names = adata.obs_names
    new_adata.obsm = adata.obsm
    new_adata.obsp = adata.obsp
    return new_adata
