import sys,locale,random,math,copy
# -*- coding: utf-8 -*-
# penalty is squared

# the file must have the following structure:
# in the first column (column 0): ID of the subject
# in the second column (column 1): the group (containing values corresponding to the variables gr_ref, gr_from)
# in the other columns (2, 3, 4, ...) the matching variables. columns we choose are defined by the column numbers in the params variable. 

f = open ("to_match_starwords_prereg1.txt" , "r")
gr_ref = "BI"
gr_from = "MONO-PL"
grupy = { gr_ref:[], gr_from:[] }
params = [2, 3, 4] 
wagi = [1, 1, 1]
data = { gr_ref:[], gr_from:[] }

def mean(rts):
    return float(sum(rts)) / len(rts) if (len(rts)) else 0.0

def sd(rts):
    mean_rt = mean(rts)
    ss = 0.0
    for rt in rts:
        ss += (rt - mean_rt) * (rt - mean_rt)
    return math.sqrt(ss / (len(rts) - 1)) if (len(rts) > 1) else 0.0


# locale.setlocale(locale.LC_NUMERIC, 'Polish_Poland')




f.readline()

for line in f:
    parts = line.strip().split("\t")
    kod = parts[0]
    grupa = parts[1] ################################
    
    for gx in params:
        parts[gx] = locale.atof(parts[gx])

    #if (parts[5] == "dziewczynka"):
    #    parts[5] = 1
    #else:
    #    parts[5] = 2
    
    grupy[grupa].append (kod)
    data[grupa].append ([0] * len(params))
    
    for px in range(len(params)):
        data[grupa][-1][px] = parts[params[px]]

# normalizacja zmiennych wewnątrz parametrów wg gr_ref
for px in range(len(params)):
    vals = [ subject[px] for subject in data[gr_ref] ]

    p_m = mean(vals)
    p_sd = sd(vals)
    
    for grupa in [gr_from, gr_ref]:
        for sx in range(len(data[grupa])):
            data[grupa][sx][px] = (data[grupa][sx][px] - p_m) / p_sd

#brute matching
master_data = data
master_grupy = grupy
best_matched = []
best_sum_dist = 10000000
            
for ix in range (10000):
    data = copy.deepcopy(master_data)
    grupy = copy.deepcopy(master_grupy)
    
#    print (data)
    
    matched = [ [], [] ] #matched_from, matched_ref
    sum_dist = 0
    while (len(grupy[gr_ref])):
    
        refx = random.randint(0, len(grupy[gr_ref])-1)
        ref_data = data[gr_ref][refx]
        ref_subject = grupy[gr_ref][refx]
 #       print ("Biore %s" % (grupy[gr_ref][refx]))
 #       print (ref_data)
        del(grupy[gr_ref][refx])
        del(data[gr_ref][refx])

        comparisons = []
        min_dist = 100000000
        best_fromx = ""
        for fromx in range(len(grupy[gr_from])):
            from_data = data[gr_from][fromx]
            dist = 0.0
            for px in range(len(params)):
                penalty = abs(from_data[px] - ref_data[px]) * wagi[px]
                dist += penalty*penalty
            if (dist < min_dist):
                min_dist = dist
                best_fromx = fromx

        sum_dist += min_dist
        matched[0].append(grupy[gr_from][best_fromx])
        matched[1].append(ref_subject)
        
#        print ("   matched: %s" % (grupy[gr_from][best_fromx]))
        del (grupy[gr_from][best_fromx])
        del (data[gr_from][best_fromx])
    if (sum_dist < best_sum_dist):
        best_matched = matched
        best_sum_dist = sum_dist

for sx in range(len(best_matched[0])):
    print ("%s\t%s" % (best_matched[0][sx], best_matched[1][sx]))
print ("sum_dist: %d" % (best_sum_dist))
