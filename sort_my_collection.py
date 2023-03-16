import subprocess

import discogs_client

discogs_token = subprocess.check_output("op item get \"Discogs\" --fields label=\"API Token\"", shell=True).rstrip()
discogs = discogs_client.Client('CollectionSort', user_token=discogs_token)

discs = []
for collection_item in discogs.identity().collection_folders[0].releases:
    album = collection_item.release
    discs.append({
        'artist': album.artists[0].name[4:] if album.artists[0].name.startswith("The ") else album.artists[0].name,
        'title': album.title,
        'year': album.master.year if album.master else album.year,
    })

discs.sort(key=lambda x: (x['artist'], x['year']))
disc_count = 0
for album in discs:
    disc_count += 1
    print(f'Disc {disc_count}: {album["artist"]} - {album["title"]} ({album["year"]})')