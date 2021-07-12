import json
import os
import sys
from typing import Any, Dict, Optional

from eth_typing import ChecksumAddress
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import Contract


def load_contract_interface(file_name):
    return _load_json_file(_abi_file_path(file_name))


def _abi_file_path(file):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file))


def _load_json_file(path):
    with open(path) as f:
        return json.load(f)


current_module = sys.modules[__name__]

"""
Safe Addresses. Should be the same for every chain. Check:
https://github.com/gnosis/safe-contracts/blob/development/zos.mainnet.json
https://github.com/gnosis/safe-contracts/blob/development/zos.rinkeby.json

GnosisSafeV1.1.1: 0x34CfAC646f301356fAa8B21e94227e3583Fe3F5F
GnosisSafeV1.1.0: 0xaE32496491b53841efb51829d6f886387708F99B
GnosisSafeV1.0.0: 0xb6029EA3B2c51D09a50B53CA8012FeEB05bDa35A

Factories
ProxyFactoryV1.1.0: 0x50e55Af101C777bA7A1d560a774A82eF002ced9F
ProxyFactoryV1.0.0: 0x12302fE9c02ff50939BaAaaf415fc226C078613C

Libraries
CreateAndAddModules: 0x1a56aE690ab0818aF5cA349b7D21f1d7e76a3d36
MultiSend: 0xD4B7B161E4779629C2717385114Bf78D612aEa72
"""

contracts = {
    'safe': 'GnosisSafe_V1_1_1.json',
    'safe_V1_3_0': 'GnosisSafe_V1_3_0.json',
    'safe_V1_0_0': 'GnosisSafe_V1_0_0.json',
    'safe_V0_0_1': 'GnosisSafe_V0_0_1.json',
    'erc20': 'ERC20.json',
    'erc721': 'ERC721.json',
    'example_erc20': 'ERC20TestToken.json',
    'delegate_constructor_proxy': 'DelegateConstructorProxy.json',
    'multi_send': 'MultiSend.json',
    'paying_proxy': 'PayingProxy.json',
    'proxy_factory': 'ProxyFactory_V1_3_0.json',
    'proxy_factory_V1_1_1': 'ProxyFactory_V1_1_1.json',
    'proxy_factory_V1_0_0': 'ProxyFactory_V1_0_0.json',
    'proxy': 'Proxy_V1_1_1.json',
    'uniswap_exchange': 'uniswap_exchange.json',
    'uniswap_factory': 'uniswap_factory.json',
    'uniswap_v2_factory': 'uniswap_v2_factory.json',
    'uniswap_v2_pair': 'uniswap_v2_pair.json',
    'uniswap_v2_router': 'uniswap_v2_router.json',  # Router02
    'kyber_network_proxy': 'kyber_network_proxy.json',
    'cpk_factory': 'CPKFactory.json',
}


def generate_contract_fn(contract: Dict[str, Any]):
    """
    Dynamically generate functions to work with the contracts
    :param contract:
    :return:
    """
    def fn(w3: Web3, address: Optional[ChecksumAddress] = None):
        return w3.eth.contract(address=address,
                               abi=contract['abi'],
                               bytecode=contract.get('bytecode'))
    return fn


# Anotate functions that will be generated later with `setattr` so typing does not complains
def get_safe_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_safe_V1_3_0_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_safe_V1_0_0_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_safe_V0_0_1_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_erc20_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_erc721_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_example_erc20_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_delegate_constructor_proxy_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_multi_send_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_paying_proxy_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_proxy_factory_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_proxy_factory_V1_1_1_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_proxy_factory_V1_0_0_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_proxy_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_uniswap_exchange_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_uniswap_factory_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_uniswap_v2_factory_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_uniswap_v2_pair_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_uniswap_v2_router_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_kyber_network_proxy_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_cpk_factory_contract(w3: Web3, address: Optional[str] = None) -> Contract:
    pass


def get_paying_proxy_deployed_bytecode() -> bytes:
    return HexBytes(load_contract_interface('PayingProxy.json')['deployedBytecode'])


def get_proxy_1_0_0_deployed_bytecode() -> bytes:
    return HexBytes(load_contract_interface('Proxy_V1_0_0.json')['deployedBytecode'])


for contract_name, json_contract_filename in contracts.items():
    fn_name = 'get_{}_contract'.format(contract_name)
    contract_dict = load_contract_interface(json_contract_filename)
    setattr(current_module, fn_name, generate_contract_fn(contract_dict))
