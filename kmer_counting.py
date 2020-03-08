#k length of kmer, input sequence
def kmer_count(k, sequence):
    #define dictionary to store each kmer, frequency and its indices inside the sequence
    kmer = {};
    #loops on the string starting from index 0 and tokenize it into substrings of length k
    for i in range(0, (len(sequence) - k + 1)):
        #cut substring of length k starting from index i
        sub = sequence[i:i + k];
        #check if this kmer already exists to increment frequency and if not set new frequency to 1
        if sub not in kmer.keys():
            kmer[sub] = [1,[[i, i + k - 1]]];
        else:
            #increment number frequency
            kmer[sub][0] += 1;
            #add the indices to dictionary
            kmer[sub][1].append([i, i + k - 1]);
    return kmer;

#main program
sequence1 = "ggcatcgatttgcatgtgaccgctagggact";
kmer = kmer_count(1,sequence1);
for k in kmer.keys():
    print(str(k) + " : with Frequency: " + str(kmer[k][0]));
    print(str(k) + " Occurrences (Indices): ");
    print(kmer[k][1]);
    print("-------------------------------------------------------------------");
