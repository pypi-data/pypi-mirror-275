#src/story_protcol_python_sdk/resources/License.py

from web3 import Web3

from story_protocol_python_sdk.abi.PILicenseTemplate.PILicenseTemplate_client import PILicenseTemplateClient
from story_protocol_python_sdk.abi.LicenseRegistry.LicenseRegistry_client import LicenseRegistryClient
from story_protocol_python_sdk.abi.LicensingModule.LicensingModule_client import LicensingModuleClient
from story_protocol_python_sdk.abi.IPAssetRegistry.IPAssetRegistry_client import IPAssetRegistryClient

from story_protocol_python_sdk.utils.license_terms import get_license_term_by_type, PIL_TYPE
from story_protocol_python_sdk.utils.transaction_utils import build_and_send_transaction

class License:
    def __init__(self, web3: Web3, account, chain_id):
        self.web3 = web3
        self.account = account
        self.chain_id = chain_id

        self.license_template_client = PILicenseTemplateClient(web3)
        self.license_registry_client = LicenseRegistryClient(web3)
        self.licensing_module_client  = LicensingModuleClient(web3)
        self.ip_asset_registry_client = IPAssetRegistryClient(web3)

    def _get_license_terms_id(self, license_terms):
        return self.license_template_client.getLicenseTermsId(license_terms)

    def registerNonComSocialRemixingPIL(self, tx_options=None):
        try:
            # Get the license terms for non-commercial social remixing PIL
            license_terms = get_license_term_by_type(PIL_TYPE['NON_COMMERCIAL_REMIX'])

            # Check if the license terms are already registered
            license_terms_id = self._get_license_terms_id(license_terms)
            if (license_terms_id is not None) and (license_terms_id != 0):
                return {'licenseTermsId': license_terms_id}

            # Build and send the transaction
            response = build_and_send_transaction(
                self.web3,
                self.account,
                self.license_template_client.build_registerLicenseTerms_transaction,
                license_terms,
                tx_options=tx_options
            )

            # Parse the event logs for LicenseTermsRegistered
            target_logs = self._parse_tx_license_terms_registered_event(response['txReceipt'])
            return {
                'txHash': response['txHash'],
                'licenseTermsId': target_logs
            }

        except Exception as e:
            raise e
        
    def registerCommercialUsePIL(self, minting_fee, currency, royalty_policy, tx_options=None):
        try:
            # Construct complete license terms
            complete_license_terms = get_license_term_by_type(PIL_TYPE['COMMERCIAL_USE'], {
                'mintingFee': minting_fee,
                'currency': currency,
                'royaltyPolicy': royalty_policy,
            })

            # Check if the license terms are already registered
            license_terms_id = self._get_license_terms_id(complete_license_terms)
            if (license_terms_id is not None) and (license_terms_id != 0):
                return {'licenseTermsId': license_terms_id}

            # Build and send the transaction
            response = build_and_send_transaction(
                self.web3,
                self.account,
                self.license_template_client.build_registerLicenseTerms_transaction,
                complete_license_terms,
                tx_options=tx_options
            )

            # Parse the event logs for LicenseTermsRegistered
            if not response['txReceipt'].logs:
                return None

            target_logs = self._parse_tx_license_terms_registered_event(response['txReceipt'])
            return {
                'txHash': response['txHash'],
                'licenseTermsId': target_logs
            }

        except Exception as e:
            raise e

    def registerCommercialRemixPIL(self, minting_fee, currency, commercial_rev_share, royalty_policy, tx_options=None):
        try:
            # Construct complete license terms
            complete_license_terms = get_license_term_by_type(PIL_TYPE['COMMERCIAL_REMIX'], {
                'mintingFee': minting_fee,
                'currency': currency,
                'commercialRevShare': commercial_rev_share,
                'royaltyPolicy': royalty_policy,
            })
            # Check if the license terms are already registered
            license_terms_id = self._get_license_terms_id(complete_license_terms)
            if license_terms_id and license_terms_id != 0:
                return {'licenseTermsId': license_terms_id}

            # Build and send the transaction
            response = build_and_send_transaction(
                self.web3,
                self.account,
                self.license_template_client.build_registerLicenseTerms_transaction,
                complete_license_terms,
                tx_options=tx_options
            )

            # Parse the event logs for LicenseTermsRegistered
            if not response['txReceipt'].logs:
                return None

            target_logs = self._parse_tx_license_terms_registered_event(response['txReceipt'])
            return {
                'txHash': response['txHash'],
                'licenseTermsId': target_logs
            }

        except Exception as e:
            raise e

    def _parse_tx_license_terms_registered_event(self, tx_receipt):
        event_signature = self.web3.keccak(text="LicenseTermsRegistered(uint256,address,bytes)").hex()

        for log in tx_receipt['logs']:
            if log['topics'][0].hex() == event_signature:
                return int(log['topics'][1].hex(), 16)

        return None
    
    def attachLicenseTerms(self, ip_id, license_template, license_terms_id, tx_options=None):
        try:
            # Validate the license template address
            if not Web3.is_address(license_template):
                raise ValueError(f'Address "{license_template}" is invalid.')

            # Check if the IP is registered
            is_registered = self.ip_asset_registry_client.isRegistered(ip_id)
            if not is_registered:
                raise ValueError(f"The IP with id {ip_id} is not registered.")

            # Check if the license terms exist
            is_existed = self.license_registry_client.exists(license_template, license_terms_id)
            if not is_existed:
                raise ValueError(f"License terms id {license_terms_id} do not exist.")

            # Check if the license terms are already attached to the IP
            is_attached_license_terms = self.license_registry_client.hasIpAttachedLicenseTerms(ip_id, license_template, license_terms_id)
            if is_attached_license_terms:
                raise ValueError(f"License terms id {license_terms_id} is already attached to the IP with id {ip_id}.")

            # Build and send the transaction
            response = build_and_send_transaction(
                self.web3,
                self.account,
                self.licensing_module_client.build_attachLicenseTerms_transaction,
                ip_id,
                license_template,
                license_terms_id,
                tx_options=tx_options
            )

            return {'txHash': response['txHash']}
        
        except Exception as e:
            raise e
        
    def mintLicenseTokens(self, licensor_ip_id, license_template, license_terms_id, amount, receiver, tx_options=None):
        try:
            # Validate the license template address
            if not Web3.is_address(license_template):
                raise ValueError(f'Address "{license_template}" is invalid.')
            
            # Validate the license template address
            if not Web3.is_address(receiver):
                raise ValueError(f'Address "{receiver}" is invalid.')

            # Check if the licensor IP is registered
            is_registered = self.ip_asset_registry_client.isRegistered(licensor_ip_id)
            if not is_registered:
                raise ValueError(f"The licensor IP with id {licensor_ip_id} is not registered.")

            # Check if the license terms exist
            is_existed = self.license_template_client.exists(license_terms_id)
            if not is_existed:
                raise ValueError(f"License terms id {license_terms_id} do not exist.")

            # Check if the license terms are attached to the IP
            is_attached_license_terms = self.license_registry_client.hasIpAttachedLicenseTerms(licensor_ip_id, license_template, license_terms_id)
            if not is_attached_license_terms:
                raise ValueError(f"License terms id {license_terms_id} is not attached to the IP with id {licensor_ip_id}.")

            # Build and send the transaction
            response = build_and_send_transaction(
                self.web3,
                self.account,
                self.licensing_module_client.build_mintLicenseTokens_transaction,
                licensor_ip_id,
                license_template,
                license_terms_id,
                amount,
                receiver,
                self.web3.constants.ADDRESS_ZERO,
                tx_options=tx_options
            )

            # Parse the event logs for LicenseTokensMinted
            target_logs = self._parse_tx_license_tokens_minted_event(response['txReceipt'])

            return {
                'txHash': response['txHash'],
                'licenseTokenIds': target_logs
            }

        except Exception as e:
            raise e

    def _parse_tx_license_tokens_minted_event(self, tx_receipt):
        event_signature = self.web3.keccak(text="LicenseTokenMinted(address,address,uint256)").hex()
        token_ids = []

        for log in tx_receipt['logs']:
            if log['topics'][0].hex() == event_signature:
                start_license_token_id = int(log['topics'][3].hex(), 16)
                token_ids.append(start_license_token_id)

        return token_ids if token_ids else None
    
    def getLicenseTerms(self, selectedLicenseTermsId):
        try:
            return self.license_template_client.getLicenseTerms(selectedLicenseTermsId)
        except Exception as e:
            raise ValueError(f"Failed to get license terms: {str(e)}")