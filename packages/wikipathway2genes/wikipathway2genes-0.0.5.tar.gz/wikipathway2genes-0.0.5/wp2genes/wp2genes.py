import argparse
import pywikipathways as pwpw

def get_gene_info(wikipathway_id):
    ensembl_ids = pwpw.get_xref_list(wikipathway_id, 'En')
    entrez_ids = pwpw.get_xref_list(wikipathway_id, 'L')
    gene_info = []
    for ensembl_id, entrez_id in zip(ensembl_ids, entrez_ids):
        gene_info.append((ensembl_id, entrez_id))
    return gene_info

def main():
    parser = argparse.ArgumentParser(description='Extract Ensembl IDs and Entrez gene IDs for a given WikiPathways ID.')
    parser.add_argument('-wp', '--wikipathway', required=True, help='WikiPathways ID')
    args = parser.parse_args()

    gene_info = get_gene_info(args.wikipathway)

    output_file = f"{args.wikipathway}.txt"

    with open(output_file, "w") as f:
        f.write("Ensembl Gene ID\tEntrez Gene ID\n")
        for ensembl_id, entrez_id in gene_info:
            f.write(f"{ensembl_id}\t{entrez_id}\n")

    print(f"Gene information written to {output_file}")

    num_genes = len(gene_info)
    print(f"Found {num_genes} genes for pathway {args.wikipathway}.")

if __name__ == '__main__':
    main()

