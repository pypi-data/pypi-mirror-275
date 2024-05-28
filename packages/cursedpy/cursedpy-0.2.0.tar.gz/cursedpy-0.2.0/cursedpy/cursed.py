import json
from typing import Any, Optional
from urllib.parse import urlencode
from dataclass_wizard import fromdict, asdict

import asyncio

from .http import CurseHTTP
from .types import *

class CFGames(CurseHTTP):
    async def games(self, index: Optional[int] = None, pageSize: Optional[int] = None) -> tuple[list[Game], Pagination]:
        """
        Get all games that are available to the provided API key.
        """
        query = {}
        if pageSize: query['pageSize'] = pageSize
        if index: query['index'] = index
        response = await self.api(endpoints["games"], query=query)
        pagination = Pagination(**response['pagination'])
        data = [fromdict(Game, game) for game in response['data']]
        return(data, pagination)

    async def game(self, gameId) -> Game:
        """
        Get a single game.
        A private game is only accessible by its respective API key.
        """
        response = await self.api(endpoints["game"], params={"gameId":gameId})
        print(response)
        data = fromdict(Game, response['data'])
        return(data)

    async def versions(self, gameId: int) -> list[GameVersionsByType]:
        """
        Get all available versions for each known version type of the specified game.
        A private game is only accessible to its respective API key.
        """
        response = await self.api(endpoints["versions"], params={"gameId":gameId})
        data = [fromdict(GameVersionsByType, vbt) for vbt in response['data']]
        return(data)

    async def version_types(self, gameId: int) -> list[GameVersionType]:
        """
        Currently, when creating games via the CurseForge for Studios Console, you are limited to a single game version type.
        This means that this endpoint is probably not useful in most cases and is relevant mostly when handling existing games that have multiple game versions such as World of Warcraft and Minecraft (e.g. 517 for wow_retail).
        """
        response = await self.api(endpoints["version_types"], params={"gameId":gameId})
        data = [fromdict(GameVersionType, gvt) for gvt in response['data']]
        return(data)

    # Add version types V2

class CFCategories(CurseHTTP):
    async def categories(self, gameId: int, classId: Optional[int] = None, classesOnly: Optional[bool] = None) -> list[Category]:
        """
        Get all available classes and categories of the specified game.
        Specify a game id for a list of all game categories, or a class id for a list of categories under that class.
        Specifiy the classes Only flag to just get the classes for a given game.
        """
        query = {"gameId":gameId}
        if classId: query['classId'] = classId
        if classesOnly: query['classesOnly'] = classesOnly
        response = await self.api(endpoints["categories"],query=query)
        data = [fromdict(Category, category) for category in response['data']]
        return(data)

class CFMods(CurseHTTP):
    async def search_mods(
        self, gameId: int, classId: Optional[int]=None,
        categoryId: Optional[int]=None, categoryIds: Optional[str]=None,
        gameVersion: Optional[str]=None, gameVersions: Optional[str]=None,
        searchFilter: Optional[str]=None, sortField: Optional[ModsSearchSortField]=None,
        sortOrder: Optional[SortOrder]=None, modLoaderType: Optional[ModLoaderType]=None,
        modLoaderTypes: Optional[str]=None, gameVersionTypeId: Optional[int]=None,
        authorId: Optional[int]=None, primaryAuthorId: Optional[int]=None,
        slug: Optional[str]=None, index: Optional[int]=None, pageSize: Optional[int]=None
        ) -> tuple[list[Mod], Pagination]:
        """
        Get all mods that match the search criteria.
        """
        query = {"gameId":gameId}
        # Construct optional part:
        if classId: query['classId'] = classId
        if categoryId: query['categoryId'] = categoryId
        if categoryIds: query['categoryIds'] = categoryIds
        if gameVersion: query['gameVersion'] = gameVersion
        if gameVersions: query['gameVersions'] = gameVersions 
        if searchFilter: query['searchFilter'] = searchFilter
        if sortField: query['sortField'] = sortField.value 
        if sortOrder: query['sortOrder'] = sortOrder.value
        if modLoaderType: query['modLoaderType'] = modLoaderType.value
        if gameVersionTypeId: query['gameVersionTypeId'] = gameVersionTypeId
        if authorId: query['authorId'] = authorId
        if primaryAuthorId: query['primaryAuthorId'] = primaryAuthorId
        if slug: query['slug'] = slug
        if index: query['index'] = index
        if pageSize: query['pageSize'] = pageSize
        # Call curseforge api
        response = await self.api(endpoints['search_mods'], query=query)
        pagination = Pagination(**response['pagination'])
        data = [fromdict(Mod, moddata) for moddata in response['data']]
        return(data, pagination)

    async def get_mod(self, modId: int) -> Mod:
        """
        Get a single mod.
        """
        response = await self.api(endpoints['get_mod'], params={'modId':modId})
        data = fromdict(Mod, response['data'])
        return(data)

    async def get_mods(self, modIds: list[int], filterPCOnly: Optional[bool] = True) -> list[Mod]:
        """
        Get a list of mods belonging the the same game.
        """
        body = {"modIds":modIds}
        if filterPCOnly: body["filterPCOnly"] = filterPCOnly
        response = await self.api(endpoints['get_mods'], data=body)
        data = [fromdict(Mod, moddata) for moddata in response['data']]
        return(data)

    async def get_featured_mods(self, gameId: int, excludedModIds: Optional[list] = None, gameVersionTypeId: Optional[int] = None) -> FeaturedModsResponse:
        """
        Get a list of featured, popular and recently updated mods.
        """
        body = {"gameId":gameId}
        if excludedModIds: body['excludedModIds'] = excludedModIds
        if gameVersionTypeId: body['gameVersionTypeId'] = gameVersionTypeId
        response = await self.api(endpoints['get_featured_mods'],data=body)
        data = fromdict(FeaturedModsResponse, response['data'])
        return(data)

    async def get_mod_description(self, modId: int, raw: Optional[bool] = None, stripped: Optional[bool] = None, markup: Optional[bool] = None) -> str:
        """
        Get the full description of a mod in HTML format.
        """
        query = {"modId":modId}
        if raw: query['raw'] = raw
        if stripped: query['stripped'] = stripped
        if markup: query['markup'] = markup
        response = await self.api(endpoints['get_mod_description'], query=query)
        data = response['data']
        return(data)

class CFFiles(CurseHTTP):
    async def get_mod_file(self, modId: int, fileId: int) -> File:
        """
        Get a single file of the specified mod.
        """
        response = await self.api(endpoints['get_mod_file'], params={'modId':modId, 'fileId':fileId})
        data = fromdict(Mod, response['data'])
        return(data)

    async def get_mod_files(
        self, modId: int, gameVersion: Optional[str] = None,
        modLoaderType: Optional[ModLoaderType] = None, gameVersionTypeId: Optional[int] = None,
        index: Optional[int] = None, pageSize: Optional[int] = None) -> tuple[list[File], Pagination]:
        """
        Get all files of the specified mod.
        """
        query={}
        if gameVersion: query['gameVersion'] = gameVersion
        if modLoaderType: query['modLoaderType'] = modLoaderType
        if gameVersionTypeId: query['gameVersionTypeId'] = gameVersionTypeId
        if index: query['index'] = index
        if pageSize: query['pageSize'] = pageSize
        response = await self.api(endpoints['get_mod_files'],params={'modId':modId}, query=query)
        pagination = Pagination(**response['pagination'])
        data = [fromdict(File, f) for f in response['data']]
        return(data, pagination)

    async def get_files(self, fileIds: list) -> list[File]:
        """
        Get a list of files.
        """
        body = {"fileIds":fileIds}
        response = await self.api(endpoints['get_files'], data=body)
        data = [fromdict(File, f) for f in response['data']]
        return(data)

    async def get_mod_file_changelog(self, modId: int, fileId: int) -> str:
        """
        Get the changelog of a file in HTML format.
        """
        respone = await self.api(endpoints['get_mod_file_changelog'], params={'modId':modId, 'fileId':fileId})
        data = response['data']
        return(data)

    async def get_mod_file_download_url(self, modId: int, fileId: int) -> str:
        """
        Get a download url for a specific file.
        """
        response = await self.api(endpoints['get_mod_file_download_url'], params={'modId':modId, 'fileId':fileId})
        data = response['data']
        return(data)

class CFMinecraft(CurseHTTP):
    async def get_minecraft_versions(self, sortDescending: Optional[bool] = None) -> list[MinecraftGameVersion]:
        """
        Get all Minecraft versions.
        """
        query = {}
        if sortDescending: query['sortDescending'] = sortDescending
        response = await self.api(endpoints['get_minecraft_versions'], query=query)
        data = [MinecraftGameVersion(**mc_gv) for mc_gv in response['data']]
        data = [fromdict(MinecraftGameVersion, mc_gv) for mc_gv in response['data']]
        return(data)

    async def get_specific_minecraft_version(self, gameVersionString: str) -> MinecraftGameVersion:
        """
        Get information about specific Minecraft version.
        """
        response = self.api(await endpoints['get_specific_minecraft_version'], params={'gameVersionString':gameVersionString})
        data = fromdict(MinecraftGameVersion, response['data'])
        return(data)

    async def get_minecraft_modloaders(self, version: Optional[str] = None, includeAll: Optional[bool] = None) -> list[MinecraftModLoaderIndex]:
        """
        Get list of all Minecraft modloaders.
        """
        query={}
        if version: query['version'] = version
        if includeAll: query['includeAll'] = includeAll
        response = await self.api(endpoints['get_minecraft_modloaders'], query=query)
        data = [fromdict(MinecraftModLoaderIndex, ml_idx) for ml_idx in response['data']]
        return(data)

    async def get_specific_minecraft_modloader(self, modLoaderName: str) -> MinecraftModLoaderVersion:
        """
        Get everything about specific Minecraft modloader version.
        """
        response = await self.api(endpoints['get_specific_minecraft_modloader'],params={'modLoaderName':modLoaderName})
        data = fromdict(MinecraftModLoaderVersion, response['data'])
        return(data)

class CFFingerprints(CurseHTTP):
    async def get_fingerprints_matches_by_game_id(self, gameId: int, fingerprints: list[int]) -> FingerprintsMatchesResult:
        """
        Get mod files that match a list of fingerprints for a given game id.
        """
        response = await self.api(endpoint['get_fingerprints_matches_by_game_id'],data={"fingerprints":fingerprints},params={"gameId":gameId})
        data = fromdict(FingerprintsMatchesResult, response['data'])
        return(data)
    
    async def get_fingerprints_matches(self, fingerprint: list[int]) -> FingerprintsMatchesResult:
        """
        Get mod files that match a list of fingerprints.
        """
        response = await self.api(endpoint['get_fingerprints_matches'],data={"fingerprints":fingerprints})
        data = fromdict(FingerprintsMatchesResult, response['data'])
        return(data)

    async def get_fingerprints_fuzzy_matches_by_game_id(self, gameId: int, fingerprints: list[FolderFingerprint]) -> FingerprintFuzzyMatchResult:
        """
        Get mod files that match a list of fingerprints using fuzzy matching.
        """
        response = await self.api(endpoint['get_fingerprints_fuzzy_matches_by_game_id'], data={"gameId": gameId, "fingerprints":fingerprints}, params={"gameId": gameId})
        data = fromdict(FingerprintFuzzyMatchResult, response['data'])
        return(data)

    async def get_fingerprints_fuzzy_matches(self, fingerprints: list[FolderFingerprint]) -> FingerprintFuzzyMatchResult:
        """
        Get mod files that match a list of fingerprints using fuzzy matching.
        """
        response = await self.api(endpoint['get_fingerprints_fuzzy_matches'], data={"gameId": gameId, "fingerprints":fingerprints})
        data = fromdict(FingerprintFuzzyMatchResult, response['data'])
        return(data)

class CFClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.Games = CFGames(self.api_key)
        self.Categories = CFCategories(self.api_key)
        self.Mods = CFMods(self.api_key)
        self.Files = CFFiles(self.api_key)
        self.Minecraft = CFMinecraft(self.api_key)
        self.Fingerprints = CFFingerprints(self.api_key)

    async def close(self):
        await self.Games.close()
        await self.Categories.close()
        await self.Mods.close()
        await self.Files.close()
        await self.Minecraft.close()
        await self.Fingerprints.close()