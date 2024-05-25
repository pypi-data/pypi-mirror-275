#src/story_protcol_python_sdk/resources/IPAsset.py

from web3 import Web3

from story_protocol_python_sdk.abi.IPAssetRegistry.IPAssetRegistry_client import IPAssetRegistryClient
from story_protocol_python_sdk.abi.LicensingModule.LicensingModule_client import LicensingModuleClient
from story_protocol_python_sdk.abi.LicenseToken.LicenseToken_client import LicenseTokenClient
from story_protocol_python_sdk.abi.LicenseRegistry.LicenseRegistry_client import LicenseRegistryClient

from story_protocol_python_sdk.utils.transaction_utils import build_and_send_transaction

class IPAsset:
    def __init__(self, web3: Web3, account, chain_id):
        self.web3 = web3
        self.account = account
        self.chain_id = chain_id

        self.ip_asset_registry_client = IPAssetRegistryClient(web3)
        self.licensing_module_client = LicensingModuleClient(web3)
        self.license_token_client = LicenseTokenClient(web3)
        self.license_registry_client = LicenseRegistryClient(web3)

    def _get_ip_id(self, token_contract, token_id):
        return self.ip_asset_registry_client.ipId(
            self.chain_id, 
            token_contract,
            token_id
        )

    def _is_registered(self, ip_id):
        return self.ip_asset_registry_client.isRegistered(ip_id)

    def register(self, token_contract, token_id, tx_options=None):
        try:
            # Check if the token is already registered
            ip_id = self._get_ip_id(token_contract, token_id)
            if self._is_registered(ip_id):
                return {
                    'txHash': None,
                    'ipId': ip_id
                }

            response = build_and_send_transaction(
                self.web3,
                self.account,
                self.ip_asset_registry_client.build_register_transaction,
                self.chain_id,
                token_contract,
                token_id,
                tx_options=tx_options
            )

            return {
                'txHash': response['txHash'],
                'ipId': ip_id
            }

        except Exception as e:
            raise e

    def registerDerivative(self, child_ip_id, parent_ip_ids, license_terms_ids, license_template, tx_options=None):
        try:
            # Check if the child IP is registered
            if not self._is_registered(child_ip_id):
                raise ValueError(f"The child IP with id {child_ip_id} is not registered.")

            # Check if all parent IPs are registered
            for parent_id in parent_ip_ids:
                if not self._is_registered(parent_id):
                    raise ValueError(f"The parent IP with id {parent_id} is not registered.")

            # Check if parent IP IDs and license terms IDs are provided in pairs and that there are 1 or 2 parents
            if len(parent_ip_ids) != len(license_terms_ids):
                raise ValueError("Parent IP IDs and license terms IDs must match in quantity.")
            if len(parent_ip_ids) not in [1, 2]:
                raise ValueError("There must be 1 or 2 parent IP IDs.")

            # Check if license terms are attached to parent IPs
            for parent_id, terms_id in zip(parent_ip_ids, license_terms_ids):
                if not self.license_registry_client.hasIpAttachedLicenseTerms(parent_id, license_template, terms_id):
                    raise ValueError(f"License terms id {terms_id} must be attached to the parent ipId {parent_id} before registering derivative.")

            zero_address = self.web3.constants.ADDRESS_ZERO
            response = build_and_send_transaction(
                self.web3,
                self.account,
                self.licensing_module_client.build_registerDerivative_transaction,
                child_ip_id,
                parent_ip_ids,
                license_terms_ids,
                license_template,
                zero_address,
                tx_options=tx_options
            )

            return {
                'txHash': response['txHash']
            }

        except Exception as e:
            raise e
        
    def registerDerivativeWithLicenseTokens(self, child_ip_id, license_token_ids, tx_options=None):
        try:
            # Check if the child IP is registered
            if not self._is_registered(child_ip_id):
                raise ValueError(f"The child IP with id {child_ip_id} is not registered.")

            # Ensure license token IDs are owned by the caller
            for token_id in license_token_ids:
                token_owner = self.license_token_client.ownerOf(token_id)
                if token_owner.lower() != self.account.address.lower():
                    raise ValueError(f"License token id {token_id} must be owned by the caller.")

            zero_address = self.web3.constants.ADDRESS_ZERO
            response = build_and_send_transaction(
                self.web3,
                self.account,
                self.licensing_module_client.build_registerDerivativeWithLicenseTokens_transaction,
                child_ip_id,
                license_token_ids,
                zero_address,
                tx_options=tx_options
            )

            return {
                'txHash': response['txHash']
            }

        except Exception as e:
            raise e
