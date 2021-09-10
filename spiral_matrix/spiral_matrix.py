import aiohttp
import re
from typing import List


async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                matrix = await response.text()
                listTraversingMatrixByRows = list(map(int, filter(None, re.split('\\D+', matrix))))
                n = int(len(listTraversingMatrixByRows) ** 0.5)
                result = []
                left = 0
                top = 0
                right = n - 1
                bottom = n - 1
                while left <= right and top <= bottom:
                    for i in range(top, bottom + 1):
                        result.append(listTraversingMatrixByRows[left + i * n])
                    left += 1

                    for i in range(left, right + 1):
                        result.append(listTraversingMatrixByRows[bottom * n + i])
                    bottom -= 1

                    for i in range(bottom, top - 1, -1):
                        result.append(listTraversingMatrixByRows[right + i * n])
                    right -= 1

                    for i in range(right, left - 1, -1):
                        result.append(listTraversingMatrixByRows[top * n + i])
                    top += 1
                return result
        except aiohttp.InvalidURL as err:
            print("The specified URL is invalid!")
            print(err)
        except aiohttp.ClientResponseError as err:
            print(f"Status code: {err.status}")
            print(err.message)
        except aiohttp.ClientConnectorError as err:
            print(err)
        except aiohttp.ClientError as err:
            print(err)
        except aiohttp.ServerTimeoutError as err:
            print(err)
        except aiohttp.ServerConnectionError as err:
            print(err)
        except Exception:
            print("Unknown error!")
