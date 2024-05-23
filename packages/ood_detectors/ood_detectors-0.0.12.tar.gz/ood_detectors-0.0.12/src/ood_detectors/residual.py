import numpy as np
from sklearn.covariance import EmpiricalCovariance
import torch


class Residual:
    """
    Residual class for outlier detection.

    Args:
        dims (int): Number of dimensions to consider for outlier detection. Default is 512.
        u (int): Mean value for data centering. Default is 0.

    Attributes:
        dims (int): Number of dimensions to consider for outlier detection.
        u (int): Mean value for data centering.
        name (str): Name of the Residual instance.

    Methods:
        fit(data, *args, **kwargs): Fit the Residual model to the given data.
        predict(data, *args, **kwargs): Predict the outlier scores for the given data.
        to(device): Move the Residual model to the specified device.
        state_dict(): Get the state dictionary of the Residual model.
        load_state_dict(state_dict): Load the state dictionary into the Residual model.

    """

    def __init__(self, dims=512, u=0):
        self.dims = dims
        self.u = u
        self.name = "Residual"

    def fit(self, data, *args, collate_fn=None, **kwargs):
        """
        Fit the Residual model to the given data.

        Args:
            data (array-like or torch.Tensor or torch.utils.data.DataLoader): Input data for fitting the model.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            list: An empty list.

        """
            
        if isinstance(data, (list, tuple)):
            data = np.array(data)
        elif isinstance(data, torch.Tensor):
            data = data.cpu().numpy()
        elif isinstance(data, torch.utils.data.Dataset):
            if collate_fn is None and getattr(data, 'collate_fn', None) is not None:
                collate_fn = data.collate_fn
            if collate_fn is None:
                data = np.vstack([x.cpu().numpy() for x, *_ in data])
            else:
                data = np.vstack([collate_fn([d]).cpu().numpy() for d in data])
        feat_dim = data.shape[-1]
        if self.dims is None:
            self.dims = 1000 if feat_dim >= 2048 else 512 
        if self.dims <= 1:
            self.dims = int(feat_dim * self.dims)
        if self.dims < 2:
            self.dims = 2
    
        ec = EmpiricalCovariance(assume_centered=True)
        ec.fit(data - self.u)
        eig_vals, eigen_vectors = np.linalg.eig(ec.covariance_)
        self.ns = np.ascontiguousarray(
            (eigen_vectors.T[np.argsort(eig_vals * -1)[self.dims :]]).T
        ).astype(np.float32)
        return [-1]

    def predict(self, data, batch_size=32, *args, collate_fn=None, **kwargs):
        """
        Predict the outlier scores for the given data in batches.

        Args:
            data (array-like, torch.Tensor, torch.utils.data.DataLoader, or torch.utils.data.Dataset): Input data for predicting the outlier scores.
            batch_size (int): The size of the batches to use for prediction.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            numpy.ndarray: Outlier scores for the input data.
        """
        def to_numpy(data_batch):
            if isinstance(data_batch, torch.Tensor):
                return data_batch.cpu().numpy()
            elif isinstance(data_batch, (list, tuple)):
                return np.array(data_batch)
            return data_batch

        if isinstance(data, (list, tuple, np.ndarray)):
            data = torch.tensor(data, dtype=torch.float32)
            dataset = torch.utils.data.TensorDataset(data)
            data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=False)
        elif isinstance(data, torch.Tensor):
            dataset = torch.utils.data.TensorDataset(data)
            data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=False)
        elif isinstance(data, torch.utils.data.Dataset):
            data_loader = torch.utils.data.DataLoader(data, batch_size=batch_size, shuffle=False, collate_fn=collate_fn)
        elif isinstance(data, torch.utils.data.DataLoader):
            data_loader = data
        else:
            raise TypeError("Unsupported data type: {}".format(type(data)))

        scores = []
        for batch in data_loader:
            batch = batch[0]  # TensorDataset returns a tuple
            batch_numpy = to_numpy(batch)
            batch_numpy = batch_numpy.astype(np.float32)
            batch_scores = np.linalg.norm((batch_numpy - self.u) @ self.ns, axis=-1)
            scores.append(batch_scores)

        return np.concatenate(scores)

    def __call__(self, *args, **kwargs):
        return self.predict(*args, **kwargs)

    def to(self, device):
        """
        Move the Residual model to the specified device.

        Args:
            device: Device to move the model to.

        """
        pass

    def state_dict(self):
        """
        Get the state dictionary of the Residual model.

        Returns:
            dict: State dictionary of the Residual model.

        """
        return {"dims": self.dims, "u": self.u, "ns": self.ns}

    def load_state_dict(self, state_dict):
        """
        Load the state dictionary into the Residual model.

        Args:
            state_dict (dict): State dictionary to load into the Residual model.

        Returns:
            self: Loaded Residual model.

        """
        self.dims = state_dict["dims"]
        self.u = state_dict["u"]
        self.ns = state_dict["ns"]
        return self
