#    Copyright 2020 Jonas Waeber
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
from typing import Dict, Any, Iterable
from pywaclient.endpoints import CrudEndpoint


class BlockCrudEndpoint(CrudEndpoint):

    def __init__(self, client: 'BoromirApiClient'):
        super().__init__(client, 'block')


class BlockFolderCrudEndpoint(CrudEndpoint):

    def __init__(self, client: 'BoromirApiClient'):
        super().__init__(client, 'blockfolder')
        self.path_blocks = 'blockfolder/blocks'

    def blocks(self, block_folder_id: str, complete: bool = True, limit: int = 50, offset: int = 0) -> Iterable[Dict[str, Any]]:
        """
        Retrieve a list of blocks which are part of a specific block.

        :param block_folder_id:    The id of the world the blocks should be returned from.
        :param complete:    Returns all the folders as an iterable.
        :param limit:       Determines how many articles are returned. Value between 1 and 50.
        :param offset:      Determines the offset at which articles are returned. Has to be a positive integer.
        :return:
        """
        if complete:
            return self._scroll_collection(self.path_blocks, {'id': block_folder_id}, 'entities')
        return self._post_request(self.path_blocks,
                                  {'id': block_folder_id},
                                  {'limit': limit, 'offset': offset})['entities']


