from enum import IntEnum
from typing import Tuple, List


# Гены представляются в виде последовательности символов A, C, G, T
# где каждая буква означает нуклеотид, а комбинация трех нуклеотидов
# называется кодоном. Кодон кодирует конкретную аминокислоту, которая
# вместе с другими аминокислотами может образовывать белок.
# Классическая задача биоинформатики - найти в гене определенный кодон.


Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
# псевдоним типа для кодонов
Gene = List[Codon] # псевдоним типа для генов

gene_str: str = "ACGTGGCTCTAACGGTAGA"

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s): # не выходить за пределы строки!
            return gene
        # инициализировать кодон из трех нуклеотидов
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]],
                        Nucleotide[s[i + 2]])
        gene.append(codon) # добавить кодон в ген
    return gene


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    '''Линейный поиск: сложность O(n)'''
    for codon in gene:
        if codon == key_codon:
            return True
    return False


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    '''Бинарный поиск: сложность O(lg n).
    Но сначала нужно отстортировать данные.'''
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

my_gene: Gene = string_to_gene(gene_str)

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

# print(my_gene)
# print(linear_contains(my_gene, acg))
# print(linear_contains(my_gene, gat))

# Same:
# print(acg in my_gene)
# print(gat in my_gene)

my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))

