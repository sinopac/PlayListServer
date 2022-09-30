from fastapi import FastAPI

app = FastAPI()


@app.get("/playlist")
async def get_playlist():
    return {
        "TrackCount": 2,
        "UserIsOwner": True,
        "CollectionStateToken": "3.0.1.1.7.7.7",
        "Tracks": {
            "Items": [
                {
                    "ReleaseDate": "2013-05-09T02:00:00+02:00",
                    "Duration": "00:06:07",
                    "TrackNumber": 8,
                    "IsExplicit": False,
                    "Genres": ["Pop"],
                    "Rights": ["Purchase", "FreeStream"],
                    "Album": {
                        "ReleaseDate": "2013-05-09T02:00:00+02:00",
                        "Genres": ["Pop"],
                        "Id": "music.AQEDB7k-sQABAA",
                        "Name": "Random Access Memories",
                        "ImageUrl": "https://musicimage.xboxlive.com/content/music.b13eb907-0100-11db-89ca-0019b92a3933/image?locale=en-US",
                        "Link": "https://music.microsoft.com/Album/b13eb907-0100-11db-89ca-0019b92a3933?partnerID=AwesomePartner",
                        "Source": "Collection",
                        "CompatibleSources": "Catalog, Collection",
                    },
                    "Artists": [
                        {
                            "Role": "Main",
                            "Artist": {
                                "Id": "music.AQIDAAAcxgACAA",
                                "Name": "Daft Punk",
                                "ImageUrl": "https://musicimage.xboxlive.com/content/music.c61c0000-0200-11db-89ca-0019b92a3933/image?locale=en-US",
                                "Link": "https://music.microsoft.com/Artist/c61c0000-0200-11db-89ca-0019b92a3933?partnerID=AwesomePartner",
                                "Source": "Collection",
                                "CompatibleSources": "Catalog, Collection",
                            },
                        },
                        {
                            "Role": "AlbumArtist",
                            "Artist": {
                                "Id": "music.AQIDAAAcxgACAA",
                                "Name": "Daft Punk",
                                "ImageUrl": "https://musicimage.xboxlive.com/content/music.c61c0000-0200-11db-89ca-0019b92a3933/image?locale=en-US",
                                "Link": "https://music.microsoft.com/Artist/c61c0000-0200-11db-89ca-0019b92a3933?partnerID=AwesomePartner",
                                "Source": "Collection",
                                "CompatibleSources": "Catalog, Collection",
                            },
                        },
                    ],
                    "Id": "music.AQQfN4uJ9UrnJkGWQ1G9KcPOkwe5PqgAAQ",
                    "Name": "Get Lucky (feat. Pharrell Williams)",
                    "ImageUrl": "https://musicimage.xboxlive.com/content/music.a83eb907-0100-11db-89ca-0019b92a3933/image?locale=en-US",
                    "Link": "https://music.microsoft.com/Track/a83eb907-0100-11db-89ca-0019b92a3933?partnerID=AwesomePartner",
                    "Source": "Collection",
                    "CompatibleSources": "Catalog, Collection",
                },
                {
                    "ReleaseDate": "2013-09-27T02:00:00+02:00",
                    "Duration": "00:04:46",
                    "TrackNumber": 7,
                    "IsExplicit": False,
                    "Genres": ["Electronic / Dance"],
                    "Album": {
                        "ReleaseDate": "2013-09-27T02:00:00+02:00",
                        "Genres": ["Electronic / Dance"],
                        "Id": "music.AQEDB-rrJgABAA",
                        "Name": "Aleph",
                        "ImageUrl": "https://musicimage.xboxlive.com/content/music.26ebea07-0100-11db-89ca-0019b92a3933/image?locale=en-US",
                        "Link": "https://music.microsoft.com/Album/26ebea07-0100-11db-89ca-0019b92a3933?partnerID=AwesomePartner",
                        "Source": "Collection",
                        "CompatibleSources": "Catalog, Collection",
                    },
                    "Artists": [
                        {
                            "Role": "Main",
                            "Artist": {
                                "Id": "music.AQIDAAdbyQACAA",
                                "Name": "Gesaffelstein",
                                "ImageUrl": "https://musicimage.xboxlive.com/content/music.c95b0700-0200-11db-89ca-0019b92a3933/image?locale=en-US",
                                "Link": "https://music.microsoft.com/Artist/c95b0700-0200-11db-89ca-0019b92a3933?partnerID=AwesomePartner",
                                "Source": "Collection",
                                "CompatibleSources": "Catalog, Collection",
                            },
                        },
                        {
                            "Role": "AlbumArtist",
                            "Artist": {
                                "Id": "music.AQIDAAdbyQACAA",
                                "Name": "Gesaffelstein",
                                "ImageUrl": "https://musicimage.xboxlive.com/content/music.c95b0700-0200-11db-89ca-0019b92a3933/image?locale=en-US",
                                "Link": "https://music.microsoft.com/Artist/c95b0700-0200-11db-89ca-0019b92a3933?partnerID=AwesomePartner",
                                "Source": "Collection",
                                "CompatibleSources": "Catalog, Collection",
                            },
                        },
                    ],
                    "Id": "music.AQQfObc7JPSYfEi-EiGVYbdyHAfq6y0AAQ",
                    "Name": "Aleph",
                    "ImageUrl": "https://musicimage.xboxlive.com/content/music.2debea07-0100-11db-89ca-0019b92a3933/image?locale=en-US",
                    "Link": "https://music.microsoft.com/Track/2debea07-0100-11db-89ca-0019b92a3933?partnerID=AwesomePartner",
                    "Source": "Collection",
                    "CompatibleSources": "Catalog, Collection",
                },
            ],
            "TotalItemCount": 2,
        },
        "Id": "music.playlist.56c99764-800a-00fe-552f-ee11db9370d1",
        "Name": "Playlist1",
        "ImageUrl": "https://musicimage.xboxlive.com/content/music.playlist.56c99764-800a-00fe-552f-ee11db9370d1/image?locale=en-US",
        "Link": "https://music.microsoft.com/Playlist/56c99764-800a-00fe-552f-ee11db9370d1?partnerID=AwesomePartner",
        "Source": "Collection",
        "CompatibleSources": "Catalog, Collection",

    }


@app.get("/playlist/{playlist_id}")
async def get_playlist_detail(playlist_id):
    return {"playlist_id": playlist_id}


@app.post("/playlist")
async def create_playlist(req_dict: dict):
    return {"message": "Welcome to my Playlist"}
