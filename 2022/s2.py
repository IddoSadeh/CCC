# Lets first take care of inputs
X = int(input()) #number of names must be together
same_group = [] 
for i in range(X):
    same_group.append(set(input().split()))

Y = int(input()) # number name must not be together
diff_group = []
for i in range(Y):
    diff_group.append(set(input().split()))

G = int(input()) #number of groups
groups = []
for i in range(G):
    groups.append(set(input().split()))

#how many rules were violated?
violations = 0
# this is a set problem hence:

# each set of same_group must be a subset of one of the groups in groups
for x in same_group:
    if sum([True if x.issubset(j) else False for j in groups]) == 0:
        violations += 1

# each set of diff group must not be a subset of the groups in groups        
for y in diff_group:
    if sum([True if y.issubset(j) else False for j in groups]) != 0:
        violations += 1
print(violations)        
