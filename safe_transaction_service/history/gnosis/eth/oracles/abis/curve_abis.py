curve_address_provider_abi = [{'name': 'NewAddressIdentifier',
                               'inputs': [{'type': 'uint256', 'name': 'id', 'indexed': True},
                                          {'type': 'address', 'name': 'addr', 'indexed': False},
                                          {'type': 'string', 'name': 'description', 'indexed': False}],
                               'anonymous': False,
                               'type': 'event'},
                              {'name': 'AddressModified',
                               'inputs': [{'type': 'uint256', 'name': 'id', 'indexed': True},
                                          {'type': 'address', 'name': 'new_address', 'indexed': False},
                                          {'type': 'uint256', 'name': 'version', 'indexed': False}],
                               'anonymous': False,
                               'type': 'event'},
                              {'name': 'CommitNewAdmin',
                               'inputs': [{'type': 'uint256', 'name': 'deadline', 'indexed': True},
                                          {'type': 'address', 'name': 'admin', 'indexed': True}],
                               'anonymous': False,
                               'type': 'event'},
                              {'name': 'NewAdmin',
                               'inputs': [{'type': 'address', 'name': 'admin', 'indexed': True}],
                               'anonymous': False,
                               'type': 'event'},
                              {'outputs': [],
                               'inputs': [{'type': 'address', 'name': '_admin'}],
                               'stateMutability': 'nonpayable',
                               'type': 'constructor'},
                              {'name': 'get_registry',
                               'outputs': [{'type': 'address', 'name': ''}],
                               'inputs': [],
                               'stateMutability': 'view',
                               'type': 'function',
                               'gas': 1061},
                              {'name': 'max_id',
                               'outputs': [{'type': 'uint256', 'name': ''}],
                               'inputs': [],
                               'stateMutability': 'view',
                               'type': 'function',
                               'gas': 1258},
                              {'name': 'get_address',
                               'outputs': [{'type': 'address', 'name': ''}],
                               'inputs': [{'type': 'uint256', 'name': '_id'}],
                               'stateMutability': 'view',
                               'type': 'function',
                               'gas': 1308},
                              {'name': 'add_new_id',
                               'outputs': [{'type': 'uint256', 'name': ''}],
                               'inputs': [{'type': 'address', 'name': '_address'},
                                          {'type': 'string', 'name': '_description'}],
                               'stateMutability': 'nonpayable',
                               'type': 'function',
                               'gas': 291275},
                              {'name': 'set_address',
                               'outputs': [{'type': 'bool', 'name': ''}],
                               'inputs': [{'type': 'uint256', 'name': '_id'},
                                          {'type': 'address', 'name': '_address'}],
                               'stateMutability': 'nonpayable',
                               'type': 'function',
                               'gas': 182430},
                              {'name': 'unset_address',
                               'outputs': [{'type': 'bool', 'name': ''}],
                               'inputs': [{'type': 'uint256', 'name': '_id'}],
                               'stateMutability': 'nonpayable',
                               'type': 'function',
                               'gas': 101348},
                              {'name': 'commit_transfer_ownership',
                               'outputs': [{'type': 'bool', 'name': ''}],
                               'inputs': [{'type': 'address', 'name': '_new_admin'}],
                               'stateMutability': 'nonpayable',
                               'type': 'function',
                               'gas': 74048},
                              {'name': 'apply_transfer_ownership',
                               'outputs': [{'type': 'bool', 'name': ''}],
                               'inputs': [],
                               'stateMutability': 'nonpayable',
                               'type': 'function',
                               'gas': 60125},
                              {'name': 'revert_transfer_ownership',
                               'outputs': [{'type': 'bool', 'name': ''}],
                               'inputs': [],
                               'stateMutability': 'nonpayable',
                               'type': 'function',
                               'gas': 21400},
                              {'name': 'admin',
                               'outputs': [{'type': 'address', 'name': ''}],
                               'inputs': [],
                               'stateMutability': 'view',
                               'type': 'function',
                               'gas': 1331},
                              {'name': 'transfer_ownership_deadline',
                               'outputs': [{'type': 'uint256', 'name': ''}],
                               'inputs': [],
                               'stateMutability': 'view',
                               'type': 'function',
                               'gas': 1361},
                              {'name': 'future_admin',
                               'outputs': [{'type': 'address', 'name': ''}],
                               'inputs': [],
                               'stateMutability': 'view',
                               'type': 'function',
                               'gas': 1391},
                              {'name': 'get_id_info',
                               'outputs': [{'type': 'address', 'name': 'addr'},
                                           {'type': 'bool', 'name': 'is_active'},
                                           {'type': 'uint256', 'name': 'version'},
                                           {'type': 'uint256', 'name': 'last_modified'},
                                           {'type': 'string', 'name': 'description'}],
                               'inputs': [{'type': 'uint256', 'name': 'arg0'}],
                               'stateMutability': 'view',
                               'type': 'function',
                               'gas': 12168}]

curve_registry_abi = [{'name': 'PoolAdded',
                       'inputs': [{'type': 'address', 'name': 'pool', 'indexed': True},
                                  {'type': 'bytes', 'name': 'rate_method_id', 'indexed': False}],
                       'anonymous': False,
                       'type': 'event'},
                      {'name': 'PoolRemoved',
                       'inputs': [{'type': 'address', 'name': 'pool', 'indexed': True}],
                       'anonymous': False,
                       'type': 'event'},
                      {'outputs': [],
                       'inputs': [{'type': 'address', 'name': '_address_provider'},
                                  {'type': 'address', 'name': '_gauge_controller'}],
                       'stateMutability': 'nonpayable',
                       'type': 'constructor'},
                      {'name': 'find_pool_for_coins',
                       'outputs': [{'type': 'address', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_from'},
                                  {'type': 'address', 'name': '_to'}],
                       'stateMutability': 'view',
                       'type': 'function'},
                      {'name': 'find_pool_for_coins',
                       'outputs': [{'type': 'address', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_from'},
                                  {'type': 'address', 'name': '_to'},
                                  {'type': 'uint256', 'name': 'i'}],
                       'stateMutability': 'view',
                       'type': 'function'},
                      {'name': 'get_n_coins',
                       'outputs': [{'type': 'uint256[2]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 1704},
                      {'name': 'get_coins',
                       'outputs': [{'type': 'address[8]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 12285},
                      {'name': 'get_underlying_coins',
                       'outputs': [{'type': 'address[8]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 12347},
                      {'name': 'get_decimals',
                       'outputs': [{'type': 'uint256[8]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 8199},
                      {'name': 'get_underlying_decimals',
                       'outputs': [{'type': 'uint256[8]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 8261},
                      {'name': 'get_rates',
                       'outputs': [{'type': 'uint256[8]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 34780},
                      {'name': 'get_gauges',
                       'outputs': [{'type': 'address[10]', 'name': ''},
                                   {'type': 'int128[10]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 20310},
                      {'name': 'get_balances',
                       'outputs': [{'type': 'uint256[8]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 16818},
                      {'name': 'get_underlying_balances',
                       'outputs': [{'type': 'uint256[8]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 158953},
                      {'name': 'get_virtual_price_from_lp_token',
                       'outputs': [{'type': 'uint256', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_token'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 2080},
                      {'name': 'get_A',
                       'outputs': [{'type': 'uint256', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 1198},
                      {'name': 'get_parameters',
                       'outputs': [{'type': 'uint256', 'name': 'A'},
                                   {'type': 'uint256', 'name': 'future_A'},
                                   {'type': 'uint256', 'name': 'fee'},
                                   {'type': 'uint256', 'name': 'admin_fee'},
                                   {'type': 'uint256', 'name': 'future_fee'},
                                   {'type': 'uint256', 'name': 'future_admin_fee'},
                                   {'type': 'address', 'name': 'future_owner'},
                                   {'type': 'uint256', 'name': 'initial_A'},
                                   {'type': 'uint256', 'name': 'initial_A_time'},
                                   {'type': 'uint256', 'name': 'future_A_time'}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 6458},
                      {'name': 'get_fees',
                       'outputs': [{'type': 'uint256[2]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 1603},
                      {'name': 'get_admin_balances',
                       'outputs': [{'type': 'uint256[8]', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 36719},
                      {'name': 'get_coin_indices',
                       'outputs': [{'type': 'int128', 'name': ''},
                                   {'type': 'int128', 'name': ''},
                                   {'type': 'bool', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'},
                                  {'type': 'address', 'name': '_from'},
                                  {'type': 'address', 'name': '_to'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 27456},
                      {'name': 'estimate_gas_used',
                       'outputs': [{'type': 'uint256', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': '_pool'},
                                  {'type': 'address', 'name': '_from'},
                                  {'type': 'address', 'name': '_to'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 32329},
                      {'name': 'add_pool',
                       'outputs': [],
                       'inputs': [{'type': 'address', 'name': '_pool'},
                                  {'type': 'uint256', 'name': '_n_coins'},
                                  {'type': 'address', 'name': '_lp_token'},
                                  {'type': 'bytes32', 'name': '_rate_method_id'},
                                  {'type': 'uint256', 'name': '_decimals'},
                                  {'type': 'uint256', 'name': '_underlying_decimals'},
                                  {'type': 'bool', 'name': '_has_initial_A'},
                                  {'type': 'bool', 'name': '_is_v1'}],
                       'stateMutability': 'nonpayable',
                       'type': 'function',
                       'gas': 10196577},
                      {'name': 'add_pool_without_underlying',
                       'outputs': [],
                       'inputs': [{'type': 'address', 'name': '_pool'},
                                  {'type': 'uint256', 'name': '_n_coins'},
                                  {'type': 'address', 'name': '_lp_token'},
                                  {'type': 'bytes32', 'name': '_rate_method_id'},
                                  {'type': 'uint256', 'name': '_decimals'},
                                  {'type': 'uint256', 'name': '_use_rates'},
                                  {'type': 'bool', 'name': '_has_initial_A'},
                                  {'type': 'bool', 'name': '_is_v1'}],
                       'stateMutability': 'nonpayable',
                       'type': 'function',
                       'gas': 5590664},
                      {'name': 'add_metapool',
                       'outputs': [],
                       'inputs': [{'type': 'address', 'name': '_pool'},
                                  {'type': 'uint256', 'name': '_n_coins'},
                                  {'type': 'address', 'name': '_lp_token'},
                                  {'type': 'uint256', 'name': '_decimals'}],
                       'stateMutability': 'nonpayable',
                       'type': 'function',
                       'gas': 10226976},
                      {'name': 'remove_pool',
                       'outputs': [],
                       'inputs': [{'type': 'address', 'name': '_pool'}],
                       'stateMutability': 'nonpayable',
                       'type': 'function',
                       'gas': 779646579509},
                      {'name': 'set_pool_gas_estimates',
                       'outputs': [],
                       'inputs': [{'type': 'address[5]', 'name': '_addr'},
                                  {'type': 'uint256[2][5]', 'name': '_amount'}],
                       'stateMutability': 'nonpayable',
                       'type': 'function',
                       'gas': 355578},
                      {'name': 'set_coin_gas_estimates',
                       'outputs': [],
                       'inputs': [{'type': 'address[10]', 'name': '_addr'},
                                  {'type': 'uint256[10]', 'name': '_amount'}],
                       'stateMutability': 'nonpayable',
                       'type': 'function',
                       'gas': 357165},
                      {'name': 'set_gas_estimate_contract',
                       'outputs': [],
                       'inputs': [{'type': 'address', 'name': '_pool'},
                                  {'type': 'address', 'name': '_estimator'}],
                       'stateMutability': 'nonpayable',
                       'type': 'function',
                       'gas': 37747},
                      {'name': 'set_liquidity_gauges',
                       'outputs': [],
                       'inputs': [{'type': 'address', 'name': '_pool'},
                                  {'type': 'address[10]', 'name': '_liquidity_gauges'}],
                       'stateMutability': 'nonpayable',
                       'type': 'function',
                       'gas': 365793},
                      {'name': 'address_provider',
                       'outputs': [{'type': 'address', 'name': ''}],
                       'inputs': [],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 2111},
                      {'name': 'gauge_controller',
                       'outputs': [{'type': 'address', 'name': ''}],
                       'inputs': [],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 2141},
                      {'name': 'pool_list',
                       'outputs': [{'type': 'address', 'name': ''}],
                       'inputs': [{'type': 'uint256', 'name': 'arg0'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 2280},
                      {'name': 'pool_count',
                       'outputs': [{'type': 'uint256', 'name': ''}],
                       'inputs': [],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 2201},
                      {'name': 'get_pool_from_lp_token',
                       'outputs': [{'type': 'address', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': 'arg0'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 2446},
                      {'name': 'get_lp_token',
                       'outputs': [{'type': 'address', 'name': ''}],
                       'inputs': [{'type': 'address', 'name': 'arg0'}],
                       'stateMutability': 'view',
                       'type': 'function',
                       'gas': 2476}]

curve_pool_abi = [{'name': 'TokenExchange',
                   'inputs': [{'type': 'address', 'name': 'buyer', 'indexed': True},
                              {'type': 'int128', 'name': 'sold_id', 'indexed': False},
                              {'type': 'uint256', 'name': 'tokens_sold', 'indexed': False},
                              {'type': 'int128', 'name': 'bought_id', 'indexed': False},
                              {'type': 'uint256', 'name': 'tokens_bought', 'indexed': False}],
                   'anonymous': False,
                   'type': 'event'},
                  {'name': 'TokenExchangeUnderlying',
                   'inputs': [{'type': 'address', 'name': 'buyer', 'indexed': True},
                              {'type': 'int128', 'name': 'sold_id', 'indexed': False},
                              {'type': 'uint256', 'name': 'tokens_sold', 'indexed': False},
                              {'type': 'int128', 'name': 'bought_id', 'indexed': False},
                              {'type': 'uint256', 'name': 'tokens_bought', 'indexed': False}],
                   'anonymous': False,
                   'type': 'event'},
                  {'name': 'AddLiquidity',
                   'inputs': [{'type': 'address', 'name': 'provider', 'indexed': True},
                              {'type': 'uint256[4]', 'name': 'token_amounts', 'indexed': False},
                              {'type': 'uint256[4]', 'name': 'fees', 'indexed': False},
                              {'type': 'uint256', 'name': 'invariant', 'indexed': False},
                              {'type': 'uint256', 'name': 'token_supply', 'indexed': False}],
                   'anonymous': False,
                   'type': 'event'},
                  {'name': 'RemoveLiquidity',
                   'inputs': [{'type': 'address', 'name': 'provider', 'indexed': True},
                              {'type': 'uint256[4]', 'name': 'token_amounts', 'indexed': False},
                              {'type': 'uint256[4]', 'name': 'fees', 'indexed': False},
                              {'type': 'uint256', 'name': 'token_supply', 'indexed': False}],
                   'anonymous': False,
                   'type': 'event'},
                  {'name': 'RemoveLiquidityImbalance',
                   'inputs': [{'type': 'address', 'name': 'provider', 'indexed': True},
                              {'type': 'uint256[4]', 'name': 'token_amounts', 'indexed': False},
                              {'type': 'uint256[4]', 'name': 'fees', 'indexed': False},
                              {'type': 'uint256', 'name': 'invariant', 'indexed': False},
                              {'type': 'uint256', 'name': 'token_supply', 'indexed': False}],
                   'anonymous': False,
                   'type': 'event'},
                  {'name': 'CommitNewAdmin',
                   'inputs': [{'type': 'uint256',
                               'name': 'deadline',
                               'indexed': True,
                               'unit': 'sec'},
                              {'type': 'address', 'name': 'admin', 'indexed': True}],
                   'anonymous': False,
                   'type': 'event'},
                  {'name': 'NewAdmin',
                   'inputs': [{'type': 'address', 'name': 'admin', 'indexed': True}],
                   'anonymous': False,
                   'type': 'event'},
                  {'name': 'CommitNewParameters',
                   'inputs': [{'type': 'uint256',
                               'name': 'deadline',
                               'indexed': True,
                               'unit': 'sec'},
                              {'type': 'uint256', 'name': 'A', 'indexed': False},
                              {'type': 'uint256', 'name': 'fee', 'indexed': False},
                              {'type': 'uint256', 'name': 'admin_fee', 'indexed': False}],
                   'anonymous': False,
                   'type': 'event'},
                  {'name': 'NewParameters',
                   'inputs': [{'type': 'uint256', 'name': 'A', 'indexed': False},
                              {'type': 'uint256', 'name': 'fee', 'indexed': False},
                              {'type': 'uint256', 'name': 'admin_fee', 'indexed': False}],
                   'anonymous': False,
                   'type': 'event'},
                  {'outputs': [],
                   'inputs': [{'type': 'address[4]', 'name': '_coins'},
                              {'type': 'address[4]', 'name': '_underlying_coins'},
                              {'type': 'address', 'name': '_pool_token'},
                              {'type': 'uint256', 'name': '_A'},
                              {'type': 'uint256', 'name': '_fee'}],
                   'constant': False,
                   'payable': False,
                   'type': 'constructor'},
                  {'name': 'get_virtual_price',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 1570535},
                  {'name': 'calc_token_amount',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [{'type': 'uint256[4]', 'name': 'amounts'},
                              {'type': 'bool', 'name': 'deposit'}],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 6103471},
                  {'name': 'add_liquidity',
                   'outputs': [],
                   'inputs': [{'type': 'uint256[4]', 'name': 'amounts'},
                              {'type': 'uint256', 'name': 'min_mint_amount'}],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 9331701},
                  {'name': 'get_dy',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [{'type': 'int128', 'name': 'i'},
                              {'type': 'int128', 'name': 'j'},
                              {'type': 'uint256', 'name': 'dx'}],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 3489637},
                  {'name': 'get_dy_underlying',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [{'type': 'int128', 'name': 'i'},
                              {'type': 'int128', 'name': 'j'},
                              {'type': 'uint256', 'name': 'dx'}],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 3489467},
                  {'name': 'exchange',
                   'outputs': [],
                   'inputs': [{'type': 'int128', 'name': 'i'},
                              {'type': 'int128', 'name': 'j'},
                              {'type': 'uint256', 'name': 'dx'},
                              {'type': 'uint256', 'name': 'min_dy'}],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 7034253},
                  {'name': 'exchange_underlying',
                   'outputs': [],
                   'inputs': [{'type': 'int128', 'name': 'i'},
                              {'type': 'int128', 'name': 'j'},
                              {'type': 'uint256', 'name': 'dx'},
                              {'type': 'uint256', 'name': 'min_dy'}],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 7050488},
                  {'name': 'remove_liquidity',
                   'outputs': [],
                   'inputs': [{'type': 'uint256', 'name': '_amount'},
                              {'type': 'uint256[4]', 'name': 'min_amounts'}],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 241191},
                  {'name': 'remove_liquidity_imbalance',
                   'outputs': [],
                   'inputs': [{'type': 'uint256[4]', 'name': 'amounts'},
                              {'type': 'uint256', 'name': 'max_burn_amount'}],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 9330864},
                  {'name': 'commit_new_parameters',
                   'outputs': [],
                   'inputs': [{'type': 'uint256', 'name': 'amplification'},
                              {'type': 'uint256', 'name': 'new_fee'},
                              {'type': 'uint256', 'name': 'new_admin_fee'}],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 146045},
                  {'name': 'apply_new_parameters',
                   'outputs': [],
                   'inputs': [],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 133452},
                  {'name': 'revert_new_parameters',
                   'outputs': [],
                   'inputs': [],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 21775},
                  {'name': 'commit_transfer_ownership',
                   'outputs': [],
                   'inputs': [{'type': 'address', 'name': '_owner'}],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 74452},
                  {'name': 'apply_transfer_ownership',
                   'outputs': [],
                   'inputs': [],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 60508},
                  {'name': 'revert_transfer_ownership',
                   'outputs': [],
                   'inputs': [],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 21865},
                  {'name': 'withdraw_admin_fees',
                   'outputs': [],
                   'inputs': [],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 23448},
                  {'name': 'kill_me',
                   'outputs': [],
                   'inputs': [],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 37818},
                  {'name': 'unkill_me',
                   'outputs': [],
                   'inputs': [],
                   'constant': False,
                   'payable': False,
                   'type': 'function',
                   'gas': 21955},
                  {'name': 'coins',
                   'outputs': [{'type': 'address', 'name': ''}],
                   'inputs': [{'type': 'int128', 'name': 'arg0'}],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2130},
                  {'name': 'underlying_coins',
                   'outputs': [{'type': 'address', 'name': ''}],
                   'inputs': [{'type': 'int128', 'name': 'arg0'}],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2160},
                  {'name': 'balances',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [{'type': 'int128', 'name': 'arg0'}],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2190},
                  {'name': 'A',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2021},
                  {'name': 'fee',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2051},
                  {'name': 'admin_fee',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2081},
                  {'name': 'owner',
                   'outputs': [{'type': 'address', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2111},
                  {'name': 'admin_actions_deadline',
                   'outputs': [{'type': 'uint256', 'unit': 'sec', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2141},
                  {'name': 'transfer_ownership_deadline',
                   'outputs': [{'type': 'uint256', 'unit': 'sec', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2171},
                  {'name': 'future_A',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2201},
                  {'name': 'future_fee',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2231},
                  {'name': 'future_admin_fee',
                   'outputs': [{'type': 'uint256', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2261},
                  {'name': 'future_owner',
                   'outputs': [{'type': 'address', 'name': ''}],
                   'inputs': [],
                   'constant': True,
                   'payable': False,
                   'type': 'function',
                   'gas': 2291}]
