import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/user/',
                                json={'name': 'John'}) as response:
            print(response.status)
            print(await response.text())

    async with session.get('http://localhost:8080/user/1/') as response:
        print(response.status)
        print(await response.text())

    async with session.post('http://localhost:8080/user/',
                            json={'name': 'Anna'}) as response:
        print(response.status)
        print(await response.text())

    async with session.post('http://localhost:8080/post/',
                            json={'owner_name': 'John', 'owner_id': 1, 'title': 'puffs',
                                  'description': 'why do you puffs'}):
        print(response.status)
        print(await response.text())

    async with session.post('http://localhost:8080/post/',
                            json={'owner_name': 'Anna', 'owner_id': 2, 'title': 'not puffs',
                                  'description': 'why do you not puffs'}):
        print(response.status)
        print(await response.text())

    async with session.patch('http://localhost:8080/post/2/',
                             json={'owner_name': 'Anna', 'owner_id': 2, 'title': 'puffs',
                                   'description': 'why do you puffs'}):
        print(response.status)
        print(await response.text())

    async with session.get('http://localhost:8080/post/1/'):
        print(response.status)
        print(await response.text())

    async with session.delete('http://localhost:8080/post/1/'):
        print(response.status)
        print(await response.text())


asyncio.run(main())
