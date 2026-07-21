"""
Garante que todos os nos de instituicao tem imageUrl no network.yaml.
Corre automaticamente via GitHub Actions quando network.yaml e atualizado.
"""
import yaml

BASE_URL = "https://raw.githubusercontent.com/Isaneedsadvisa/hfpt-logos/main/"

LOGO_MAP = {
    "2CA-Braga": "inst-2cabraga.png",
    "Altice Labs": "inst-altice.png",
    "APDP": "inst-apdp.png",
    "CCG/ZGDV": "inst-ccg-zgdv.png",
    "CeNTI": "inst-centi.png",
    "CINTESIS": "inst-cintesis.png",
    "CITEVE": "inst-citeve.png",
    "ESEP": "inst-esep.png",
    "Everythink": "inst-everythink.png",
    "FCUL": "inst-fcul.png",
    "Fraunhofer": "inst-fraunhofer.png",
    "GLINTT": "inst-glintt.png",
    "H. Sao Joao": "inst-hsj.png",
    "HSC": "inst-hsc.png",
    "INL": "inst-inl.png",
    "ISPUP": "inst-ispup.png",
    "Medida": "inst-medida.png",
    "P5": "inst-p5.png",
    "PLUX": "inst-plux.png",
    "INESC TEC": "inst-inesc-tec.png",
    "ProChild": "inst-prochild.png",
    "Speculum": "inst-speculum.png",
    "Tintex": "inst-tintex.png",
    "VirtualCare": "inst-virtualcare.png",
    "WHYMOB": "inst-whymob.png",
    "Wiselife": "inst-wiselife.png",
    "Agenda HfPT": "inst-hfpt.png",
}

with open("network.yaml") as f:
    data = yaml.safe_load(f)

fixed = 0
for node in data.get("nodes", []):
    label = node.get("label", "")
    if label in LOGO_MAP and not node.get("imageUrl"):
        node["imageUrl"] = BASE_URL + LOGO_MAP[label]
        fixed += 1
        print(f"Fixed: {label}")

if fixed:
    with open("network.yaml", "w") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print(f"Total fixed: {fixed}")
else:
    print("All imageUrls already present. No changes needed.")
