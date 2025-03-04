
# EVE Market Icons

This python script create an export of EVE Online market group icons from the
game files. The resulting export is a folder containing pngs in the format
`<iconid>.png`.

Icons are available [here](https://github.com/raph5/eve-market-icons/releases/tag/latest).

## Manpage

This sciprt takes 4 cli arguments:
1. The path to the SharedCache. On windows it's generaly C:/EVE/SharedCache/ or
%AppData%/Local/CCP/EVE/SharedCache. If you did not downloaded the entier game
(via the launcher) you will miss some icons.
2. The marketGroups.yaml file for SDE (https://developers.eveonline.com/).
3. The iconIDs.yaml file for SDE.
4. The output directory. If not already created the script will create it.
