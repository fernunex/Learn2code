# Problem name: USACO 2018 December Contest, Bronze Problem 1. Mixing Milk
# Link: http://usaco.org/index.php?page=viewproblem2&cpid=855

def mix_two_buckets(bucket_a, bucket_b, buckets_limit, buckets):
    """
    bucket_a and bucket_b are the index of the bucket to mix on the list buckets
    the milk in bucket_a will be served in bucket_b until bucket_a is empty or 
    bucket_b is full acording to the limit in the buckets_limit

    """
    buckets[bucket_b] = buckets[bucket_b] + buckets[bucket_a]
    buckets[bucket_a] = 0
    if buckets[bucket_b] > buckets_limit[bucket_b]:
        rest = buckets[bucket_b] - buckets_limit[bucket_b]
        buckets[bucket_a] = rest
        buckets[bucket_b] = buckets_limit[bucket_b]


# Main
input_file = open('mixmilk.in', 'r')
output_file = open('mixmilk.out', 'w')

# Read input
buckets_limit = []
buckets = []

for bucket in input_file:
    bucket_info = bucket.rstrip().split()
    buckets_limit.append(int(bucket_info[0]))
    buckets.append(int(bucket_info[1]))

# 2 Mixing
for i in range(100):
    if i % 3 == 0:
        mix_two_buckets(0, 1, buckets_limit, buckets)
    elif i % 3 == 1:
        mix_two_buckets(1, 2, buckets_limit, buckets)

    else:
        mix_two_buckets(2, 0, buckets_limit, buckets)

# 3 Output
for bucket in buckets:
    output_file.write(str(bucket) + '\n')

input_file.close()
output_file.close()