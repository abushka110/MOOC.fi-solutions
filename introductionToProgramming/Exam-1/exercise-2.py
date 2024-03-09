# solution
def find_gene_positions(gene, genome):
    # create list for indexes
    index_list = []
    # loop will run until there are characters in genome string
    # and will stop if there are no gene in genome
    while len(genome) != 0:
        index = genome.find(gene)
        # check if there a gene in genome
        if index != -1:
            # if it's first gene
            if index_list == []:
                index_list.append(index)
            # if there are already gene index in list
            else:
                index_list.append(index + index_list[-1] + len(gene))
            # remove gene that already found
            genome = genome[index+len(gene):]
        # break if there are no gene in genome
        else:
            break

    # return list if genes were found in genome
    if index_list != []:
        return index_list

# test
if __name__ == "__main__":
    genome = "ATCGAGATCGACGATCGTAGCTAGCTAGCTAGCGATCGA"
    gene1 = "TAGCTA"
    gene2 = "ATCGA"
    gene3 = "X"

    print(find_gene_positions(gene1, genome)) # [17, 25]
    print(find_gene_positions(gene2, genome)) # [0, 6, 34]
    print(find_gene_positions(gene3, genome)) # None
    print(type((find_gene_positions(gene3, genome)))) # <class 'NoneType'>