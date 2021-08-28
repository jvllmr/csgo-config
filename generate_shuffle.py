from csgoinvshuffle.enums import TeamSide, TagsInternalName
from csgoinvshuffle import get_inventory, ShuffleConfig
from csgoinvshuffle.inventory import Inventory

inv = get_inventory("76561198232352624")

knives = inv.filter(TagsInternalName.KNIVES)
music_kits = inv.filter(TagsInternalName.MUSIC_KITS)
for music_kit in music_kits:
    if "Matt" in music_kit.name:
        music_kits.remove(music_kit)

m4a4 = inv.filter(TagsInternalName.M4A4)
m4a1 = inv.filter(TagsInternalName.M4A1_S)
ak47 = inv.filter(TagsInternalName.AK_47)
ak47 = list(filter(lambda x: not "Safari Mesh" in x.name, ak47))




with ShuffleConfig() as sc:
    sc.add_items(m4a4)
    sc.add_items(m4a1)
    sc.add_items(knives)
    sc.add_items(music_kits)
    sc.add_items(ak47)
    sc.randomize()