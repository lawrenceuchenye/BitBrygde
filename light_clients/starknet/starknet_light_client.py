import asyncio
from starknet_py.net.full_node_client import FullNodeClient
from dotenv import load_dotenv
import os

load_dotenv()

client = FullNodeClient(node_url=os.getenv("INFURA_STARKNET_RPC"))

async def get_starknet_proof():
    # The address you want to prove (must be a Starknet address)
    target_address ="0x3757149db508d2385e39329d3645aa2a1672ab8915b4dc6bf85d30d368629a8"
    
    # Starknet uses 'get_proof' which returns the state commitment
    # instead of the Ethereum-style eth_getProof
    proof = await client.get_storage_proof(
        contract_addresses=[target_address],
        contracts_storage_keys=[], # Storage keys if needed
        block_number="latest"
    )

    contracts_root = proof.global_roots.contracts_tree_root

    print(f"Starknet Proof: {1} Merkle Root:{hex(contracts_root)}")

asyncio.run(get_starknet_proof())
