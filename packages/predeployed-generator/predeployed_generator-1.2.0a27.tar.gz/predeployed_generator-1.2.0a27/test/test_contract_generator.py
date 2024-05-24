import pytest
from web3.auto import w3

from src.predeployed_generator.tools import MetaNotFoundError
from .tools.custom_contract_generator import CustomContractGenerator
from .tools.test_solidity_project import TestSolidityProject
from src.predeployed_generator.contract_generator import ContractGenerator


class TestContractGenerator(TestSolidityProject):
    OWNER_ADDRESS = '0xd200000000000000000000000000000000000000'
    TESTER_ADDRESS = '0xd200000000000000000000000000000000000001'
    TESTER2_ADDRESS = '0xD200000000000000000000000000000000000002'
    CONTRACT_ADDRESS = '0xd200000000000000000000000000000000000003'

    def get_test_contract_abi(self):
        return self.get_abi(CustomContractGenerator.CONTRACT_NAME)

    def prepare_genesis(self):
        test_contract_generator = CustomContractGenerator()

        return self.generate_genesis(test_contract_generator.generate_allocation(
            self.CONTRACT_ADDRESS,
            default_admin=self.OWNER_ADDRESS,
            testers=[self.TESTER_ADDRESS, self.TESTER2_ADDRESS]))

    def test_short_string(self, tmpdir):
        self.datadir = tmpdir
        genesis = self.prepare_genesis()

        with self.run_geth(tmpdir, genesis):
            assert w3.is_connected()

            test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
            assert test_contract.functions.shortString().call() == 'short string'

    def test_long_string(self, tmpdir):
        self.datadir = tmpdir
        genesis = self.prepare_genesis()

        with self.run_geth(tmpdir, genesis):
            assert w3.is_connected()

            test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
            assert test_contract.functions.longString().call() == ' '.join(['very'] * 32) + ' long string'

    def test_bytes32(self, tmpdir):
        self.datadir = tmpdir
        genesis = self.prepare_genesis()

        with self.run_geth(tmpdir, genesis):
            assert w3.is_connected()

            test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
            assert test_contract.functions.bytes32Value().call() == CustomContractGenerator.TESTER_ROLE

    def test_addresses_array(self, tmpdir):
        self.datadir = tmpdir
        genesis = self.prepare_genesis()

        with self.run_geth(tmpdir, genesis):
            assert w3.is_connected()

            test_contract = w3.eth.contract(address=self.CONTRACT_ADDRESS, abi=self.get_test_contract_abi())
            assert test_contract.functions.testers(0).call() == self.TESTER_ADDRESS
            assert test_contract.functions.testers(1).call() == self.TESTER2_ADDRESS

    def test_generator_without_storage(self):
        class EmptyGenerator(ContractGenerator):
            pass

        bytecode = '0xbytecode'
        abi = ['function']
        meta = {'name': 'test'}
        balance = 5
        nonce = 13
        generator = EmptyGenerator(bytecode, abi, meta)
        assert generator.generate(balance=balance, nonce=nonce) == {
            'code': bytecode,
            'nonce': hex(nonce),
            'balance': hex(balance),
            'storage': {}
        }
        assert generator.get_abi() == abi
        assert generator.get_meta() == meta

    def test_non_existent_map_key_type(self):
        with pytest.raises(TypeError):
            ContractGenerator.calculate_mapping_value_slot(0, 'key', 'nonexistent')

    def test_generator_without_meta(self):
        class EmptyGenerator(ContractGenerator):
            pass

        bytecode = '0xbytecode'
        abi = ['function']
        generator = EmptyGenerator(bytecode, abi)
        assert generator.meta is None
        with pytest.raises(MetaNotFoundError):
            generator.get_meta()

    def test_generator_from_hardhat_artifact(self):
        class EmptyGenerator(ContractGenerator):
            pass

        generator = EmptyGenerator.from_hardhat_artifact(
            self.get_artifacts_path(CustomContractGenerator.CONTRACT_NAME)
        )
        assert generator.meta is None
        with pytest.raises(MetaNotFoundError):
            generator.get_meta()

    def test_keccak_calculation(self):
        class EmptyGenerator(ContractGenerator):
            pass

        web3_keccak = w3.solidity_keccak(['address'], [self.OWNER_ADDRESS])
        assert EmptyGenerator.calculate_keccak(['address'], [self.OWNER_ADDRESS]) == web3_keccak
