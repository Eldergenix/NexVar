MODEL_NAMES = [
    'nexvar_40b',
    'nexvar_7b',
    'nexvar_40b_base',
    'nexvar_7b_base',
    'nexvar_1b_base',
]

HF_MODEL_NAME_MAP = {
    'nexvar_40b': 'arcinstitute/nexvar_40b',
    'nexvar_7b': 'arcinstitute/nexvar_7b',
    'nexvar_40b_base': 'arcinstitute/nexvar_40b_base',
    'nexvar_7b_base': 'arcinstitute/nexvar_7b_base',
    'nexvar_1b_base': 'arcinstitute/nexvar_1b_base',
}

CONFIG_MAP = {
    'nexvar_7b': 'configs/nexvar-7b-1m.yml',
    'nexvar_40b': 'configs/nexvar-40b-1m.yml',
    'nexvar_7b_base': 'configs/nexvar-7b-8k.yml',
    'nexvar_40b_base': 'configs/nexvar-40b-8k.yml',
    'nexvar_1b_base': 'configs/nexvar-1b-8k.yml',
}


def make_phylotag_from_gbif(
        species_name: str,
) -> dict:
    """
    Returns phylogenetic tags for a given species, to get new tags not in the metadata
    """

    import requests
    def get_taxonomy_from_gbif(species_name):
        url = f"https://api.gbif.org/v1/species/match?name={species_name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "kingdom": data.get("kingdom"),
                "phylum": data.get("phylum"),
                "class": data.get("class"),
                "order": data.get("order"),
                "family": data.get("family"),
                "genus": data.get("genus"),
                "species": data.get("species")
            }
        else:
            print(f"Could not find taxonomy for {species_name}")

    taxonomy = get_taxonomy_from_gbif(species_name)
    if taxonomy:
        phylo_tag = (
        f'd__{taxonomy["kingdom"]};'
        f'p__{taxonomy["phylum"]};'
        f'c__{taxonomy["class"]};'
        f'o__{taxonomy["order"]};'
        f'f__{taxonomy["family"]};'
        f'g__{taxonomy["genus"]};'
        f's__{taxonomy["species"]}'
    ).upper()
        phylo_tag = '|'+phylo_tag+'|'
    else:
        print(f"Could not find taxonomy for {species_name}")

    return phylo_tag.upper()

