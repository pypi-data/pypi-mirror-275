"""Generic class for deep reconstruction (a.k.a iCNN reconstruction)."""


from typing import Callable, Dict, Optional

import torch
import torch.optim as optim


FeatureSetType = Dict[str, torch.Tensor]


class BaseEncoder(object):
    """Base encoder class."""
    def encode(self, x: torch.Tensor) -> FeatureSetType:
        raise NotImplementedError


class BaseGenerator(object):
    """Base generator class."""
    def generate(self, x: torch.Tesnro) -> torch.Tensor:
        raise NotImplementedError


class BaseLoss(object):
    """Base"""
    def __init__(self, loss_func: Callable):
        self._loss_func = loss_func

    def calc_loss(self, xs: FeatureSetType, ys: FeatureSetType) -> torch.Tensor:
        layers = xs.keys()
        loss = 0
        for layer in layers:
            loss += self._loss_func(x[layer], y[layer])
        return loss


class NullGenerator(BaseGenerator):
    def generate(self, x: torch.Tensor) -> torch.Tensor:
        return x


class DeepRecon(object):
    def __init__(
            self,
            encoder: BaseEncoder,
            generator: Optional[BaseGenerator] = None,
            loss: Optional[BaseLoss] = None,
            optimizer: Optional[torch.optim.optimizer.Optimizer] = None,
            latent_initializer: Optional[Callable] = None,
            n_iter: Optional[int] = 100,
            callbacks: Optional[str, Callable] = None,
    ) -> None:
        self._encoder = encoder
        self._generator = generator
        self._latent_initializer
        self._optimizer = optimizer
        self._loss = loss
        self._n_iter = n_iter
        self._callbacks = {}

        if self._generator is None:
            self._generator = NullGenerator()
        if self._loss is None:
            self._loss = BaseLoss(loss_func=torch.nn.MSELoss(reduction='sum'))
        if self._optimizer is None:
            self._loss = optim.SGD
        if self._latent_initializer is None:
            self._latent_initializer = DefaultInitializer()
        if self._callbacks is None:
            self._callbacks = {}

    def __call__(self, features: Dict[str, np.ndarray]):
        return self.reconstruct(features)

    def _trigger(self, name: str, *args, **kwargs):
        """Trigger callback function."""
        return self._callbacks[name](*args, **kwargs)

    def reconstruct(self, features: Dict[str, np.ndarray]):
        # features を Dict[str, np.ndarray] から Dict[str, torch.Tensor] に変換

        self._trigger("OnReconstructionBegin")

        z: torch.Tensor  # Latent vector to be optimized

        # Initialize latent vector and y
        z = self._latent_initializer()
        x = self._generator.generate(z)

        # Initialize optimizer
        op = self._optimizer()

        # Save initial z and x

        loss_history = []
        for i in range(self._n_iter):

            self._trigger("OnIterationBegin")

            self._encoder.zero_grad()
            self._generator.zero_grad()
            op.zero_grad()

            _feats = self._encoder(x)
            _loss = self._loss_func(features, _feats)
            loss_history.append(_loss)

            _loss.backward()
            op.step()

            x = self._generator.generate(z)

            # Save snapshot
            _x = x.cpu().detach().numpy()
            _z = z.cpu().deatch().numpy()

            self._trigger("OnIterationEnd")

        # Save final results
        x = x.cpu().detach().numpy()
        z = z.cpu().deatch().numpy()

        self._trigger("OnReconstructionEnd")

        return x
