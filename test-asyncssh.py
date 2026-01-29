import asyncio
import asyncssh
async def download_file(sftp, file: str, localdir: str):
    await sftp.get(file, localpath=f"{localdir}/{file}")
async def run_client():
    async with asyncssh.connect(
        "host", username="username", password="password"
    ) as conn:
        async with conn.start_sftp_client() as sftp:
            files = await sftp.glob("/Exports/*")
            tasks = (download_file(sftp, file, localdir="/") for file in files)
            await asyncio.gather(*tasks)
asyncio.run(run_client())

1`710`749`989