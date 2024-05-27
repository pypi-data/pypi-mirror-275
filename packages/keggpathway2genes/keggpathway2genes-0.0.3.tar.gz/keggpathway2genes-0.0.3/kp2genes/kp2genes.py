import argparse
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_gene_info(pathway_id):
    url = f"https://www.kegg.jp/pathway/{pathway_id}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        gene_info = []
        total_genes = 0
        for area in tqdm(soup.find_all('area', title=True), desc="Fetching genes"):
            title = area['title']
            match = title.split("), ")
            for item in match:
                try:
                    gene_id, gene_name = item.split(" (")
                    if gene_name.isupper() and ' ' not in gene_name:
                        gene_info.append((gene_id, gene_name.rstrip(')')))
                        total_genes += 1
                except ValueError:
                    continue
        return gene_info, total_genes
    else:
        print(f"Error fetching pathway page: {response.status_code}")
        return [], 0

def main(pathway_id):
    gene_info, total_genes = get_gene_info(pathway_id)
    if not gene_info:
        print(f"No gene info found for pathway {pathway_id}.")
        return
    
    with open(f"{pathway_id}.txt", "w") as file:
        file.write("Entrez_ID\tGene\n")
        for gene_id, gene_name in gene_info:
            file.write(f"{gene_id}\t{gene_name}\n")
    
    print(f"Found {total_genes} genes for pathway {pathway_id}.")

def main_cli():
    parser = argparse.ArgumentParser(description='Extract gene entries for a specific KEGG pathway.')
    parser.add_argument('-kp', '--keggpathway', required=True, help='KEGG pathway ID')
    args = parser.parse_args()

    main(args.keggpathway)

if __name__ == "__main__":
    main_cli()

