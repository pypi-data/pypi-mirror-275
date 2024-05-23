import torch
from ood_detectors import train, losses, ood_utils
from ood_detectors.models import SimpleMLP
from ood_detectors.sde import VESDE, subVPSDE, VPSDE
import torch.optim as optim
import functools


class Likelihood:
    """Base class for likelihood function implementations for different SDEs with dependency injection.

    Args:
        sde (object): The SDE object representing the stochastic differential equation.
        optimizer (function): The optimizer function used for training the model. Default is Adam optimizer.
        model (object): The model object used for likelihood estimation. If None, a SimpleMLP model will be created.
        feat_dim (int): The feature dimension of the model. Required if model is None.

    Attributes:
        model (object): The model object used for likelihood estimation.
        sde (object): The SDE object representing the stochastic differential equation.
        optimizer (object): The optimizer object used for training the model.
        device (str): The device (CPU or GPU) on which the model is loaded.
        name (str): The name of the likelihood function.

    Methods:
        to(device): Moves the model to the specified device.
        load_state_dict(state_dict): Loads the model state from a state dictionary.
        state_dict(): Returns the model state dictionary.
        fit(dataset, n_epochs, batch_size, num_workers, update_fn, verbose): Trains the model on the given dataset.
        predict(dataset, batch_size, num_workers, verbose): Performs inference on the given dataset.
        __call__(*args, **kwargs): Calls the predict method.

    """

    def __init__(self, sde, 
                 optimizer=functools.partial(
                    optim.Adam,
                    lr=5e-5,
                    betas=(0.9, 0.999),
                    eps=1e-8,
                    weight_decay=0,
                 ), 
                 model=None, 
                 feat_dim=None,
                 ):
        self.model = model
        if model is None:
            assert feat_dim is not None, "feat_dim must be provided if model is None"
            self.model = SimpleMLP(feat_dim)
        self.sde = sde
        self.optimizer = optimizer(self.model.parameters())
        self.device = "cpu"
        self.name = f"{self.sde.__class__.__name__}_{self.model.__class__.__name__}"

    def to(self, device):
        """Moves the model to the specified device.

        Args:
            device (str): The device to which the model should be moved (cpu or cuda).

        Returns:
            self: The Likelihood object.

        """
        self.model.to(device)
        self.device = device
        return self

    def load_state_dict(self, state_dict):
        """Loads the model state from a state dictionary.

        Args:
            state_dict (dict): The state dictionary containing the model state.

        """
        self.model.load_state_dict(state_dict)

    def state_dict(self):
        """Returns the model state dictionary.

        Returns:
            dict: The model state dictionary.

        """
        return self.model.state_dict()

    def fit(self, dataset, n_epochs, batch_size, 
            num_workers=0,
            update_fn=None, 
            verbose=True,
            collate_fn=None,
            ):
        """Trains the model on the given dataset.

        Args:
            dataset (object): The dataset object containing the training data.
            n_epochs (int): The number of epochs to train the model.
            batch_size (int): The batch size for training.
            num_workers (int): The number of worker processes for data loading. Default is 0.
            update_fn (object): The update function for updating the model parameters. If None, a default update function is used.
            verbose (bool): Whether to print training progress. Default is True.

        Returns:
            dict: A dictionary containing the training loss and other metrics.

        """
        if update_fn is None:
            update_fn = losses.SDE_BF16(
                sde=self.sde,
                model=self.model,
                optimizer=self.optimizer,
            )
        else:
            update_fn = update_fn(sde=self.sde, model=self.model, optimizer=self.optimizer)
        
        if collate_fn is None and getattr(dataset, 'collate_fn', None) is not None:
            collate_fn = dataset.collate_fn

        return train.train(dataset, self.model, update_fn, n_epochs, batch_size, self.device, num_workers, verbose=verbose, collate_fn=collate_fn)

    def predict(self, dataset, batch_size, num_workers=0, verbose=True, collate_fn=None):
        """Performs inference on the given dataset.

        Args:
            dataset (object): The dataset object containing the test data.
            batch_size (int): The batch size for inference.
            num_workers (int): The number of worker processes for data loading. Default is 0.
            verbose (bool): Whether to print inference progress. Default is True.

        Returns:
            dict: A dictionary containing the likelihood scores for the test data.

        """
        likelihood_fn = ood_utils.get_likelihood_fn(self.sde)
        if collate_fn is None and getattr(dataset, 'collate_fn', None) is not None:
            collate_fn = dataset.collate_fn
        return train.inference(dataset, self.model, likelihood_fn, batch_size, self.device, num_workers, verbose=verbose, collate_fn=collate_fn)
    
    def __call__(self, *args, **kwargs):
        """Calls the predict method.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: A dictionary containing the likelihood scores.

        """
        return self.predict(*args, **kwargs)
    
def VESDE_RDM(feat_dim):
    """Creates a Likelihood object for Variational Ensemble SDE with Dependency Detection Model.

    Args:
        feat_dim (int): The feature dimension of the model.

    Returns:
        Likelihood: The Likelihood object.

    """
    return Likelihood(VESDE(sigma_min=0.05, sigma_max=30, N=1000), feat_dim=feat_dim)

def SubSDE_RDM(feat_dim):
    """Creates a Likelihood object for Sub-Variational Poisson SDE with Dependency Detection Model.

    Args:
        feat_dim (int): The feature dimension of the model.

    Returns:
        Likelihood: The Likelihood object.

    """
    return Likelihood(subVPSDE(beta_min=0.5, beta_max=15, N=1000), feat_dim=feat_dim)

def VPSDE_RDM(feat_dim):
    """Creates a Likelihood object for Variational Poisson SDE with Dependency Detection Model.

    Args:
        feat_dim (int): The feature dimension of the model.

    Returns:
        Likelihood: The Likelihood object.

    """
    return Likelihood(VPSDE(beta_min=0.5, beta_max=15, N=1000),feat_dim=feat_dim)
