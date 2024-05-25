import aiohttp
import asyncio
from pathlib import Path
import json
import base64


def encode_binary_file(file_path):
    with open(file_path, "rb") as f:
        binary_content = f.read()
    return base64.b64encode(binary_content).decode("utf-8")


async def create_decompile_task(payload, base_url):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{base_url}/decompile", json=payload) as response:
            if response.status == 200:
                return (await response.json())["uuid"]
            else:
                print(f"Failed to create decompile task: {response.status}")
                return None


async def get_decompile_status(task_uuid, base_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{base_url}/status/{task_uuid}") as response:
            if response.status == 200:
                return (await response.json())["results"]
            else:
                print(f"Failed to get decompile status: {response.status}")
                return None


async def decompile_async(
    binary_path, address_list, decompiler_name, base_url="http://localhost:8000"
):
    payload = {
        "binary": encode_binary_file(binary_path),
        "address": address_list,
        "decompiler": decompiler_name,
    }

    # Create a decompile task
    task_uuid = await create_decompile_task(payload, base_url)
    if not task_uuid:
        return None

    # Poll the server for the status of the decompile task
    while True:
        status = await get_decompile_status(task_uuid, base_url)
        if not status:
            return None

        if status["status"] == "completed":
            return json.loads(status["result"])
        elif status["status"] == "error":
            return None

        # Wait for a few seconds before polling again
        await asyncio.sleep(2)


async def get_decompilers_async(base_url="http://localhost:8000"):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{base_url}/get_decompilers") as response:
            if response.status == 200:
                return (await response.json())["decompilers"]
            else:
                print(f"Failed to get decompilers: {response.status}")
                return None


# Example usage
async def main():
    binary_path = Path(__file__).parent / "testcases" / "test.bin.strip"
    address_list = ["0x1a00", "0x1b00"]  # Example address list
    decompiler_name = "hexrays"  # Example decompiler name
    base_url = "http://localhost:8000"  # Example base URL

    result = await decompile_async(binary_path, address_list, decompiler_name, base_url)
    print(json.loads(result))


if __name__ == "__main__":
    asyncio.run(main())
