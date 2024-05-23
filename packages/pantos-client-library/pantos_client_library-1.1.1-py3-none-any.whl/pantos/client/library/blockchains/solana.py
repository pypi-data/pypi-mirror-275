"""Module for Solana-specific clients and errors.

"""
import typing

from pantos.common.blockchains.base import Blockchain
from pantos.common.entities import ServiceNodeBid
from pantos.common.types import BlockchainAddress

from pantos.client.library.blockchains.base import BlockchainClient
from pantos.client.library.blockchains.base import BlockchainClientError


class SolanaClientError(BlockchainClientError):
    """Exception class for all Solana client errors.

    """
    pass


class SolanaClient(BlockchainClient):
    """Solana-specific blockchain client.

    """
    def compute_transfer_signature(
            self, request: BlockchainClient.ComputeTransferSignatureRequest) \
            -> BlockchainClient.ComputeTransferSignatureResponse:
        # Docstring inherited
        raise NotImplementedError

    def compute_transfer_from_signature(
            self,
            request: BlockchainClient.ComputeTransferFromSignatureRequest) \
            -> BlockchainClient.ComputeTransferFromSignatureResponse:
        # Docstring inherited
        raise NotImplementedError

    def is_valid_recipient_address(self, recipient_address: str) -> bool:
        # Docstring inherited
        raise NotImplementedError

    @classmethod
    def get_blockchain(cls) -> Blockchain:
        # Docstring inherited
        return Blockchain.SOLANA

    @classmethod
    def get_error_class(cls) -> type[BlockchainClientError]:
        # Docstring inherited
        return SolanaClientError

    def read_external_token_address(
            self, token_address: BlockchainAddress,
            destination_blockchain: Blockchain) -> BlockchainAddress:
        # Docstring inherited
        raise NotImplementedError

    def read_service_node_addresses(self) -> typing.List[BlockchainAddress]:
        # Docstring inherited
        raise NotImplementedError

    def read_service_node_bid(self, service_node_address: BlockchainAddress,
                              bid_id: int) -> ServiceNodeBid:
        # Docstring inherited
        raise NotImplementedError

    def read_service_node_bids(
            self, service_node_address: BlockchainAddress,
            destination_blockchain: Blockchain) -> typing.List[ServiceNodeBid]:
        # Docstring inherited
        raise NotImplementedError

    def read_service_node_url(self,
                              service_node_address: BlockchainAddress) -> str:
        # Docstring inherited
        raise NotImplementedError

    def read_token_decimals(self, token_address: BlockchainAddress) -> int:
        # Docstring inherited
        raise NotImplementedError
